import pandas as pd
from config import DB_DETAILS
from mysql import connector as mc


def load_db_details(env):
    return DB_DETAILS[env]


def create_mysql_connection(host_name, database_name, user_name, db_pass):
    connection = None
    try:
        connection = mc.connect(
            host=host_name,
            database=database_name,
            user=user_name,
            password=db_pass
        )
    except mc.Error as error:
        if error.errno == mc.errors.ProgrammingError:
            print('Invalid Credentials')
        else:
            print(error)

    return connection


def get_tables(path, table_list):
    tables = pd.read_csv(path, delimiter=':')
    if table_list == 'all':
        return tables[tables['to_be_loaded'] == 'yes']
    else:
        table_list_df = pd.DataFrame(table_list.split(','), columns=['table_name'])
        return tables.merge(table_list_df, on='table_name').query('to_be_loaded == "yes"')

# table = get_tables('table_list')
#
# print([print(t) for t in table['table_name']])