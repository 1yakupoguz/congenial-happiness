import sqlite3

def connect_db(): # database bağlantısı yapmaya yarayan fonksiyon
    try:
        conn = sqlite3.connect('tasks.db')
        cursor = conn.cursor()
        print("Database connection is initialized.")
        return conn, cursor
    except Exception as e:
        print(f"Database connection failed: {e}")
        return None, None

def get_all_tasks():
    try:
        print("Checking get_all_tasks() function.")
        conn, cursor = connect_db()
        cursor.execute('''SELECT * FROM tasks''')
        tasks = cursor.fetchall()
        success = len(tasks)
        print("Checking if there are any tasks in the database before the test starts.")
        if success > 0: 
            for task in tasks:
                print(f"{task[0]}: {task[3]} (Completed: {task[2]})")
        else:
            print("Test setup passed: No tasks found in the database before the test started.")

    except sqlite3.Error as e:
        print(f"get_all_tasks() function is failed.{e}")

    finally:
        conn.close()
        print("get_all_tasks() function is worked successfully.\n")
        # try-except-finally bloğu ile database bağlantısı, SQL execute işlemi hatası gibi durumlarda hata görüntülenebilecek ve her iki koşulda da connection kesilecek.

if __name__ == "__main__":
    get_all_tasks()