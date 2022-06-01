"""
A Python module to parse anthology XML files (and non-anthology
metadata TSV files, if available) to obtain authors, titles,
abstracts and, optionally, anthology URLs for papers and posters.
This code is entirely in service of producing web and app schedules
for conferences and, therefore, no other metadata is extracted.
In addition, for those papers that are in the non-anthology
metadata file, no abstracts and anthology URLs are available.

Author: Nitin Madnani (nmadnani@ets.org)
Date: May, 2019
"""

import csv
import html
import re

from collections import namedtuple
from pathlib import Path

from bs4 import BeautifulSoup

# define a named tuple that will contain the metadata for each item
MetadataTuple = namedtuple('MetadataTuple',
                           ['title',
                            'authors',
                            'abstract',
                            'pdf_url',
                            'video_url'])


class ScheduleMetadata(object):
    """
    Class encapsulating an object that contains
    the metadata needed for the website and app
    schedules. The object is defined by 3 dictionaries:
    one defined by the mapping file that maps IDs in the
    anthology XML files to the IDs in the various order files,
    the second is the same as the first but in the reverse
    direction, and the third maps IDs in the order files
    to tuples containing the following metadata: title,
    authors, abstracts, and anthology URLs.
    """
    def __init__(self, metadata_dict=None, mapping_dict=None):
        super(ScheduleMetadata, self).__init__()
        self._order_id_to_metadata_dict = metadata_dict
        self._order_id_to_anthology_id_dict = mapping_dict
        self._anthology_id_to_order_id_dict = {v: k for k, v in mapping_dict.items()}

    @staticmethod
    def authors_string_to_list(authorstr):
        liststr = re.sub(r',|\band ', '|', authorstr)
        return [author.strip() for author in liststr.split('|') if author.strip()]

    @classmethod
    def _parse_id_mapping_file(cls, mapping_file, event='main'):
        """
        A private class method used to parse files
        mapping anthology IDs to IDs in the order files.
        These files are generally provided by the pub chairs.

        Parameters
        ----------
        mapping_file : str
            The path to the mapping file.
        event : str, optional
            The name of the event corresponding
            to the mapping file. The event name will
            be used as a prefix for the actual
            order ID and the combination used
            as the key. Defaults to `main`, which
            denotes the main conference event.

        Returns
        -------
        mapping_dict : dict
            A dictionary with event-suffixed order file
            IDs as the keys and anthology file IDs as the
            values.

        Raises
        ------
        FileNotFoundError
            If the mapping files does not exist.
        """

        # convert string to a Path object
        mapping_file = Path(mapping_file)

        # make sure the file exists
        if not mapping_file.exists():
            raise FileNotFoundError('File {} does not exist'.format(mapping_file))

        # iterate over each row of the file and populate
        # the dictionary we want to return
        mapping_dict = {}
        with open(mapping_file, 'r') as mappingfh:
            for line in mappingfh:
                anthology_id, order_id = line.strip().split(' ')
                mapping_dict['{}#{}'.format(order_id, event)] = anthology_id

        return mapping_dict

    @classmethod
    def _parse_anthology_xml(cls, xml_file):
        """
        A private class method used to parse the
        anthology XML files containing the metadata
        for each paper.

        Parameters
        ----------
        xml_file : str
            Path to the xml file to parse.

        Returns
        -------
        anthology_dict : dict
            A dictionary with the anthology ID from
            the XML file as the key and a `MetdataTuple`
            instance containing the corresponding
            metadata as the value.

        Raises
        ------
        FileNotFoundError
            If the xml file does not exist.
        """

        # initialize the output dictionary
        anthology_dict = {}

        # make sure the file exists
        xml_file = Path(xml_file)
        if not xml_file.exists():
            raise FileNotFoundError('File {} does not exist'.format(xml_file))

        # parse the XML file using BeautifulSoup and extract
        # the metadata items we need for each paper; note that
        # we do not care about which volume the paper is in
        with open(xml_file, 'r') as xmlfh:
            soup = BeautifulSoup(xmlfh, 'xml')
            for paper in soup.find_all('paper'):

                # get the anthology ID
                id_ = '{}-{}'.format(xml_file.stem, paper['id'])

                # get the paper title
                title = paper.title.text

                # sometimes there are angle brackets
                # in the title which can cause problems
                # unless we escape them
                if '<' in title:
                    title = html.escape(title)

                # get the abstract which may not exist for all papers
                abstract = '' if not paper.abstract else paper.abstract.text

                # get the paper's anthology URL
                anthology_url = paper.url.text

                # TODO: get the video URL from the anthology
                # XML file if it has it or from somewhere else
                video_url = ''

                # get the authors which also may not exist for all papers
                authorlist = []
                if paper.find_all('author'):
                    authortags = paper.find_all('author')
                    authorlist = ['{} {}'.format(author.first.text, author.last.text) for author in authortags]

                # create the named tuple and save it in the dictionary
                anthology_dict[id_] = MetadataTuple(title=title,
                                                    authors=authorlist,
                                                    abstract=abstract,
                                                    pdf_url=anthology_url,
                                                    video_url=video_url)

        # return the output dictionary
        return anthology_dict

    @classmethod
    def _parse_non_anthology_file(cls, event, non_anthology_tsv):
        """
        A private class method used to parse the
        non-anthology metadata TSV file for a given
        event containing the titles, authors, and abstracts
        for order file IDs.

        Parameters
        ----------
        event : str
            The event to which this file applies.
        non_anthology_tsv : str
            Path to non-anthology metadata TSV file.

        Returns
        -------
        non_anthology_dict : dict
            A dictionary with the order file IDs
            in the TSV file as the key and `MetadataTuple`
            instances as values, with only the `title`
            and `author` fields populated.

        Raises
        ------
        FileNotFoundError
            If the non-anthology TSV file does not exist.
        """
        # initialize the return dictionary
        non_anthology_dict = {}

        # make sure the file actually exists
        non_anthology_tsv = Path(non_anthology_tsv)
        if not non_anthology_tsv.exists():
            raise FileNotFoundError('File {} does not exist'.format(non_anthology_tsv))

        # iterate over each TSV row and create a new
        # MetadataTuple instance and add to dictionary
        # to the `main` event space since this file is
        # assumed to be just necessary for the main
        # conference and no other events.
        with open(non_anthology_tsv, 'r') as nonanthfh:
            reader = csv.DictReader(nonanthfh,
                                    dialect=csv.excel_tab)
            for row in reader:
                title = row['title'].strip()
                authors = ScheduleMetadata.authors_string_to_list(row['authors'].strip())
                abstract = row['abstract'].strip() if row.get('abstract') else None
                value = MetadataTuple(title=title,
                                      authors=authors,
                                      abstract=abstract,
                                      pdf_url='',
                                      video_url='')
                key = '{}#{}'.format(row['paper_id'].strip(), event)
                non_anthology_dict[key] = value

        # return the dictionary
        return non_anthology_dict

    @classmethod
    def fromfiles(cls,
                  xmls=[],
                  mappings={},
                  extra_metadata_files={}):
        """
        Class method to create an instance of
        `ScheduleMetadata` from the set of
        relevant files.

        Parameters
        ----------
        xmls : list, optional
            List of anthology XML files.
        mappings : dict, optional
            Dictionary of event names as keys
            and paths to ID mapping (`id_map.txt`) files
            as values.
        extra_metadata_files : dict, optional
            Dictionary of event names as keys and
            paths to non-anthology metadata files
            as values. These are TSV files containing
            title, authors, and abstract metdata for the
            order file IDs that are _not_ in the anthology
            XML files.

        Returns
        -------
        schedule_metadata : ScheduleMetadata
            A populated instance of `ScheduleMetadata`.
        """
        # initialize dictionaries we need for later
        order_id_to_anthology_id_dict = {}
        order_id_to_metadata_dict = {}
        anthology_metadata_dict = {}

        # parse the ID mapping files first and update the
        # relevant dictionary with the results
        for event, mapping in mappings.items():
            order_id_to_anthology_id_dict.update(cls._parse_id_mapping_file(mapping, event=event))

        # next parse all of the anthology XML files and update
        # the relevant dictionary with the results
        for xml in xmls:
            anthology_metadata_dict.update(cls._parse_anthology_xml(xml))

        # next create the bridge between the paper ID and
        # the anthology metadata
        for (order_id,
             anthology_id) in order_id_to_anthology_id_dict.items():
            order_id_to_metadata_dict[order_id] = anthology_metadata_dict[anthology_id]

        # next handle the non-anthology metadata TSV file
        # if one has been provided and update the
        # bridged dictionary
        if extra_metadata_files:
            for event, extra_metadata_file in extra_metadata_files.items():
                order_id_to_metadata_dict.update(cls._parse_non_anthology_file(event, extra_metadata_file))

        # finally return an instance of ScheduleMetadata
        # with the dictionaries populated
        return cls(metadata_dict=order_id_to_metadata_dict,
                   mapping_dict=order_id_to_anthology_id_dict)

    def lookup(self, id_, event='main'):
        """
        Look up metadata for an order file ID from a particular event
        or an anthology ID. For order file IDs, the default event is
        `main` which refers to the main conference. The event names
        would have been provided when this dictionary was populated.

        We infer whether the given ID is an anthology ID if it
        start with 'N', 'W', or 'S', since order file IDs
        always start with a number.

        Parameters
        ----------
        id_ : str
            Order file ID or anthology ID.
        event : str, optional
            The name of the event to which the order
            file ID belongs. This is necessary since
            order file IDs are not globally unique
            across the main confernece and the
            various workshops. Defaults to `main`
            which denotes IDs from the main conference.

        Returns
        -------
        metadata_tuple : MetadataTuple
            An instance of `MetadataTuple` containing
            the metdata for the given ID.

        Raises
        ------
        KeyError
            If no metadata could be found for the given
            ID.
        """
        if id_[0] in ['N', 'W', 'S']:
            order_id = self._anthology_id_to_order_id_dict[id_]
        else:
            order_id = '{}#{}'.format(id_, event)

        try:
            value = self._order_id_to_metadata_dict[order_id]
        except KeyError:
            raise KeyError('Could not find metadata for ID '
                           '{} within event "{}"'.format(id_, event))
        else:
            return value
