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
    
    
def add_task(added_by, task_description, conn, cursor, status='no'): # VERI TABANINA GOREV EKLEMEYI SAGLAYACAK SQL SORGUSUNU CALISTIRAN FONKSIYON
    cursor.execute('''
    INSERT INTO tasks (added_by, status, task_description)
    VALUES (?, ?, ?)
    ''', (added_by, status, task_description))
    conn.commit()
    print(f"{added_by} bir gorev ekledi: {task_description}")

if __name__ == "__main__":
    connect_db()
    add_task("1yakupoguz", "son bir is", conn, cursor)