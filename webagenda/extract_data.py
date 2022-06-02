#!/usr/bin/env python3

"""
Extract raw data and generate the files needed for generate.py.
"""

import csv
import json
import logging

from pathlib import Path

_THIS_DIR = Path(__file__).absolute().parent

# Change the hard-coded paths below
# Input files
_ORDER_OUTLINE_ = _THIS_DIR / 'data' / 'order-outline.txt'
_RAW_PAPER_SCHEDULE = _THIS_DIR / 'data' / 'Detailed Schedule - reformatted version.tsv'
_RAW_POSTER_SCHEDULE = _THIS_DIR / 'data' / 'Detailed Schedule - Poster sessions.tsv'
_RAW_PAPER_DETAILS = _THIS_DIR / 'data' / 'Accepted papers main info for detailed program - Accepted_papers_main info for detailed program.tsv'
_INDUSTRY_ORAL_1 = _THIS_DIR / 'data' / 'NAACL_2022_Industry_Track_oral_session1.csv'
_INDUSTRY_ORAL_2 = _THIS_DIR / 'data' / 'NAACL_2022_Industry_Track_oral_session2.csv'
_INDUSTRY_POSTER = _THIS_DIR / 'data' / 'NAACL_2022_Industry_Track_posters.csv'
# Output files
_ORDER_FINAL = _THIS_DIR / 'data' / 'order-final.txt'
_METADATA = _THIS_DIR / 'data' / 'metadata.tsv'


class RawSchedule:

    def __init__(self):
        self.records = []

    def read_tsv(self, path):
        new_records = []
        with open(path) as fin:
            reader = csv.DictReader(fin, dialect=csv.excel_tab)
            for row in reader:
                new_records.append(
                        {key: value.strip() for (key, value) in row.items()})
        logging.info('Read %d records from %s', len(new_records), path)
        self.records += new_records

    def read_industry_csv(self, path, session_name, metadata_fout):
        new_records = []
        with open(path) as fin:
            reader = csv.DictReader(fin)
            for row in reader:
                print('{}\t{}\t{}\t{}'.format(
                    row['number'] + '-industry',
                    'Industry',
                    row['title'],
                    row['authors'].replace('|', ', ')), file=metadata_fout)
                new_records.append({
                    'Session Name': session_name,
                    'Paper ID': row['number'] + '-industry'})
        logging.info('Read %d records from %s', len(new_records), path)
        self.records += new_records

    def search(self, query):
        for record in self.records:
            if all(record.get(key) == query[key] for key in query):
                if record.get('used'):
                    logging.warning('Repeated record: {}'.format(record))
                record['used'] = True
                yield record

    def report_unused(self):
        for record in self.records:
            if not record.get('used'):
                logging.warning('Unused record: {}'.format(record))


def main():
    # set up the logging
    logging.basicConfig(format='%(levelname)s - %(message)s', level=logging.INFO)

    with open(_RAW_PAPER_DETAILS) as fin, open(_METADATA, 'w') as fout:
        fin.readline()
        print('paper_id\ttrack\ttitle\tauthors', file=fout)
        for line in fin:
            print(line.rstrip('\n'), file=fout)

    raw_schedule = RawSchedule()
    # Read the paper and poster schedules
    raw_schedule.read_tsv(_RAW_PAPER_SCHEDULE)
    raw_schedule.read_tsv(_RAW_POSTER_SCHEDULE)
    with open(_METADATA, 'a') as fout:
        raw_schedule.read_industry_csv(_INDUSTRY_ORAL_1, 'Industry Oral 1', fout)
        raw_schedule.read_industry_csv(_INDUSTRY_ORAL_2, 'Industry Oral 2', fout)
        raw_schedule.read_industry_csv(_INDUSTRY_POSTER, 'Industry Poster', fout)

    # Process the `order` file
    with open(_ORDER_OUTLINE_) as fin, open(_ORDER_FINAL, 'w') as fout:
        for line in fin:
            if line[0] == '{':
                # Search for matching papers
                for record in raw_schedule.search(json.loads(line)):
                    fout.write('{} #\n'.format(record['Paper ID'].replace(' ', '_')))
            else:
                fout.write(line)
    raw_schedule.report_unused()


if __name__ == '__main__':
    main()
