"""
A Python module to parse *ACL style conference
order files in an object-oriented manner.

Author: Nitin Madnani (nmadnani@ets.org)
Date: May, 2019
"""

import re

from datetime import datetime
from itertools import count

_METADATA_REGEXP = re.compile(r'%([^\s]+)\s+([^%]+)')


def parse_order_file_metadata(metadata_string):
    """
    A function to parse any additional metadata
    provided as part of a session or item in the
    order file. This metadata usually contains the
    room and the session chair. An example of such a
    metadata string is:
    "## %room FOO %chair1 BAR BAZ"

    This function parses such a string and creates
    a dictionary from it irrespective of the specified
    metadata categories. For example, for the above
    string, the output is the dictionary:

    {'room': 'FOO', 'chair1': 'BAR BAZ'}

    Parameters
    ----------
    metadata_string : str
        The metadata string for a session.

    Returns
    -------
    metadata_dict : dict
        A dictionary containing the metadata keys
        and values.
    """
    metadata_string = (metadata_string or '').strip()
    return dict(_METADATA_REGEXP.findall(metadata_string))


class Agenda(object):
    """
    Class encapsulating an Agenda object for a
    given event which is defined as a collection
    of `Day` objects.
    """
    def __init__(self, event):
        super(Agenda, self).__init__()
        self.event = event
        self.days = []
        self._poster_number_counter = count(1)

    def save_states(self,
                    current_tuple,
                    save_session=True,
                    save_group=True,
                    save_day=True):
        """
        A method run when we transition to a new state
        in the state machine we are using to keep track
        of progress through the order file. For example,
        at transition time, we want to save any active
        sessions to either the currently active session
        group (if it's a parallel track) or the currently
        active day, if it's a plenary session. This method
        updates the objects passed in via reference directly
        and does not return anything.

        Parameters
        ----------
        current_tuple : (Day, SesssionGroup, Session, Item)
            A tuple containing the currently active
            `Day` object, the currently active `SessionGroup`
            object (if any), the currently active
            `Session` object (if any), and the current
            active `Item` object (if any). These objects
            are passed in via reference and updated directly
            by this method.
        save_session : bool, optional
            A boolean indicating whether to save the
            currently active `Session` to either the
            session group or the day (depending on the type)
            of session), effectively being done with it.
            This may not always be necessary, e.g., when
            we are not done moving through the items in a
            a single session.
        save_group : bool, optional
            A boolean indicating whether to save the
            currently active `SessionGroup` object to
            the currently active `Day` object, effectively
            being done with it. This may not always be
            necessary, e.g., when we are not done moving
            through the parallel tracks in a single session
            group.
        save_day : bool, optional
            A boolean indicating whether to save the currently
            active `Day` object to the `Agenda`, effectively being
            done with it. This is not always necessary, e.g.,
            when the day is not yet finished.
        """
        (current_day,
         current_session_group,
         current_session,
         current_item) = current_tuple

        # if there is an active item ...
        if current_item:

            # and it's a poster not a demo, generate a poster number
            # and assign it as extended metadata; these numbers will
            # allow attendees to locate them in the real world
            if (current_item.type == 'poster' and not
                    current_item.id_.endswith('-demos')):
                poster_number = next(self._poster_number_counter)
                # NOTE: Removed poster_number for now.
                # current_item.extended_metadata['poster_number'] = poster_number

            # add it to the active session
            if current_session:
                current_session.add(current_item)

        # if there is an active session ....
        if save_session and current_session:

            # add it to the active session group
            # if any (unless it's a plenary/break session);
            if (current_session_group and
                    current_session.type not in ['plenary', 'break']):
                    current_session_group.add(current_session)

            # otherwise add it to the active day
            else:
                current_day.add(current_session)

            # also reset the poster number counter
            self._poster_number_counter = count(1)

        # save the currently active session group, if
        # any, to the active day
        if save_group and current_session_group:

            current_day.add(current_session_group)

            # also reset the poster number counter
            self._poster_number_counter = count(1)

        # save the active day to the agenda
        if save_day:
            self.days.append(current_day)

            # also reset the poster number counter
            self._poster_number_counter = count(1)

    def fromfile(self, filepath):
        """
        A method to create an `Agenda` object from
        a given order file.

        Parameters
        ----------
        filepath : str
            The path to the order file that we want
            to convert to an `Agenda` object.
        """

        # re-initialize all variables to get rid
        # of any old content
        current_day = None
        current_session_group = None
        current_session = None
        current_poster_topic = None
        current_item = None
        self.days = []

        # iterate over each line in the order file
        with open(filepath, 'r') as orderfh:
            for line in orderfh:
                line = line.strip()
                if not line:
                    continue

                # if we encounter a new day ..
                if line.startswith('* '):

                    # update the various pending states
                    if current_day:
                        self.save_states((current_day,
                                          current_session_group,
                                          current_session,
                                          current_item))

                    # once the update is finished; no sessions
                    # and session groups can be active for the
                    # new day since we just started it
                    current_session = None
                    current_session_group = None
                    current_item = None

                    # make this new day the active one
                    current_day = Day.fromstring(line)

                # if we encounter a new plenary session ...
                elif line.startswith('! '):

                    # update the various pending states
                    self.save_states((current_day,
                                      current_session_group,
                                      current_session,
                                      current_item), save_day=False)

                    # make it so that there is no group active anymore
                    # since session groups cannot span plenary sessions
                    current_session_group = None
                    current_item = None

                    # make this new plenary session the active one
                    current_session = Session.fromstring(line)

                # if we encounter a new session group ...
                elif line.startswith('+ '):

                    # update the states
                    self.save_states((current_day,
                                      current_session_group,
                                      current_session,
                                      current_item), save_day=False)

                    # there is no longer an active session
                    # or an active item
                    current_session = None
                    current_item = None

                    # make this new session group the active one
                    current_session_group = SessionGroup.fromstring(line)

                # if we encounter a new paper/poster/tutorial/best-paper
                # session ...
                elif line.startswith('= '):

                    # update states but do not yet save
                    # the currently active session group
                    # since we may still be in it
                    self.save_states((current_day,
                                      current_session_group,
                                      current_session,
                                      current_item),
                                     save_day=False,
                                     save_group=False)

                    # nullify any previously active item
                    current_item = None

                    # make this new session the active one
                    current_session = Session.fromstring(line)

                # if we encounter a poster group topic ...
                elif line.startswith('@'):

                    # update the states for pending items
                    # but do not yet save the day, the session
                    # group or the session since we are still
                    # in them
                    self.save_states((current_day,
                                      current_session_group,
                                      current_session,
                                      current_item),
                                     save_day=False,
                                     save_group=False,
                                     save_session=False)

                    # save the topic to greedily attach to
                    # the next poster we see, which should
                    # be the next line
                    current_poster_topic = line.lstrip('@ ').rstrip().replace('\&', '&')
                    current_item = None

                # if we encounter a presentation item
                # (poster/paper/tutorial) ...
                elif Item._regexp.match(line):

                    # update the states for pending items
                    # but do not yet save the day, the session
                    # group or the session since we may still
                    # be in them
                    self.save_states((current_day,
                                      current_session_group,
                                      current_session,
                                      current_item),
                                     save_session=False,
                                     save_day=False,
                                     save_group=False)

                    # make this new item the currently active one
                    matchobj = Item._regexp.match(line)
                    current_item = Item.fromstring(matchobj, current_session.type)

                    # if we have encountered a poster and
                    # we have an active poster topic, attach
                    # that topic to this poster to indicate
                    # that this is where the topic starts
                    # and then remove the active topic since
                    # we are done with it
                    if current_item.type == 'poster' and current_poster_topic:
                        current_item.topic = current_poster_topic
                        current_poster_topic = None

                else:
                    raise ValueError('Unparsable line: "{}"'.format(line))

            # after we are done iterating through the
            # lines in the file, we may still have some
            # pending items, sessions, groups, and days
            # to take care of before we are done
            self.save_states((current_day,
                              current_session_group,
                              current_session,
                              current_item))

            # now we are really done and so we can
            # nullify the current pointers since
            # they are no longer needed
            current_day = None
            current_session_group = None
            current_session = None
            current_item = None

    def __repr__(self):
        # initialize the output variable
        out = ['Agenda for event "{}":'.format(self.event)]

        # iterate over each day ...
        for day in self.days:
            out.append(str(day))

            # over each session or session group
            for content in day.contents:
                out.append(str(content))

                # over each session in each session group
                if isinstance(content, SessionGroup):
                    for session in content.sessions:
                        out.append(str(session))

                        # over each item in each parallel session
                        for item in session.items:
                            out.append(str(item))

                else:
                    # over each item in non-parallel session
                    for item in content.items:
                        out.append(str(item))

        # return the list as a string
        return '\n'.join(out)


