import psycopg2
import csv
from config import load_config


def insert_csv(csv_filepath):
    rows_inserted = 0
    config = load_config()

    try:
        with open(csv_filepath, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)

            with psycopg2.connect(**config) as conn:
                with conn.cursor() as cur:
                    sql = """
                    INSERT INTO contacts(firstname, lastname, phone)
                    VALUES(%s, %s, %s);
                    """

                    for row in reader:
                        cur.execute(sql, tuple(row))
                        rows_inserted += 1

                    conn.commit()
                    print("Insertion complete.")

    except FileNotFoundError:
        print(f"Error: CSV file not found at path: {csv_filepath}")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Database Error: {error}")

    return rows_inserted


if __name__ == '__main__':
    inserted_count = insert_csv('phonebook_data.csv')
    print(f"Total rows successfully inserted: {inserted_count}")