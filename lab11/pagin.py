import psycopg2
from config import load_config


def pagin(pattern, type, page=1, limit=5):
    config = load_config()
    search_pattern = f"%{pattern}%"
    offset = (page - 1) * limit

    if type.lower() == 'firstname':
        sql = "SELECT id, firstname, lastname, phone FROM contacts WHERE firstname ILIKE %s LIMIT %s OFFSET %s;"
        count_sql = "SELECT COUNT(*) FROM contacts WHERE firstname ILIKE %s;"

    elif type.lower() == 'lastname':
        sql = "SELECT id, firstname, lastname, phone FROM contacts WHERE lastname ILIKE %s LIMIT %s OFFSET %s;"
        count_sql = "SELECT COUNT(*) FROM contacts WHERE lastname ILIKE %s;"

    elif type.lower() == 'phone':
        sql = "SELECT id, firstname, lastname, phone FROM contacts WHERE phone LIKE %s LIMIT %s OFFSET %s;"
        count_sql = "SELECT COUNT(*) FROM contacts WHERE phone LIKE %s;"

    else:
        print("wrong type")
        return

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(count_sql, (search_pattern,))
                total = cur.fetchone()[0]

                cur.execute(sql, (search_pattern, limit, offset))
                records = cur.fetchall()

                total_pages = (total + limit - 1) // limit

                print(f"\npage {page} of {total_pages} (total: {total} records)")

                if records:
                    for record in records:
                        print(record)
                else:
                    print("nothing found")

                return total_pages

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"error: {error}")