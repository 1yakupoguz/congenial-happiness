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
        
def delete_task(task_number):
    try:
        print("Checking delete_task() function.")
        conn, cursor =connect_db()
        cursor.execute('''
        SELECT added_by FROM tasks WHERE task_id = ?
        ''', (task_number,))
        task = cursor.fetchone()
        if task:
            cursor.execute('''
            DELETE FROM tasks WHERE task_id = ?
            ''', (task_number,))
            conn.commit()
            print(f"Task {task_number} is deleted.")
        else:
            print("Task which you want to delete is not found.")

    except sqlite3.Error as e:
        print(f"delete_task() function is failed.{e}")

    finally:
        conn.close()
        print("delete_task() function is worked successfully.\n")
        # try-except-finally bloğu ile database bağlantısı, SQL execute işlemi hatası gibi durumlarda hata görüntülenebilecek ve her iki koşulda da connection kesilecek.

def delete_all_tasks():
    try:
        print("Checking delete_all_tasks() function.")
        conn, cursor = connect_db()
        cursor.execute('''
        SELECT added_by FROM tasks''')
        task = cursor.fetchone()
        if task:
            cursor.execute('''
            DELETE FROM tasks
            ''',)
            conn.commit()
            print(f"Tasks all are deleted.")
        else:
            print("Task is not found.")

    except sqlite3.Error as e:
        print(f"delete_task() function is failed.{e}")

    finally:
        conn.close()
        print("delete_task() function is worked successfully.\n")
        # try-except-finally bloğu ile database bağlantısı, SQL execute işlemi hatası gibi durumlarda hata görüntülenebilecek ve her iki koşulda da connection kesilecek.

if __name__ == "__main__" :
    delete_task(17)
    delete_all_tasks()