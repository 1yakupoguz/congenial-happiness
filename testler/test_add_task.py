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
    
def add_task(added_by, task_description, status='no'): # VERI TABANINA GOREV EKLEMEYI SAGLAYACAK SQL SORGUSUNU CALISTIRAN FONKSIYON
    try:
        print("Checking add_task() function.")
        conn, cursor = connect_db()
        cursor.execute('''
        INSERT INTO tasks (added_by, status, task_description)
        VALUES (?, ?, ?)
        ''', (added_by, status, task_description))
        conn.commit()
        print(f"{added_by} bir gorev ekledi: {task_description}")
    except sqlite3.Error as e:
        print(f"add_task() function is failed.{e}")
    finally:
        conn.close()
        print("add_task() function is worked successfully.\n")
    # try-except-finally bloğu ile database bağlantısı, SQL execute işlemi hatası gibi durumlarda hata görüntülenebilecek ve her iki koşulda da connection kesilecek.

if __name__ == "__main__":
    add_task("1yakupoguz", "son bir is")