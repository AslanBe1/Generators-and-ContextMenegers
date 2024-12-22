import psycopg2

class DatabaseConnection:
    def __init__(self, host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.connection = None

    def __enter__(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                port=self.port
            )
            return self.connection
        except psycopg2.DatabaseError as e:
            print(e)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection and not self.connection.closed:
            self.connection.close()

if __name__ == '__main__':
    db_info = {
        'host': 'localhost',
        'database': 'najot_talim',
        'user': 'postgres',
        'password': '123',
        'port': 5432
    }
    with DatabaseConnection(**db_info) as connection:
        with connection.cursor() as cursor:
            cursor.execute('select * from persons')
            print(cursor.fetchall())

# conn= psycopg2.connect(
#     dbname = 'najot_talim',
#     user = 'postgres',
#     password = '123',
#     host = 'localhost',
#     port = '5432'
# )
# cur = conn.cursor()
#
# cur.execute('''
# CREATE TABLE IF NOT EXISTS persons (
#     id serial PRIMARY KEY,
#     full_name varchar(255),
#     age INT NOT NULL
# );''')
# conn.commit()
