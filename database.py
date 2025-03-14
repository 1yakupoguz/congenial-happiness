import sqlite3

conn = sqlite3.connect('tasks.db') #VERI TABANINA BAGLANIR 
cursor = conn.cursor() #VERI TABANI UZERINDE ISLEM YAPMAYI SAGLAR

# TABLO OLUSTURULUR
cursor.execute(''' 
CREATE TABLE IF NOT EXISTS tasks(
    task_id integer PRIMARY KEY AUTOINCREMENT,
    added_by TEXT NOT NULL,
    status TEXT NOT NULL,
    task_description TEXT NOT NULL
)
    ''')

def add_task(added_by, task_description, status='no'): # VERI TABANINA GOREV EKLEMEYI SAGLAYACAK SQL SORGUSUNU CALISTIRAN FONKSIYON
    cursor.execute('''
    INSERT INTO tasks (added_by, status, task_description)
    VALUES (?, ?, ?)
    ''', (added_by, status, task_description))
    conn.commit()

def show_tasks(author): # VERI TABANINDAKI GOREVLERI KULLANICI ADINA GORE VERCEK SQL SORGUSUNU CALISTIRAN FONKSIYON
    cursor.execute('''SELECT * FROM tasks WHERE added_by = ?
    ''', (author,))
    tasks = cursor.fetchall()
    return tasks        

def update_task_status(author, task_id): # GOREV DURUMUNU KULLANICI ADI UYUSURSA VE GOREV VARSA GUNCELLEYECEK FONKSIYON
    cursor.execute('''
    SELECT added_by FROM tasks WHERE task_id = ?
    ''', (task_id,))
    task = cursor.fetchone()
    if task: # Eğer görev bulunduysa ve added_by, author ile eşleşiyorsa silme işlemi yapalım
        if task[0] == author:
            cursor.execute('''
            UPDATE tasks
            SET status = ?
            WHERE task_id = ?
            ''', ("yes", task_id))
            conn.commit()
            return 1
        else:
            return 0
    else:
        return -1

def delete_task(author, task_id):# GOREVI KULLANICI ADI ESLESIRSE SILECEK SQL SORGUSUNU CALISTIRACAK FONKSIYON
    cursor.execute('''
    SELECT added_by FROM tasks WHERE task_id = ?
    ''', (task_id,))
    task = cursor.fetchone()

    if task:
        if task[0] == author:
            cursor.execute('''
            DELETE FROM tasks WHERE task_id = ?
            ''', (task_id,))
            conn.commit()
            return 1
        else:
            return 0
    else:
        return -1