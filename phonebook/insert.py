from bisect import insort_right

import psycopg2
from config import load_config

def insert_contact(firstname, lastname, phone):
    sql = """INSERT INTO contacts(firstname, lastname, phone)
             VALUES(%s, %s, %s) RETURNING id;"""
    contact_id = None
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (firstname, lastname, phone))
                rows = cur.fetchone()
                if rows:
                    contact_id = rows[0]
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return contact_id

if __name__ == '__main__':
    insert_contact("John", "Smith", "122313456")