from testler import test_add_task as add
from testler import test_complete_task as complete
from testler import test_delete_task as delete
from testler import test_show_task as show

def run_tests(): # bir task ekleme, bir taskı tamamlama, bir taskı silme ve tüm taskları gösterme işlemlerini yaptıktan sonra veri tabanı bağlantısını kesen fonksiyon
    add.add_task("1yakupoguz", "son bir is")
    complete.complete_task(20)
    delete.delete_task(19)
    show.get_all_tasks()

if __name__ == "__main__":
    run_tests()