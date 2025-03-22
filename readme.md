# Task Management Bot

Bu bot, ekibinizin görev takibini yapmasını sağlayan basit ve kullanışlı bir Discord botudur. Kullanıcılar kendilerine görevler ekleyebilir, tamamlayabilir, silebilir ve mevcut görevlerini görüntüleyebilirler.

## Kurulum

### 1. Gerekli Bağımlılıkları Yükleyin

```bash
pip install -r requirements.txt
```

### 2. Bot Tokenini Ekleyin

`bot.py` dosyasını açın ve `TOKEN` kısmına kendi Discord botunuzun tokenini yazın.

```python
TOKEN = "YOUR_BOT_TOKEN"
```

### 3. Botu Çalıştırın

```bash
python bot.py
```

## Kullanım

Botu çalıştırdıktan sonra, sunucunuzda aşağıdaki komutları kullanabilirsiniz:

### 📌 Görev Ekleme

```bash
!add_task <description>
```

Bu komut, kendiniz için yeni bir görev eklemenizi sağlar.

### ❌ Görev Silme

```bash
!delete_task <task_id>
```

Bu komut, belirtilen görev ID'sine sahip görevi siler.

### 📋 Görevleri Listeleme

```bash
!show_tasks
```

Bu komut, mevcut görevlerinizi listeler.

### ✅ Görev Tamamlama

```bash
!complete_task <task_id>
```

Bu komut, belirtilen görev ID'sine sahip görevi tamamlandı olarak işaretler.

## Test Dosyası Kullanımı

Botunuz aşağıdaki her işlem için veri tabanı bağlantısını otomatik olarak yapacak, başarı durumuna göre çıktı verecektir.

### 📝 Görev Ekleme

```python
add_task("kullanici_adi", "gorev_tanimi")
```

Belirtilen kullanıcı adına görev ekler.

### ✅ Görev Tamamlama

```python
complete_task(task_id)
```

Belirtilen görev ID'sini tamamlandı olarak işaretler.

### ❌ Görev Silme

```python
delete_task(task_id)
```

Belirtilen görev ID'sine sahip görevi siler.

### 📋 Görevleri Listeleme

```python
get_all_tasks()
```

Mevcut tüm görevleri listeler.

---
