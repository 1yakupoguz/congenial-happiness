import sqlite3

def connect_db():
    global cursor,conn
    try:
        conn = sqlite3.connect('tasks.db') #VERI TABANINA BAGLANIR 
        cursor = conn.cursor() #VERI TABANI UZERINDE ISLEM YAPMAYI SAGLAR
        print("Database connection is initialized.")
        return conn, cursor
    except Exception as e:
        print("Database connection is failed.")

def get_all_tasks(conn, cursor):
    cursor.execute('''SELECT * FROM tasks''')
    tasks = cursor.fetchall()
    success = len(tasks)
    print("Checking if there are any tasks in the database before the test starts.")
    if success > 0: 
        for task in tasks:
            print(f"{task[0]}: {task[3]} (Completed: {task[2]})")
    else:
        print("Test setup passed: No tasks found in the database before the test started.")

if __name__ == "__main__":
    conn, cursor = connect_db()
    get_all_tasks(conn, cursor)