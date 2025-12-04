import psycopg2
from config import load_config
from pagin import pagin

def search(pattern, type):

    config = load_config()

    if type.lower() == 'firstname':
        sql = "SELECT * FROM contacts WHERE firstname ILIKE %s ORDER BY firstname;"
        search_pattern = f"%{pattern}%"
        params = (search_pattern,)

    elif type.lower() == 'lastname':
        sql = "SELECT * FROM contacts WHERE lastname ILIKE %s ORDER BY lastname;"
        search_pattern = f"%{pattern}%"
        params = (search_pattern,)

    elif type.lower() == 'phone':
        sql = "SELECT * FROM contacts WHERE phone LIKE %s ORDER BY phone;"
        search_pattern = f"%{pattern}%"
        params = (search_pattern,)

    else:
        print("wrong type")
        return

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                cur.execute(sql, params)
                print(f"search results for {type}: '{pattern}'")
                row = cur.fetchone()

                if row is None:
                    print("no one was found")
                else:
                    while row is not None:
                        print(row)
                        row = cur.fetchone()


    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def delete(pattern, type):

    config = load_config()

    if type.lower() == 'firstname':
        sql = "DELETE FROM contacts WHERE firstname ILIKE %s;"
        params = (pattern,)

    elif type.lower() == 'lastname':
        sql = "DELETE FROM contacts WHERE lastname ILIKE %s;"
        params = (pattern,)

    elif type.lower() == 'phone':
        sql = "DELETE FROM contacts WHERE phone LIKE %s;"
        params = (pattern,)

    else:
        print("wrong type")
        return

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, params)
                deleted = cur.rowcount
                conn.commit()

                if deleted == 0:
                    print("no contacts were found")
                else:
                    print(f"deleted {deleted} contact(s)")

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def insert(firstname, lastname, phone):

    config = load_config()

    sql = """
        INSERT INTO contacts (firstname, lastname, phone)
        VALUES (%s, %s, %s)
        ON CONFLICT (firstname, lastname)
        DO UPDATE SET phone = EXCLUDED.phone;
    """

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (firstname, lastname, phone))
                conn.commit()
                print(f"contact '{firstname} {lastname}' saved/updated with phone: {phone}")

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def menu():
    print("1. search contact")
    print("2. delete contact")
    print("3. add/update contact")
    print("4. exit")


def search_menu():
    print("\nchoose search type:")
    print("1. first name")
    print("2. last name")
    print("3. phone")
    print("4. back to main menu")


def delete_menu():
    print("\nchoose delete type:")
    print("1. by first name")
    print("2. by last name")
    print("3. by phone")
    print("4. back to main menu")


if __name__ == "__main__":
    while True:
        menu()
        choice = input("select option (1-4): ").strip()

        if choice == "1":
            while True:
                search_menu()
                search_choice = input("what do you want to search? (1-4): ").strip()

                if search_choice == "1":
                    pattern = input("enter the first name you would like to search for: ").strip()
                    if pattern:
                        search(pattern, "firstname")

                elif search_choice == "2":
                    pattern = input("enter the last name you would like to search for: ").strip()
                    if pattern:
                        page = 1
                        while True:
                            total_pages = pagin(pattern, "lastname", page=page, limit=5)

                            if total_pages:
                                nav = input("\ntype n to go next | p for previous | q to quit: ").strip()
                                if nav == "n" and page < total_pages:
                                    page += 1
                                elif nav == "p" and page > 1:
                                    page -= 1
                                elif nav == "q":
                                    break
                            else:
                                break

                elif search_choice == "3":
                    pattern = input("enter phone number to search for: ").strip()
                    if pattern:
                        search(pattern, "phone")

                elif search_choice == "4":
                    break

                else:
                    print("wrong input")

        elif choice == "2":
            while True:
                delete_menu()
                delete_choice = input("\nwhat do you want to delete? (1-4): ").strip()

                if delete_choice == "1":
                    pattern = input("enter the first name to delete: ").strip()
                    if pattern:
                        delete(pattern, "firstname")

                elif delete_choice == "2":
                    pattern = input("enter the last name to delete: ").strip()
                    if pattern:
                        delete(pattern, "lastname")

                elif delete_choice == "3":
                    pattern = input("enter phone number to delete: ").strip()
                    if pattern:
                        delete(pattern, "phone")

                elif delete_choice == "4":
                    break

                else:
                    print("wrong input")

        elif choice == "3":
            firstname = input("\nenter first name: ").strip()
            lastname = input("enter last name: ").strip()
            phone = input("enter phone number: ").strip()

            if firstname and lastname and phone:
                insert(firstname, lastname, phone)
            else:
                print("fill all fields pls")



        elif choice == "4":
            exit(0)

        else:
            print("wrong input")