class Day(object):
    """
    Class encapsulating a day in the order file.
    A `Day` object contains a datetime attribute
    along a list (`contents`) that can contain
    sessions (represented as `Session` objects)
    amd session groups (represented as `SessionGroup`
    objects) happening on that day.
    """
    def __init__(self, datetime):
        super(Day, self).__init__()
        self.datetime = datetime
        self.contents = []

    def __str__(self):
        return self.datetime

    def __repr__(self):
        return 'Day <{}>'.format(str(self))

    @classmethod
    def fromstring(cls, day_string):
        """
        A class method to create a `Day` instance from
        a string indicating a day in the order file.

        Parameters
        ----------
        day_string : str
            A string indicating the day in the order
            file. An example string looks like this:
            "Monday, June 2, 2019".

        Returns
        -------
        day : Day
            An instance of `Day`.
        """
        real_day_string = day_string.lstrip('* ').rstrip()
        return cls(real_day_string)

    def add(self, session_or_session_group):
        """
        A method to add a `Session` or `SessionGroup`
        object to this day.

        Parameters
        ----------
        session_or_session_group : Session or SessionGroup
            An instance of either `Session` or `SessionGroup`.
        """
        self.contents.append(session_or_session_group)


class SessionGroup(object):
    """
    Class encapsulating a session group containing parallel
    tracks in the order file. A `SessionGroup` object is
    defined by a title, a list of the sessions that it
    contains (represented as `Session` objects), a start
    time, and an end time.
    """
    _regexp = re.compile(r'([0-9]{1,2}:[0-9]{2})--([0-9]{1,2}:[0-9]{2})\s+(.*)')

    def __init__(self, title='', start_time='', end_time=''):
        super(SessionGroup, self).__init__()
        self.title = title
        self.sessions = []
        self.start = start_time
        self.end = end_time

    @classmethod
    def fromstring(cls, session_group_string):
        """
        A class method to create a `SessionGroup`
        object from a string in the order file.
        An example string looks like this:
        "11:00--12:30 Oral Sessions (long papers) and Posters"

        Parameters
        ----------
        session_group_string : str
            The string indicating a session group in
            the order file.

        Returns
        -------
        session_group : SessionGroup
            An instance of `SessionGroup`.
        """
        real_session_group_string = session_group_string.lstrip('+ ')
        (session_group_start,
         session_group_end,
         session_group_title) = cls._regexp.match(real_session_group_string).groups()

        # replace any "\&"s with "&"s
        return cls(title=session_group_title.strip().replace('\\&', '&'),
                   start_time=session_group_start.strip(),
                   end_time=session_group_end.strip())

    def add(self, session):
        """
        A method to add a session to this session group.

        Parameters
        ----------
        session : Session
            An instance of `Session`.
        """
        self.sessions.append(session)

    def __repr__(self):
        return 'SessionGroup {}--{} <{}>'.format(self.start,
                                                 self.end,
                                                 self.title)


