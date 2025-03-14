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
        
def delete_task(task_number,conn, cursor):
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

def delete_all_tasks(conn, cursor):
    cursor.execute('''
    SELECT added_by FROM tasks''')
    task = cursor.fetchone()

    if task:
        cursor.execute('''
        DELETE FROM tasks
        ''',)
        conn.commit()
        print(f"Tasks all is deleted.")

    else:
        print("Task is not found.")

if __name__ == "__main__" :
    connect_db()
    delete_task(15, conn, cursor)