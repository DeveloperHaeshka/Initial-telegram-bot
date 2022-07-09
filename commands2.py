from imports import *

bot = Bot(token=config.token)
dp = Dispatcher(bot)

async def start_handler(message):
    msg = message
    user_id = msg.from_user.id
    user_name = msg.from_user.full_name
    ban_status = 'OFF'
    Avto = 'Велосипед'
    House = 'Яма'
    Phone = ''
    Biz = ''
    user_status = "Player"
    chat_id = message.chat.id
    result = time.localtime()

    if int(result.tm_mon) <= 9:
      tm_mon = "0"
    else:
      tm_mon = ''
    
    if int(result.tm_mday) <= 9:
      tm_mday = "0"
    else:
      tm_mday = ''
    
    if int(result.tm_hour) <= 9:
      tm_hour = "0"
    else:
      tm_hour = ''
    
    if int(result.tm_min) <= 9:
      tm_min = "0"
    else:
      tm_min = ''
    
    if int(result.tm_sec) <= 9:
      tm_sec = "0"
    else:
      tm_sec = ''
    times = f'{tm_mday}{result.tm_mday}.{tm_mon}{result.tm_mon}.{result.tm_year} | {tm_hour}{result.tm_hour}:{tm_min}{result.tm_min}:{tm_sec}{result.tm_sec}'
    times2 = str(times)

    cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",(user_id, 100000, 0, 0, user_name, 0, user_status, House, Avto, Phone, Biz, times2, ban_status))
        cursor.execute("INSERT INTO bot VALUES(?, ?);", (chat_id, 0))
        cursor.execute("INSERT INTO Бизнес VALUES(?, ?, ?);", (0, 0, user_id))
        cursor.execute("INSERT INTO farm VALUES(?, ?, ?);", (user_id, 0, 0))
        cursor.execute("INSERT INTO time_bot VALUES(?, ?, ?, ?);", (user_id, user_name, 0, 0))
        connect.commit()
    else:
        cursor.execute("INSERT INTO bot VALUES(?, ?);", (chat_id, 0))
        connect.commit()
        

    name1 = message.from_user.get_mention(as_html=True)
    await message.reply(
                         f'🧙‍♂Привет я VARS.\n\n{name1}\nТебе я дал подарок в размере 100.000.\n\nℹЧто бы начать играть введите команду "Помощь"',
                         parse_mode='html')