class Session(object):
    """
    Class encapsulating a session in the order file.
    A `Session` object is defined by an ID (only
    for parallel tracks), a title, a type ("plenary",
    "break", "paper", "poster", "tutorial", or "best_paper"),
    a location (if any), a start time, an end time,
    and a session chair (if any).
    """

    # define regular expressions to parse the session strings
    _any_session_regexp = re.compile(r'^([!=])\s*(([0-9]{1,2}:[0-9]{2})--([0-9]{1,2}:[0-9]{2}))?\s*(.*?)(?:##(.*))?$')
    _session_id_regexp = re.compile('Session ([0-9A-Za-z]+)\s*:')

    def __init__(self,
                 session_id='',
                 title='',
                 type='',
                 location='',
                 start_time='',
                 end_time='',
                 chair='',
                 extended_metadata=None):
        super(Session, self).__init__()
        self.id_ = session_id
        self.title = title
        self.type = type
        self.location = location
        self.chair = chair
        self.start = start_time
        self.end = end_time
        self.items = []
        self.extended_metadata = {} if not extended_metadata else extended_metadata

    def __repr__(self):
        out = 'Session '
        if self.start:
            out += '{}--{} '.format(self.start, self.end)
        attrs = ['type={}'.format(self.type)]
        if self.id_:
            attrs.append('id={}'.format(self.id_))
        if self.title:
            attrs.append('title={}'.format(self.title))
        if self.location:
            attrs.append('room={}'.format(self.location))
        if self.chair:
            attrs.append('chair={}'.format(self.chair))
        for key, value in self.extended_metadata.items():
            attrs.append('{}={}'.format(key, value))
        out += '<' + ', '.join(attrs) + '>'

        return out

    def add(self, item):
        self.items.append(item)

    @classmethod
    def fromstring(cls, session_string):
        """
        A class method to create a `Session` instance
        from a string in the order file. The format
        of the string depends on the type of session
        and a different regular expression is used
        to parse each different session type. Here
        are some examples:

        Break : "! 12:30--14:00 Lunch Break"
        Non-break Plenary : "! 9:30--10:30 Keynote 1: Arvind Narayanan "Data as a Mirror of Society: Lessons from the Emerging Science of Fairness in Machine Learning" ## %room Nicollet Grand Ballroom"
        Paper : "= Session 1B: Speech ## %room Nicollet A %chair1 Yang Liu"
        Poster : "= Session 1F: Question Answering, Sentiment, Machine Translation, Resources \& Evaluation (Posters) ## %room Hyatt Exhibit Hall"

        Break and non-break plenary sessions are distinguished
        by the presence of the words "break/coffee/lunch". Paper
        and poster sessions are distinguished by the presence
        of the word "posters".

        Parameters
        ----------
        session_string : str
            The string indicating a session in
            the order file.

        Returns
        -------
        session : Session
            An instance of `Session`.
        """
        # plenary session or break

        # use the generic session regular expression; it must match
        # or else there is a problem
        m = cls._any_session_regexp.match(session_string)
        assert m is not None

        (starting_char,
         _,
         start_time,
         end_time,
         title,
         metadata) = m.groups()

        # make sure we have the starthing character we expect
        assert starting_char in ['!', '=']

        # if the string starts with '!', it's either a plenary session
        # or a break session
        if starting_char == '!':
            session_type = 'break' if re.search(r'registration|break|lunch|coffee', title.lower()) else 'plenary'
            id_ = ''
        # if the starting character is '=', it's a presentation
        # session with actual presentation items (paper/poster/tutorial)
        elif starting_char == '=':
            # we assume a paper session by default
            # and override based on the title
            if re.search('poster', title, re.I):
                session_type = 'poster'
                m = cls._session_id_regexp.search(title)
                if m:
                    id_ = m.group(1)
                    title = re.sub(cls._session_id_regexp, '', title)
                else:
                    id_ = ''
            elif re.search('tutorial', title, re.I):
                session_type = 'tutorial'
                id_ = ''
            elif re.search('best paper', title, re.I):
                session_type = 'best_paper'
                id_ = ''
            else:
                session_type = 'paper'
                m = cls._session_id_regexp.search(title)
                if m:
                    id_ = m.group(1)
                    title = re.sub(cls._session_id_regexp, '', title)
                else:
                    id_ = ''

        # parse any metadata we are given in the string
        metadata_dict = parse_order_file_metadata(metadata) if metadata else {}

        # if there are metdata attributes other than 'room'
        # and 'chair' in the metadata dictionary, save those
        # as extended metadata
        extra_metadata_dict = {k: v.strip() for k, v in metadata_dict.items()
                               if k not in ['room', 'chair']}

        # replace any "\&"s with "&"s in the title
        return cls(session_id=id_,
                   title=title.strip().replace('\&', '&'),
                   type=session_type,
                   location=metadata_dict.get('room', '').strip(),
                   chair=metadata_dict.get('chair1', '').strip(),
                   start_time=start_time.strip() if start_time else '',
                   end_time=end_time.strip() if end_time else '',
                   extended_metadata=extra_metadata_dict)


