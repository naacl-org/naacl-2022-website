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
_ORDER_OUTLINE_ = _THIS_DIR / 'data' / 'order-outline.txt'
_RAW_PAPER_SCHEDULE = _THIS_DIR / 'data' / 'raw-paper-schedule.tsv'
_RAW_POSTER_SCHEDULE = _THIS_DIR / 'data' / 'raw-poster-schedule.tsv'
_ORDER_FINAL = _THIS_DIR / 'data' / 'order-final.txt'


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

    def search(self, query):
        for record in self.records:
            if all(record.get(key) == query[key] for key in query):
                yield record


def main():
    # set up the logging
    logging.basicConfig(format='%(levelname)s - %(message)s', level=logging.INFO)

    raw_schedule = RawSchedule()
    # Read the paper and poster schedules
    raw_schedule.read_tsv(_RAW_PAPER_SCHEDULE)
    raw_schedule.read_tsv(_RAW_POSTER_SCHEDULE)

    # Process the `order` file
    with open(_ORDER_OUTLINE_) as fin, open(_ORDER_FINAL, 'w') as fout:
        for line in fin:
            if line[0] == '{':
                # Search for matching papers
                for record in raw_schedule.search(json.loads(line)):
                    fout.write('{} #\n'.format(record['Paper ID'].replace(' ', '_')))
            else:
                fout.write(line)


if __name__ == '__main__':
    main()
