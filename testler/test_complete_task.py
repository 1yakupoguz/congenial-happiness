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
        
def complete_task(task_id): # GOREV DURUMUNU KULLANICI ADI UYUSURSA VE GOREV VARSA GUNCELLEYECEK FONKSIYON
    try:
        print("Checking complete_task() function.")
        conn, cursor = connect_db()
        cursor.execute('''
        SELECT added_by FROM tasks WHERE task_id = ?
        ''', (task_id,))
        task = cursor.fetchone()
        if task:
            print(f"Task {task_id} is found, is being completed.")
            cursor.execute('''
            UPDATE tasks
            SET status = ?
            WHERE task_id = ?
            ''', ("yes", task_id))
            conn.commit()
            print(f"Task {task_id} is completed.")
        else:
            print("Firstly, you must define task.")
    except sqlite3.Error as e:
        print(f"complete_task() function is failed.{e}")
    finally:
        conn.close()
        print("complete_task() function is worked successfully.\n")

    # try-except-finally bloğu ile database bağlantısı, SQL execute işlemi hatası gibi durumlarda hata görüntülenebilecek ve her iki koşulda da connection kesilecek.

if __name__ == "__main__" :
    complete_task(21)