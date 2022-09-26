import telebot
import sqlite3

tk ='1215774630'
conn = sqlite3.connect('all.db', check_same_thread=False)

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS user(
   id INT PRIMARY KEY,
   user_name TEXT);
""")
conn.commit()

token = "5569898662:AAHk6_41WF9roFwq70b_-KnAmMs5gI_Ui5s"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def table(message):
    user = (message.chat.id, message.from_user.first_name)
    cur.execute("""INSERT OR IGNORE INTO user(id, user_name) VALUES(?, ?)""", user)
    conn.commit()
@bot.message_handler(commands=['getdata'])
def send(message):
    cur.execute("""SELECT user_name FROM user""")
    data = cur.fetchall()
    conn.commit()
    cur.execute("""SELECT Count(*) FROM user""")
    count = cur.fetchall()
    conn.commit()
    for sending in data:
        print(sending)
        bot.send_message(tk, sending)
    for c in count:
        bot.send_message(tk, c)

bot.infinity_polling()
