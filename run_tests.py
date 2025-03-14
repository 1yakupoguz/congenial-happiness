from testler import test_add_task as add
from testler import test_complete_task as complete
from testler import test_delete_task as delete
from testler import test_show_task as show

conn, cursor = add.connect_db()
add.add_task("1yakupoguz", "son bir is", conn, cursor)
complete.complete_task(20,conn,cursor)
delete.delete_task(19, conn, cursor)
show.get_all_tasks(conn,cursor)