class Item(object):

    """
    Class encapsulating a presentation item in the
    order file. There are three main item types:
    papers, posters, and tutorials. Demo, SRW, and
    Industry items are all considered papers.
    An Item is defined by an ID, the `type` attribute
    ("paper", "poster", or "tutorial"), a title, authors,
    a track ("demos", "srw", or "industry"), a location
    (if any), a start time (if any), and an end time
    (if any).
    """

    _regexp = re.compile(r'^([0-9]+(-[a-z]+)?)(\s*([0-9]{1,2}:[0-9]{2})--([0-9]{1,2}:[0-9]{2}))?\s*(?:##(.*))?$')

    def __init__(self, id_, type, **kwargs):
        super(Item, self).__init__()
        self.id_ = id_
        self.type = type
        for key, value in kwargs.items():
            self.__setattr__(key, value)

    def __repr__(self):
        out = '{} '.format(self.type.title())
        attrs = ['id={}'.format(self.id_)]
        for key, value in self.extended_metadata.items():
            attrs.append('{}={}'.format(key, value))
        if self.type == 'poster' and self.topic:
            attrs.append('topic={}'.format(self.topic))
        out += '<' + ', '.join(attrs) + '>'

        return out

    @classmethod
    def fromstring(cls,
                   item_regex_match_object,
                   containing_session_type):
        """
        A class method to create an `Item` instance
        from a string in the order file. The format
        of the string depends on the item type, whether
        it's a paper, poster, or tutorial. All of them
        start with a numeric ID (with a possible track
        indicator of some sort) and then have various
        other attributes. Examples include:

        Regular paper/poster item: "737 15:30--15:45"
        Tutorial : "28-tutorial 9:00--12:30  ## %room Greenway DE/FG"
        A special track paper : "45-srw 15:30--15:45"

        Parameters
        ----------
        item_regex_match_object : re.MatchObject
            A match object returned by applying the
            `Item` regular expression to the string.
        containing_session_type : str
            A string indicating the type of the most recently
            active `Session` object. This lets us distinguish
            between posters and papers.

        Returns
        -------
        item : Item
            An instance of `Item`.
        """
        (item_id,
         _,
         _,
         start_time,
         end_time,
         metadata_string) = item_regex_match_object.groups()

        # parse the metadata string for the item, if any
        metadata_dict = parse_order_file_metadata(metadata_string)

        # if there are metdata attributes other than 'room'
        # in the metadata dictionary, save those as extended metadata
        extra_metadata_dict = {k: v.strip() for k, v in metadata_dict.items()
                               if k != 'room'}

        if containing_session_type == 'poster':
            return cls(item_id,
                       'poster',
                       topic='',
                       title='',
                       authors='',
                       paper_url='',
                       extended_metadata=extra_metadata_dict)
        elif (containing_session_type == 'paper' or
                containing_session_type == 'best_paper'):
            return cls(item_id,
                       'paper',
                       title='',
                       authors='',
                       paper_url='',
                       video_url='',
                       start=start_time,
                       end=end_time,
                       extended_metadata=extra_metadata_dict)
        elif containing_session_type == 'tutorial':
            assert item_id.endswith('-tutorial')
            return cls(item_id,
                       'tutorial',
                       title='',
                       authors='',
                       location=metadata_dict.get('room', '').strip(),
                       start=start_time,
                       end=end_time,
                       extended_metadata=extra_metadata_dict)
