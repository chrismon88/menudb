"""
A menu - you need to add the database and fill in the functions. 
"""
import sqlite3
from unittest import result

db = 'menu_db.sqlite'

def main():
    menu_text = """
    1. Display all records
    2. Add new record
    3. Edit existing record
    4. Delete record 
    5. Quit
    """

    while True:
        print(menu_text)
        choice = input('Enter your choice: ')
        if choice == '1':
            display_all_records()
        elif choice == '2':
            add_new_record()
        elif choice == '3':
            edit_existing_record()
        elif choice == '4':
            delete_record()
        elif choice == '5':
            break
        else:
            print('Not a valid selection, please try again')


def display_all_records():
    conn = sqlite3.connect(db)
    results = conn.execute('SELECT * FROM records')
    print('All records')
    for row in results:
        print(row)
    conn.close()


def add_new_record():
    new_name = (input('enter name: '))# new record that needs to be added to database
    new_country = input('enter counrty: ')
    new_catches = int(input('enter record of catches: '))

    with sqlite3.connect(db) as conn:
        conn.execute(f'INSERT INTO record VALUES (?, ?, ?)', (new_name, new_country, new_catches) )#insert statement to add new records question mark for parameterized queries which 
    #will not crash if "" are entered or other sqlite commands
    
    conn.close()
    #print('todo add new record. What if user wants to add a record that already exists?')


def edit_existing_record():
    updated_name = 'Christian' 
    updated_country = 'US'
    updated_catches = 89
    
    with sqlite3.connect(db) as conn:
        conn.execute('UPDATE record SET catches = ? WHERE name = ? ', (updated_catches, updated_name) )
    
    conn.close()

    #print('todo edit existing record. What if user wants to edit record that does not exist?') 


def delete_record(record_name):
    with sqlite3.connect(db) as conn: 
        conn.execute('DELETE from RECORD WHERE name = ?', (record_name, ) )
    conn.close()  


if __name__ == '__main__':
    main()