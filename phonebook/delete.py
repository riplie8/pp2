import psycopg2
from config import load_config


def delete_contact(value, by_field='name'):
    rows_deleted = 0
    config = load_config()

    if by_field == 'name':
        name_parts = value.split(' ', 1)
        if len(name_parts) != 2:
            print("Error: Deleting by name requires a full name (Firstname Lastname).")
            return 0

        firstname, lastname = name_parts
        # Case-insensitive match for name
        sql = 'DELETE FROM contacts WHERE firstname ILIKE %s AND lastname ILIKE %s;'
        params = (firstname, lastname)

    elif by_field == 'phone':
        sql = 'DELETE FROM contacts WHERE phone = %s;'
        params = (value,)

    else:
        print(f"Error: Deletion field '{by_field}' is not supported. Use 'name' or 'phone'.")
        return 0

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, params)
                rows_deleted = cur.rowcount
            conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return rows_deleted


if __name__ == '__main__':
    deleted_by_name = delete_contact('Axa Smith', by_field='name')
    print(f'Deleted contacts by name: {deleted_by_name}')

    deleted_by_phone = delete_contact('555-123-4567', by_field='phone')
    print(f'Deleted contacts by phone: {deleted_by_phone}')
    pass