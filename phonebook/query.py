import psycopg2
from config import load_config


def get_contacts():

    sql = "SELECT id, firstname, lastname, phone FROM contacts ORDER BY id;"

    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql)

                # Get the number of rows returned
                print("The number of contacts: ", cur.rowcount)

                # Fetch the first row
                row = cur.fetchone()

                # Loop through and print all rows one by one
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
