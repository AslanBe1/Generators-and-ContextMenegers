from project1 import DatabaseConnection

db_info = {
    'host': 'localhost',
    'database': 'najot_talim',
    'user': 'postgres',
    'password': '123',
    'port': 5432
}

class Person:
    def __init__(self, full_name,age):
        self.full_name = full_name
        self.age = age


    def save(self):
        with DatabaseConnection(**db_info) as connection:
            with connection.cursor() as cursor:
                insert_person_query = '''INSERT INTO persons(full_name, age) VALUES (%s, %s);'''
                data = (self.full_name, self.age)
                cursor.execute(insert_person_query, data)
                connection.commit()
                print('Person successfully Added')


    @staticmethod
    def get_all_persons():
        try:
            with DatabaseConnection(**db_info) as connection:
                with connection.cursor() as cursor:
                    cursor.execute('SELECT * FROM persons')
                    rows = cursor.fetchall()
                    return rows
        except Exception as e:
            print(e)


    @staticmethod
    def get_one_person(persons_id):
        try:
            with DatabaseConnection(**db_info) as connection:
                with connection.cursor() as cursor:

                    cursor.execute('SELECT * FROM persons WHERE id=%s;', (persons_id,))
                    person = cursor.fetchone()

                    if person:
                        query = 'SELECT * FROM persons WHERE id=%s;'
                        data = (persons_id,)
                        cursor.execute(query, data)
                        rows = cursor.fetchone()
                        return rows

                    else:
                        return 'Person not found'

        except Exception as e:
            print(e)

    @staticmethod
    def update_person(person_id, full_name, age):
        try:
            with DatabaseConnection(**db_info) as connection:
                with connection.cursor() as cursor:

                    cursor.execute('SELECT * FROM persons WHERE id=%s;', (person_id,))
                    person = cursor.fetchone()

                    if person:
                        query = 'UPDATE persons SET full_name=%s, age=%s WHERE id=%s;'
                        data = (full_name, age, person_id)
                        cursor.execute(query, data)
                        connection.commit()
                        print('Person successfully Updated')
                    else:
                        print('Person not found')

        except Exception as e:
            print(e)


    @staticmethod
    def delete_person(persons_id):
        try:
            with DatabaseConnection(**db_info) as connection:
                with connection.cursor() as cursor:

                    cursor.execute('SELECT * FROM persons WHERE id=%s;', (persons_id,))
                    person = cursor.fetchone()

                    if person:
                        query = 'DELETE FROM persons WHERE id=%s;'
                        data = (persons_id,)
                        cursor.execute(query, data)
                        connection.commit()
                        print('Person successfully Deleted')
                    else:
                        print('Person not found')

        except Exception as e:
            print(e)


# john = Person('John', 25)
# john.save()
# ann = Person('ann', 18)
# ann.save()

# Person.get_all_persons()
# print(Person.get_all_persons())
#
# Person.update_person(6,'Tom',36)
# one_person = Person.get_one_person(6)
# print(one_person)
#
# Person.delete_person(6)