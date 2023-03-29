from db import get_conn

def init_database(conn):
    with open('./data/script.sql', 'r') as f:
        script = f.read()

    # Split the script into individual statements
    statements = script.split(';')

    # Remove any empty statements
    statements = [stmt.strip() for stmt in statements if stmt.strip()]

    # Execute each statement
    for stmt in statements:
        conn.execute(stmt)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    warning = input("By executing this script you are going to delete all the data in the DB. Are you sure to continue? y/N: ")

    if warning == "y":
        init_database(get_conn())

    else:
        print("No executed")
