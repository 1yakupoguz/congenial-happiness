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
    
        
def complete_task(task_id, conn, cursor): # GOREV DURUMUNU KULLANICI ADI UYUSURSA VE GOREV VARSA GUNCELLEYECEK FONKSIYON
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
        
if __name__ == "__main__" :
    conn, cursor = connect_db()
    complete_task(6, conn, cursor)