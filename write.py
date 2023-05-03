from util import create_mysql_connection


def build_insert_query(table_name, column_names):
    column_names_string = ', '.join(column_names)
    column_values = tuple(map(lambda column: column.replace(column, '%s'), column_names))
    column_values_string = ', '.join(column_values)
    query = ('INSERT INTO {} ({}) VALUES ({})'.format(table_name, column_names_string, column_values_string))
    return query


def insert_data(connection, cursor, query, data, batch_size=100):
    recs = []
    count = 1
    for rec in data:
        recs.append(rec)
        if count % batch_size == 0:
            cursor.executemany(query, recs)
            connection.commit()
            recs = []
        count += 1
    cursor.executemany(query, recs)
    connection.commit()


def load_table(db_details, data, column_names, table_name):
    target = db_details['TARGET_DB']

    connection = create_mysql_connection(
        host_name=target.get('DB_HOST'),
        database_name=target.get('DB_NAME'),
        user_name=target.get('DB_USER'),
        db_pass=target.get('DB_PASS')
    )
    cursor = connection.cursor()
    query = build_insert_query(table_name, column_names)
    # print(query)
    insert_data(connection, cursor, query, data)

    connection.close()


# print(build_insert_query('student_fee', ['id', 'name']))


