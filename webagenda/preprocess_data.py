#!/usr/bin/env python3
"""
Extract raw data and generate the files needed for generate.py.
"""

import csv
import json
import logging
import re

from pathlib import Path

_THIS_DIR = Path(__file__).absolute().parent

# Change the hard-coded paths below
# Input files
_ORDER_OUTLINE_ = _THIS_DIR / 'raw' / 'order-outline.txt'
_RAW_PAPER_SCHEDULE = _THIS_DIR / 'raw' / 'Detailed Schedule - reformatted version.tsv'
_RAW_POSTER_IN_PERSON_SCHEDULE = _THIS_DIR / 'raw' / 'Detailed Schedule - Poster in-person sessions.tsv'
_RAW_POSTER_VIRTUAL_SCHEDULE = _THIS_DIR / 'raw' / 'Detailed Schedule - Posters virtual.tsv'
_RAW_FINDINGS_SCHEDULE = _THIS_DIR / 'raw' / 'Detailed Schedule - Findings in-person.tsv'
_RAW_PAPER_DETAILS = _THIS_DIR / 'raw' / 'Accepted papers main info for detailed program - Accepted_papers_main.tsv'
_RAW_FINDINGS_DETAILS = _THIS_DIR / 'raw' / 'Accepted papers main info for detailed program - Accepted_papers_findings.tsv'
_INDUSTRY_ALL = _THIS_DIR / 'raw' / 'Detailed Schedule - Industry.tsv'
_DEMO_POSTER = _THIS_DIR / 'raw' / 'Detailed Schedule - Demos.tsv'
_SRW_POSTER_IN_PERSON_SCHEDULE = _THIS_DIR / 'raw' / 'SRW Detailed Schedule - SRW Poster in-person sessions.tsv'
_SRW_POSTER_VIRTUAL_SCHEDULE = _THIS_DIR / 'raw' / 'SRW Detailed Schedule - Posters virtual.tsv'
_SRW_PAPER_DETAILS = _THIS_DIR / 'raw' / 'SRW Accepted papers info for detailed program - Accepted_papers_main.tsv'
# Output files
_ORDER_PREPROCESSED = _THIS_DIR / 'preprocessed' / 'order.txt'
_METADATA = _THIS_DIR / 'preprocessed' / 'metadata.tsv'


class RawSchedule:

    def __init__(self):
        self.records = []

    def read_tsv(self, path, extra_info=None):
        new_records = []
        with open(path) as fin:
            reader = csv.DictReader(fin, dialect=csv.excel_tab)
            for row in reader:
                record = {key: value.strip() for (key, value) in row.items() if key}
                record['Source'] = path.name
                if extra_info:
                    record.update(extra_info)
                new_records.append(record)
        logging.info('Read %d records from %s', len(new_records), path)
        self.records += new_records

    def check_duplicates(self):
        paper_id_to_record = {}
        for record in self.records:
            paper_id = record['Paper ID']
            if paper_id in paper_id_to_record:
                logging.warning('Repeated ID in raw schedule files: {}'.format(paper_id))
                logging.warning('    {}'.format(paper_id_to_record[paper_id]))
                logging.warning('    {}'.format(record))
            paper_id_to_record[paper_id] = record

    def search(self, query):
        for record in self.records:
            if all(record.get(key) == query[key] for key in query):
                if record.get('used'):
                    logging.warning('Reappearing schedule record: {}'.format(record))
                record['used'] = True
                yield record

    def report_unused(self):
        for record in self.records:
            if not record.get('used'):
                logging.warning('Unused schedule record: {}'.format(record))

    def record_to_order_line(self, record):
        order_line = record['Paper ID']
        metadata = {}
        if record.get('Paper Awards'):
            metadata['award'] = record['Paper Awards'].replace(' ', '_')
        if metadata:
            order_line += ' ## ' + ' '.join(
                    '%{} {}'.format(key, value) for (key, value) in metadata.items())
        return order_line


