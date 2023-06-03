import mysql.connector

n = int(input("Enter a number (1 Add, 2 Delete, 3 Update, 4 Found):> "))

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    database="amit",
    passwd=""
)
cur = conn.cursor()

if conn:
    if n == 1:
        cur.execute("INSERT INTO mark (name, mal, eng, math) VALUES (%s,%s,%s,%s)", (
            input("Enter name:"),
            input("Enter mal:"),
            input("Enter eng:"),
            input("Enter math:")
        ))
        conn.commit()
        print("Data saved successfully.")
    elif n == 2:
        cur.execute("DELETE FROM mark WHERE name = %s" % input("Enter name to delete: "))
        conn.commit()
        print("Deleted successfully.")
    elif n == 3:
        cur.execute("UPDATE mark SET name = ? WHERE name = ?", (input("New name: "), input("Old name: ")))
        conn.commit()
        print("Updated successfully.")
    elif n == 4:
        cur.execute("SELECT * FROM mark WHERE name = %s" % input("Enter name to search for: "))
        result = cur.fetchall()
        for row in result:
            print(row)
        print("Found successfully.")
    else:
        print()
        print("FAILED.")
