import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('personnel.db')
c = conn.cursor()

# Create a table
def create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS personnel
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  age INTEGER,
                  position TEXT)''')
    conn.commit()

# Insert a new record
def add_personnel(name, age, position):
    c.execute("INSERT INTO personnel (name, age, position) VALUES (?, ?, ?)", (name, age, position))
    conn.commit()

# View all records
def view_personnel():
    c.execute("SELECT * FROM personnel")
    records = c.fetchall()
    for record in records:
        print(record)

# Update a record
def update_personnel(personnel_id, name, age, position):
    c.execute("UPDATE personnel SET name = ?, age = ?, position = ? WHERE id = ?", (name, age, position, personnel_id))
    conn.commit()

# Delete a record
def delete_personnel(personnel_id):
    c.execute("DELETE FROM personnel WHERE id = ?", (personnel_id,))
    conn.commit()

# Simple CLI to interact with the database
def main():
    create_table()
    while True:
        print("\nPersonnel Management System")
        print("1. Add Personnel")
        print("2. View Personnel")
        print("3. Update Personnel")
        print("4. Delete Personnel")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            position = input("Enter position: ")
            add_personnel(name, age, position)

        elif choice == '2':
            view_personnel()

        elif choice == '3':
            personnel_id = int(input("Enter personnel ID to update: "))
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            position = input("Enter new position: ")
            update_personnel(personnel_id, name, age, position)

        elif choice == '4':
            personnel_id = int(input("Enter personnel ID to delete: "))
            delete_personnel(personnel_id)

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