class RawMetadata:

    def __init__(self):
        self.records = []

    def read_tsv(self, path, track_override=None):
        new_records = []
        with open(path) as fin:
            reader = csv.DictReader(fin, dialect=csv.excel_tab)
            for row in reader:
                paper_id = row.get('Number') or row.get('Paper ID')
                paper_id = re.sub(r'SRW_(\d+)', r'\1-srw', paper_id)    # TODO: Remove this hack
                track = track_override or row.get('Track')
                new_records.append({
                    'paper_id': paper_id,
                    'track': track,
                    'title': row['Title'],
                    'authors': row['Authors'],
                    'source': path.name,
                    })
        logging.info('Read %d metadata records from %s', len(new_records), path)
        self.records += new_records

    def check_duplicates(self):
        paper_id_to_record = {}
        for record in self.records:
            paper_id = record['paper_id']
            if paper_id in paper_id_to_record:
                logging.warning('Repeated ID in raw metadata files: {}'.format(paper_id))
                logging.warning('    {}'.format(paper_id_to_record[paper_id]))
                logging.warning('    {}'.format(record))
            paper_id_to_record[paper_id] = record

    def mark_used(self, paper_id):
        for record in self.records:
            if record['paper_id'] == paper_id:
                if record.get('used'):
                    logging.warning('Re-queried metadata record: {}'.format(record))
                record['used'] = True

    def report_unused(self):
        for record in self.records:
            if not record.get('used'):
                logging.warning('Unused metadata record: {}'.format(record))

    def dump_metadata(self, path):
        with open(path, 'w') as fout:
            print('paper_id\ttrack\ttitle\tauthors', file=fout)
            for record in self.records:
                print('{}\t{}\t{}\t{}'.format(
                    record['paper_id'],
                    record['track'],
                    record['title'],
                    record['authors']), file=fout)
        logging.info('Wrote %d metadata records to %s', len(self.records), path)


def main():
    # set up the logging
    logging.basicConfig(format='%(levelname)s - %(message)s', level=logging.INFO)

    raw_schedule = RawSchedule()
    raw_metadata = RawMetadata()

    # Read data
    raw_schedule.read_tsv(_RAW_PAPER_SCHEDULE)
    raw_schedule.read_tsv(_RAW_POSTER_IN_PERSON_SCHEDULE, extra_info={'Format': 'in-person'})
    raw_schedule.read_tsv(_RAW_POSTER_VIRTUAL_SCHEDULE, extra_info={'Format': 'virtual'})
    raw_schedule.read_tsv(_RAW_FINDINGS_SCHEDULE)
    raw_schedule.read_tsv(_INDUSTRY_ALL)
    raw_schedule.read_tsv(_DEMO_POSTER)
    raw_schedule.read_tsv(_SRW_POSTER_IN_PERSON_SCHEDULE)
    raw_schedule.read_tsv(_SRW_POSTER_VIRTUAL_SCHEDULE, extra_info={'Format': 'virtual'})
    raw_schedule.check_duplicates()

    raw_metadata.read_tsv(_RAW_PAPER_DETAILS)
    raw_metadata.read_tsv(_RAW_FINDINGS_DETAILS)
    raw_metadata.read_tsv(_INDUSTRY_ALL, track_override='Industry')
    raw_metadata.read_tsv(_DEMO_POSTER, track_override='Demo')
    raw_metadata.read_tsv(_SRW_PAPER_DETAILS)
    raw_metadata.check_duplicates()

    # Process the `order` file
    with open(_ORDER_OUTLINE_) as fin, open(_ORDER_PREPROCESSED, 'w') as fout:
        for line in fin:
            if line[0] == '{':
                # Search for matching papers
                for record in raw_schedule.search(json.loads(line)):
                    order_line = raw_schedule.record_to_order_line(record)
                    print(order_line, file=fout)
                    raw_metadata.mark_used(record['Paper ID'])
            else:
                fout.write(line)
    raw_schedule.report_unused()
    raw_metadata.report_unused()
    raw_metadata.dump_metadata(_METADATA)


if __name__ == '__main__':
    main()
