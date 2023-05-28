import sqlite3

def print_database_rows():
    conn = sqlite3.connect('educationNews.db')
    c = conn.cursor()

    c.execute("SELECT * FROM educationNews")
    rows = c.fetchall()

    if rows:
        for row in rows:
            print("ID:", row[0])
            print("Title:", row[1])
            print("Image URL:", row[2])
            print("Content:", row[3])
            print("Author:", row[4])
            print("Date:", row[5])
            print("Time:", row[6])
            print("Read More URL:", row[7])
            print("-" * 40)
    else:
        print("No rows found in the database.")

    conn.close()


def main():
    print_database_rows()


if __name__ == '__main__':
    main()
