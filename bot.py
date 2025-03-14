import discord
import logging
import logging.handlers
import database as db #sqlite veri tabanını oluşturmak, veri tabanına veri göndermek, almak ve silmek için oluşturulmuştur.

# BURADA DEBUG YAPABİLMEK İÇİN BİR LOGGER OLUŞTURULUR VE BU SAYEDE KOD YAZILIRKEN YAPILAN HATALAR discord.log dosyası içerisinden ayıklanabilir.
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
logging.getLogger('discord.http').setLevel(logging.INFO)

handler = logging.handlers.RotatingFileHandler(
    filename='discord.log',
    encoding='utf-8',
    maxBytes=32 * 1024 * 1024,  # 32 MiB
    backupCount=5,  # Rotate through 5 files
)
dt_fmt = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
handler.setFormatter(formatter)
logger.addHandler(handler)

# BURADA BOTUN CHATTEKİ MESAJLARI OKUYABİLMESİ SAĞLANIR
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event # BOTUN BELİRLİ DURUMLARDA TETİKLENMESİ İÇİN KULLANILAN DECORATOR'dür
async def on_ready(): # BOT BAŞLADIĞINDA ÇALIŞIR
    print(f'We have logged in as {client.user}')

@client.event # BOTUN BELİRLİ DURUMLARDA TETİKLENMESİ İÇİN KULLANILAN DECORATOR'dür
async def on_message(message): # CHATE MESAJ YAZILDIGINDA CALISIR
    author = str(message.author) # BIRDEN FAZLA FONKSIYON ICERISINE GONDERILDIGI ICIN MESAJI YAZAN KISININ NICKNAME'I ALINIR

    if message.content.startswith('!add_task'): # KULLANICI GOREV EKLEMEK ISTERSE BU SORGU CALISIR 
        db.add_task(added_by=author, task_description= str(message.content[len('!add_task '):].strip())) # NICKNAME VE MESAJ AYIKLANARAK FONKSIYON ICERISINE GONDERILIR
        await message.channel.send(f'{message.author} task added! To list all tasks use !show_tasks')

    elif message.content.startswith('!delete_task'): # GOREV SILMEK ISTENIRSE CALISIR
        number = message.content[len('!delete_task '):].strip() 
        index_number = int(number) 
        success = db.delete_task(author, index_number) # MESAJ ICERISINDEN SILINMESI ISTENEN GOREV NUMARASI VE SILMEK ISTEYEN KISININ NICKNAME'I FONKSIYON ICERISINE GONDERILIR

        if success == 1: # FONKSIYONUN CIKTISINA GORE YOK, GOREV SILINDI VE GOREV BULUNAMADI CIKTILARI VEREN SORGU BLOGU
            await message.channel.send(f'Task {number} deleted.')
        elif success == 0:
            await message.channel.send('You are not authorized to delete this task.')
        else:
            await message.channel.send('Task not found!')

    elif message.content.startswith('!show_tasks'): # GOREVLER GORUNTULENMEK ISTENIRSE CALISIR
        tasks = db.show_tasks(author) # NICKNAME GORE HANGI GOREVLERE SAHIP OLDUGU ALINIR
        success = len(tasks)

        if success > 0: #GOREV VARSA YAZDIRMASI YOKSA GOREVE SAHIP OLMADIGINI YAZDIRACAK SORGU BLOGU
            await message.channel.send('Here is the list of tasks.')
            for task in tasks:
                await message.channel.send(f"{task[0]}: {task[3]} (Completed: {task[2]})")
        else:
            await message.channel.send('You have not any task.')

    elif message.content.startswith('!complete_task'): # GOREV TAMAMLANMAK ISTENIRSE CALISIR
        number = message.content[len('!complete_task '):].strip() 
        index_number = int(number)
        success = db.update_task_status(author, index_number) #TAMAMLANMAK ISTENEN GOREV NUMARASI VE KULLANICI ADI FONKSIYONA GONDERILIR
        
        if success == 1: #YETKI VARSA SILDIGINI YOKSA GOREVE SAHIP OLMADIGINI YAZDIRACAK SORGU BLOGU
            await message.channel.send(f'Task {number} marked as completed.')
        elif success == 0:
            await message.channel.send('You are not authorized to complete this task.')
        else:
            await message.channel.send('Task not found!')
token = 'YOUR BOT TOKEN'
client.run(token) #DISCORD BOTUNU BAŞLATIR

