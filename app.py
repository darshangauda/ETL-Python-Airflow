import sys
from util import get_tables, load_db_details
from read import read_table
from write import load_table
import os
import loguru as logger


def main():
    """Program takes atleast one argument"""
    name = None
    env = sys.argv[1]
    db = load_db_details(env)
    logger.logger.add('data-copier.info',
                      rotation='1 MB',
                      retention='10 days',
                      level='INFO')
    logger.logger.add('data-copier.err',
                      rotation='1 MB',
                      retention='10 days',
                      level='ERROR')
    tables = get_tables('table_list', 'all')
    for table in tables['table_name']:
        name = table
        logger.logger.info('Reading data from {}'.format(name))
    data, columns = read_table(db_details=db, table_name=name)
    for rec in data:
        print(rec)
    logger.logger.info('Loading data into {}'.format(name))
    load_table(db, data, columns, 'student_fee_copy')


print(os.getenv('SOURCE_DB_USER'))

if __name__ == "__main__":
    main()
