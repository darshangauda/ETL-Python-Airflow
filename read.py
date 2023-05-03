from util import create_mysql_connection


def read_table(db_details, table_name, limit=0):

    source = db_details.get('SOURCE_DB')

    connection = create_mysql_connection(
        host_name=source.get('DB_HOST'),
        database_name=source.get('DB_NAME'),
        user_name=source.get('DB_USER'),
        db_pass=source.get('DB_PASS')
    )
    cursor = connection.cursor()
    if limit == 0:
        query = 'SELECT * FROM {}'.format(table_name)
    else:
        query = 'SELECT * FROM {} LIMIT {}'.format(table_name, limit)
    cursor.execute(query)
    data = cursor.fetchall()
    columns = cursor.column_names

    connection.close()

    return data, columns

# from util import load_db_details
# db = load_db_details('dev')
# data, c = read_table(db, 'student_fee')
# #
# # for d in data:
# #     print(d)
# # db = load_db_details('dev')
# # source_db = db.get('SOURCE_DB')
# # print(source_db.get('DB_HOST'))
#
# print(type(data))
# print(type(c))
