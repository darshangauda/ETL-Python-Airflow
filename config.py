import os

"""Dev, UAT, Testing , Prod all have different login credentials.
Dev team does not have user and pass credentials to log into prod databases.
Hence dev team should log into their own dev specific databases."""


DB_DETAILS = {
    'dev': {
        'SOURCE_DB': {
            'DB_TYPE': 'mysql',
            'DB_HOST': 'zeyodb.cveqgaujeiwd.ap-south-1.rds.amazonaws.com',
            'DB_NAME': 'student',
            'DB_USER': os.environ.get('SOURCE_DB_USER'),
            'DB_PASS': os.getenv('SOURCE_DB_PASS')
        },
        'TARGET_DB': {
            'DB_TYPE': 'mysql',
            'DB_HOST': 'zeyodb.cveqgaujeiwd.ap-south-1.rds.amazonaws.com',
            'DB_NAME': 'student',
            'DB_USER': os.getenv('TARGET_DB_USER'),
            'DB_PASS': os.getenv('TARGET_DB_PASS')
        }
    }
}

# source_db = DB_DETAILS.get('SOURCE_DB')
# print(source_db)
# host_name = source_db.get('DB_HOST')
# print(source_db)