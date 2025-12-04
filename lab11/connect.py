import psycopg2
from config import load_config

def connect(config):
    """ Connect to the PostgreSQL database server """
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            print('Connected to the PostgreSQL server.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


if __name__ == '__main__':
    config = load_config()
    connect(config)


    def get_contacts():

        sql = "SELECT * FROM contacts;"

        config = load_config()
        try:
            with psycopg2.connect(**config) as conn:
                with conn.cursor() as cur:
                    cur.execute(sql)

                    print("The number of contacts: ", cur.rowcount)

                    row = cur.fetchone()

                    while row is not None:
                        print(row)
                        row = cur.fetchone()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)


    def get_contacts_phone():

        sql = "SELECT id, phone FROM contacts ORDER BY id;"

        config = load_config()
        try:
            with psycopg2.connect(**config) as conn:
                with conn.cursor() as cur:
                    cur.execute(sql)

                    print("Number of phones: ", cur.rowcount)

                    row = cur.fetchone()

                    while row is not None:
                        print(row)
                        row = cur.fetchone()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)


    if __name__ == '__main__':
        get_contacts()
        get_contacts_phone()

def get_contacts():

    sql = "SELECT * FROM contacts;"

    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql)

                print("The number of contacts: ", cur.rowcount)

                row = cur.fetchone()

                while row is not None:
                    print(row)
                    row = cur.fetchone()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def get_contacts_phone():

    sql = "SELECT id, phone FROM contacts ORDER BY id;"

    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql)

                print("Number of phones: ", cur.rowcount)

                row = cur.fetchone()

                while row is not None:
                    print(row)
                    row = cur.fetchone()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)



if __name__ == '__main__':
    get_contacts()
    get_contacts_phone()
