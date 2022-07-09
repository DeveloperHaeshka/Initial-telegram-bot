from imports import *

bot = Bot(token=config.token)
dp = Dispatcher(bot)

async def commands_handler(message: types.Message):

    if message.forward_date != None:
        rx = ['😌','🥱','🙄','😎','😏']
        rdrx = random.choice(rx)
        return await bot.send_message(message.chat.id,f"")





#########################################  БАЛАНС   ######################################################
    if message.text.lower() in ["баланс", "б"]:
        user_id = message.from_user.id

        user_name = cursor.execute(f'SELECT user_name from users where user_id = {user_id}').fetchone()
        user_name = user_name[0]

        cripto = cursor.execute(f"SELECT cripto from users where user_id = {user_id}").fetchone()
        cripto = int(cripto[0])
        cripto2 = '{:,}'.format(cripto).replace(',', '.')

        balance = cursor.execute(f"SELECT balance from users where user_id = {user_id}").fetchone()
        balance = int(balance[0])
        balance2 = '{:,}'.format(balance).replace(',', '.')

        user_status = cursor.execute(f"SELECT user_status from users where user_id = {user_id}").fetchone()
        user_status = user_status[0]

        bank = cursor.execute(f"SELECT bank from users where user_id = {user_id}").fetchone()
        bank = int(bank[0])
        bank2 = '{:,}'.format(bank).replace(',', '.')

        if balance >= config.limit:
            balance = config.limit
            cursor.execute(f'UPDATE users SET balance = {config.limit}  WHERE user_id = {user_id}')
            connect.commit()
            balance2 = '{:,}'.format(balance).replace(',', '.')
        else:
            pass
        if bank >= config.limit:
            bank = config.limit
            cursor.execute(f'UPDATE users SET bank = {config.limit}  WHERE user_id = {user_id}')
            connect.commit()
            bank2 = '{:,}'.format(bank).replace(',', '.')
        else:
            pass
        if user_status == 'Rab':
            user_Status2 = 'РАЗРАБОТЧИК✅'

        if user_status == 'Sponsor':
            user_Status2 = 'СПОНСОР🌐'

        if user_status == 'Zam':
            user_Status2 = 'ЗАМ🚫'

        if user_status == 'Vladelec':
            user_Status2 = 'ВЛАДЕЛЕЦ🦠'

        if user_status == 'Sosdatel':
            user_Status2 = 'СОЗДАТЕЛЬ🧬'

        if user_status == 'Gl-Admin':
            user_Status2 = 'ГЛ-АДМИН🔥'

        if user_status == 'Admin':
            user_Status2 = 'АДМИН⚡️'

        if user_status == 'Ne-Admin':
            user_Status2 = 'НЕПОЛНЫЙ-АДМИН🕸'

        if user_status == 'Premium':
            user_Status2 = 'ПРЕМИУМ🦋'

        if user_status == 'Vip':
            user_Status2 = 'ВИП🐶'

        if user_status == 'Player':
            user_Status2 = 'ИГРОК💤'
        
        text = f'''
📜Имя: {user_name} 
🌡 Статус: {user_Status2}
💎Состояние: {balance2}$ 
💳Карта: {bank2}$
📀Крипто: {cripto2}шт   
        '''
        await bot.send_message(message.chat.id,text, parse_mode='html')





################################################ПРОФИЛЬ#############################################################


    if message.text.lower() in ["профиль", "п"]:
        name1 = message.from_user.get_mention(as_html=True)
        user_id = message.from_user.id

        user_name = cursor.execute(f'SELECT user_name from users where user_id = {user_id}').fetchone()
        user_name = user_name[0]

        user_status = cursor.execute(f"SELECT user_status from users where user_id = {user_id}").fetchone()

        balance = cursor.execute(f"SELECT balance from users where user_id = {user_id}").fetchone()
        balance = int(balance[0])

        bank = cursor.execute(f"SELECT bank from users where user_id = {user_id}").fetchone()
        bank = int(bank[0])

        rating = cursor.execute(f"SELECT rating from users where user_id = {user_id}").fetchone()
        rating = int(rating[0])
        rating2 = '{:,}'.format(rating).replace(',', '.')

        cripto = cursor.execute(f"SELECT cripto from users where user_id = {user_id}").fetchone()
        cripto = int(cripto[0])
        cripto2 = '{:,}'.format(cripto).replace(',', '.')

        farm = cursor.execute(f"SELECT farm from farm where user_id = {user_id}").fetchone()
        farm = int(farm[0])

        Biz = cursor.execute(f"SELECT Biz from users where user_id = {user_id}").fetchone()
        Biz = str(Biz[0])

        Phone = cursor.execute(f"SELECT Phone from users where user_id = {user_id}").fetchone()
        Phone = str(Phone[0])

        Avto = cursor.execute(f"SELECT Avto from users where user_id = {user_id}").fetchone()
        Avto = str(Avto[0])

        House = cursor.execute(f"SELECT House from users where user_id = {user_id}").fetchone()
        House = str(House[0])

        time_register = cursor.execute(f'SELECT time_register from users where user_id = {user_id}').fetchone()
        time_register = time_register[0]

        if balance >= config.limit:
            balance = config.limit
            cursor.execute(f'UPDATE users SET balance = {config.limit}  WHERE user_id = {user_id}')
            connect.commit()
        else:
            pass
        if int(balance) in range(0, 1000):
            balance3 = cursor.execute(f"SELECT balance from users where user_id = {user_id}").fetchone()
            balance3 = int(balance3[0])
        if int(balance) in range(1000, 999999):
            balance1 = balance / 1000
            balance2 = round(balance1)
            balance3 = f'{balance2} тыщ'
        if int(balance) in range(1000000, 999999999):
            balance1 = balance / 1000000
            balance2 = round(balance1)
            balance3 = f'{balance2} млн'
        if int(balance) in range(1000000000, 999999999999):
            balance1 = balance / 1000000000
            balance2 = round(balance1)
            balance3 = f'{balance2} млрд'
        if int(balance) in range(1000000000000, 999999999999999):
            balance1 = balance / 1000000000000
            balance2 = round(balance1)
            balance3 = f'{balance2} трлн'
        if int(balance) in range(1000000000000000, 999999999999999999):
            balance1 = balance / 1000000000000000
            balance2 = round(balance1)
            balance3 = f'{balance2} квдр'
        if int(balance) in range(1000000000000000000, 999999999999999999999):
            balance1 = balance / 1000000000000000000
            balance2 = round(balance1)
            balance3 = f'{balance2} квнт'
        if int(balance) >= 1000000000000000000000:
            balance1 = balance / 1000000000000000000000
            balance2 = round(balance1)
            balance3 = f'{balance2} скст'
        if bank >= config.limit:
            bank = config.limit
            cursor.execute(f'UPDATE users SET bank = {config.limit}  WHERE user_id = {user_id}')
            connect.commit()
        else:
            pass
        if int(bank) in range(0, 1000):
            bank3 = cursor.execute(f"SELECT bank from users where user_id = {user_id}").fetchone()
            bank3 = int(bank3[0])
        if int(bank) in range(1000, 999999):
            bank1 = bank / 1000
            bank2 = round(bank1)
            bank3 = f'{bank2} тыс'
        if int(bank) in range(1000000, 999999999):
            bank1 = bank / 1000000
            bank2 = round(bank1)
            bank3 = f'{bank2} млн'
        if int(bank) in range(1000000000, 999999999999):
            bank1 = bank / 1000000000
            bank2 = round(bank1)
            bank3 = f'{bank2} млрд'
        if int(bank) in range(1000000000000, 999999999999999):
            bank1 = bank / 1000000000000
            bank2 = round(bank1)
            bank3 = f'{bank2} трлн'
        if int(bank) in range(1000000000000000, 999999999999999999):
            bank1 = bank / 1000000000000000
            bank2 = round(bank1)
            bank3 = f'{bank2} квдр'
        if int(bank) in range(1000000000000000000, 999999999999999999999):
            bank1 = bank / 1000000000000000000
            bank2 = round(bank1)
            bank3 = f'{bank2} квнт'
        if int(bank) >= 1000000000000000000000:
            bank1 = bank / 1000000000000000000000
            bank2 = round(bank1)
            bank3 = f'{bank2} скст'
        if rating >= config.limit:
            rating = config.limit
            cursor.execute(f'UPDATE users SET rating = {config.limit}  WHERE user_id = {user_id}')
            connect.commit()
        else:
            pass

        if user_status[0] == 'Rab':
            user_Status2 = 'РАЗРАБОТЧИК✅'

        if user_status[0] == 'Sponsor':
            user_Status2 = 'СПОНСОР🌐'

        if user_status[0] == 'Zam':
            user_Status2 = 'ЗАМ🚫'

        if user_status[0] == 'Vladelec':
            user_Status2 = 'ВЛАДЕЛЕЦ🦠'

        if user_status[0] == 'Sosdatel':
            user_Status2 = 'СОЗДАТЕЛЬ🧬'

        if user_status[0] == 'Gl-Admin':
            user_Status2 = 'ГЛ-АДМИН🔥'

        if user_status[0] == 'Admin':
            user_Status2 = 'АДМИН⚡️'

        if user_status[0] == 'Ne-Admin':
            user_Status2 = 'НЕПОЛНЫЙ-АДМИН🕸'

        if user_status[0] == 'Premium':
            user_Status2 = 'ПРЕМИУМ🦋'

        if user_status[0] == 'Vip':
            user_Status2 = 'ВИП🐶'

        if user_status[0] == 'Player':
            user_Status2 = 'ИГРОК💤'

        if House == '':
            House = '<b> Нет ❗️ </b>'

        if Avto == '':
            Avto = '<b> Нет ❗️ </b>'

        if Phone == '':
            Phone = '<b> Нет ❗️ </b>'

        if Biz == '':
            Biz = '<b> Нет ❗️ </b>'

        if farm == 0:
            farm = '<b> Нет ❗️ </b>'

        text = f'''
{name1}, ваш профиль : 

👤 Ник: {user_name}
📌Ваш статус: {user_Status2}
 🔎 {config.full_name_bot} ID: {user_id}
 💰 Состояние: {balance3}
 💳На карте:{bank3}
 👑 Рейтинг: {rating2}
 💽 Крипто: {cripto2}шт
📦Имущество:

🏠 Дом: {House}
🚘 Машина: {Avto}
📱 Телефон:  {Phone} 
🏭 Бизнес:  {Biz} 
📡Майнинг-ферма: {farm} 

📆 Дата регистрации: {time_register}
        '''
        await bot.send_message(message.chat.id,text ,parse_mode='html')



#############################  КЛИК  #################################
    if message.text.lower() == 'клик':
        user_name = message.from_user.full_name
        user_id = message.from_user.id

        user_name = cursor.execute(f'SELECT user_name from users where user_id = {user_id}').fetchone()
        user_name = user_name[0]

        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)

        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])

        random_money = random.randint(90000000000,100000000000)
        random_money2 = '{:,}'.format(random_money)


        await bot.send_message(message.chat.id, f'{user_name}, вы получили {random_money2}$ {rwin}')
        cursor.execute(f'UPDATE users SET balance = {balance + random_money} WHERE user_id = "{user_id}"')
        connect.commit()




    ###########################################КАРТА БАНК ###########################################
    if message.text.lower() in ["карта", "банк"]:
        user_id = message.from_user.id

        user_name = cursor.execute(f'SELECT user_name from users where user_id = {user_id}').fetchone()
        user_name = user_name[0]

        bank = cursor.execute("SELECT bank from users where user_id = ?", (message.from_user.id,)).fetchone()
        bank = int(bank[0])
        bank2 = '{:,}'.format(bank)

        if bank >= 999999999999999999999999:
            bank = 999999999999999999999999
            cursor.execute(f'UPDATE users SET bank = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
            connect.commit()
            bank2 = '{:,}'.format(bank)

        banks = ['🏪', '🏦', '🏛']
        rbanks = random.choice(banks)

        text = f'''
{user_name} , Добро пожаловать в банк {config.full_name_bot} {rbanks}

👤 Владелец: {user_name}
🏪 Банковский счёт: {bank2}$

❗️ <code>Карта положить</code> <b>- положить на свою карту </b>
❗️ <code>Карта снять</code> - <b>снять с карты</b>
        '''
        await bot.send_message(message.chat.id,text , parse_mode='html')


# Карта положить
    if message.text.startswith("Карта положить") or message.text.startswith("карта положить") or message.text.startswith("банк положить") or message.text.startswith("Банк положить"):
        user_id = message.from_user.id

        user_name = cursor.execute(f'SELECT user_name from users where user_id = {user_id}').fetchone()
        user_name = user_name[0]

        su1 = message.text.split()[2]
        su2 = (su1).replace(',', '').replace('k', 'к').replace('к', '000').replace('.', '').replace('е', 'e').replace('$', '')
        su3 = float(su2)
        summ = int(su3)
        summ2 = '{:,}'.format(summ).replace(',', '.')

        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])

        bank = cursor.execute("SELECT bank from users where user_id = ?", (message.from_user.id,)).fetchone()
        bank = int(bank[0])
        bank2 = '{:,}'.format(bank).replace(',', '.')

        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)

        if summ <= 0:
            return await message.reply('❗️ Сумма не должна быть отрицательной <b>[0 и меньше]</b>', parse_mode='html')
        
        if summ > balance:
            return await message.reply('❗️ У вас <b>недостаточно средств</b>', parse_mode='html')
        
        await message.reply(f'{user_name} вы положили на карту <code>{summ2}$</code> {rwin}', parse_mode='html')
        cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = {user_id}')
        cursor.execute(f'UPDATE users SET bank = {bank + summ} WHERE user_id = {user_id}')
        connect.commit()



# Карта снять
    if message.text.startswith("Карта снять") or message.text.startswith("карта снять") or message.text.startswith("банк снять") or message.text.startswith("Банк снять"):
        user_id = message.from_user.id

        user_name = cursor.execute(f'SELECT user_name from users where user_id = {user_id}').fetchone()
        user_name = user_name[0]

        su1 = message.text.split()[2]
        su2 = (su1).replace(',', '').replace('k', 'к').replace('к', '000').replace('.', '').replace('е', 'e').replace('$', '')
        su3 = float(su2)
        summ = int(su3)
        summ2 = '{:,}'.format(summ).replace(',', '.')

        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])

        bank = cursor.execute("SELECT bank from users where user_id = ?", (message.from_user.id,)).fetchone()
        bank = int(bank[0])
        bank2 = '{:,}'.format(bank)

        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)

        if summ <= 0:
            return await message.reply('❗️ Сумма не должна быть отрицательной <b>[0 и меньше]</b>', parse_mode='html')
        
        if summ > bank:
            return await message.reply('❗️ У вас <b>недостаточно средств</b>', parse_mode='html')
        
        await message.reply(f'{user_name}, вы сняли с банка <code>{summ2}$</code> {rwin}', parse_mode='html')
        cursor.execute(f'UPDATE users SET balance = {balance + summ} WHERE user_id = {user_id}')
        cursor.execute(f'UPDATE users SET bank = {bank - summ} WHERE user_id = {user_id}')
        connect.commit()







   
  
###########################################АДМИН КОМАНДЫ###########################################

    if message.text.lower() in ['админ команды', "админ-команды", 'админ к']:
        text = f'''
<b>Неполный админ🕸</b>
  [1] | <code>Выдать</code> [Сумма] - Ограничение(не выше 2ТРЛН)

<b>Админ⚡️</b>
  [1] | <code>Выдать</code> [Сумма] - Ограничение(не выше 50ТРЛН)
  [2] | <code>Забрать</code> [Сумма] - Ограничение(не выше 50ТРЛН)

<b>Гл-Админ 🔥️</b>
  [1] | <code>Выдать</code> [Сумма] - Ограничение(не выше 300ТРЛН)
  [2] | <code>Забрать</code> [Сумма] - Ограничение(не выше 300ТРЛН)

<b>Создатель 🧬</b>
  [1] | <code>Выдать </code>[Сумма] - Ограничение(не выше 5КВРД)
  [2] | <code>Забрать</code> [Сумма] - Ограничение(не выше 5КВРД)

<b>Владелец 🦠</b>
  [1] | <code>Выдать</code> [Сумма] 
  [2] | <code>Забрать</code> [Сумма] 
  [3] | <code>Умножить</code> [Количество раз]
  [4] | <code>Обнулить б</code> - обнуляет баланс 
  [5] | <code>Выдать вип</code>
  [6] | <code>Выдать премиум</code> 

<b>Зам 🚫</b>
  [1] | <code>Выдать</code> [Сумма] 
  [2] | <code>Забрать</code> [Сумма] 
  [3] | <code>Умножить</code> [Количество раз]
  [4] | <code>Обнулить б</code> - обнуляет баланс
  [5] | <code>Обнулить профиль</code> - обнуляет профиль
  [6] | <code>Выдать вип</code>
  [7] | <code>Выдать премиум</code>
  [8] | <code>Выдать неполного админа</code>

<b>Спонсор 🌐</b>
  [1] | <code>Выдать</code> [Сумма] 
  [2] | <code>Забрать</code> [Сумма] 
  [3] | <code>Умножить</code> [Количество раз]
  [4] | <code>Обнулить б</code> - обнуляет баланс
  [5] | <code>Обнулить профиль</code> - обнуляет профиль
  [6] | <code>Выдать вип</code>
  [7] | <code>Выдать премиум</code>
  [8] | <code>Выдать неполного админа</code>
  [9] | <code>Выдать админа</code>
  [10] | <code>Выдать гл админа</code>

<b>Разработчик ✅</b>
  [1] | <code>Выдать</code> [Сумма] 
  [2] | <code>Забрать</code> [Сумма] 
  [3] | <code>Умножить</code> [Количество раз]
  [4] | <code>Обнулить б</code> - обнуляет баланс
  [5] | <code>Обнулить профиль</code> - обнуляет профиль
  [6] | <code>Выдать вип</code>
  [7] | <code>Выдать премиум</code>
  [8] | <code>Выдать неполного админа</code>
  [9] | <code>Выдать админа</code>
  [10] | <code>Выдать гл админа</code>
  [11] | <code>Выдать создателя</code>
  [12] | <code>Выдать владельца</code>
  [12] | <code>Выдать зама</code>
  [13] | <code>Выдать спонсора</code>
        '''
        await message.reply(text, parse_mode='html')






# Выдача привилегии
    if message.text.lower() == "выдать спонсора":
        if not message.reply_to_message:
            return await message.reply('❗️ Эта команда должна быть <b>ответом на сообщение</b>', parse_mode='html')
                
        reply_user_id = message.reply_to_message.from_user.id
        user_id = message.from_user.id

        reply_user_name = cursor.execute(f'SELECT user_name from users where user_id = {reply_user_id}').fetchone()
        reply_user_name = reply_user_name[0]

        user_name = cursor.execute(f'SELECT user_name from users where user_id = {user_id}').fetchone()
        user_name = user_name[0]

        user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
        user_status = user_status[0]

        if user_status == 'Rab':
            text = f'''
✅<b>Разработчик</b> <code>{user_name}</code> выдал <b>СПОНСОРА</b> игроку <code>{reply_user_name}</code>
            '''
            await bot.send_message(message.chat.id, text, parse_mode='html')
            cursor.execute(f'UPDATE users SET user_status = "Sponsor" WHERE user_id = {reply_user_id}')
            connect.commit()
        else:
            await message.reply(f'❗️Данная команда доступна от привилегии <b>РАЗРАБОТЧИК</b>', parse_mode='html')






# Выдача привилегии
    if message.text.lower() == "выдать зама":
        if not message.reply_to_message:
            return await message.reply('❗️ Эта команда должна быть <b>ответом на сообщение</b>', parse_mode='html')
                
        reply_user_id = message.reply_to_message.from_user.id
        user_id = message.from_user.id

        reply_user_name = cursor.execute(f'SELECT user_name from users where user_id = {reply_user_id}').fetchone()
        reply_user_name = reply_user_name[0]

        user_name = cursor.execute(f'SELECT user_name from users where user_id = {user_id}').fetchone()
        user_name = user_name[0]

        user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
        user_status = user_status[0]

        if user_status == 'Rab':
            text = f'''
✅<b>Разработчик</b> <code>{user_name}</code> выдал <b>ЗАМА</b> игроку <code>{reply_user_name}</code>
            '''
            await bot.send_message(message.chat.id, text, parse_mode='html')
            cursor.execute(f'UPDATE users SET user_status = "Zam" WHERE user_id = {reply_user_id}')
            connect.commit()
        else:
            await message.reply(f'❗️Данная команда доступна от привилегии <b>РАЗРАБОТЧИК</b>', parse_mode='html')








# Выдача привилегии
    if message.text.lower() in ["выдать владельца", "Выдать владельца"]:
        if not message.reply_to_message:
            return await message.reply('❗️ Эта команда должна быть <b>ответом на сообщение</b>', parse_mode='html')
                
        reply_user_id = message.reply_to_message.from_user.id
        user_id = message.from_user.id

        reply_user_name = cursor.execute(f'SELECT user_name from users where user_id = {reply_user_id}').fetchone()
        reply_user_name = reply_user_name[0]

        user_name = cursor.execute(f'SELECT user_name from users where user_id = {user_id}').fetchone()
        user_name = user_name[0]

        user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
        user_status = user_status[0]

        if user_status == 'Rab':
            text = f'''
✅<b>Разработчик</b> <code>{user_name}</code> выдал <b>ВЛАДЕЛЬЦА</b> игроку <code>{reply_user_name}</code>
            '''
            await bot.send_message(message.chat.id, text, parse_mode='html')
            cursor.execute(f'UPDATE users SET user_status = "Vladelec" WHERE user_id = {reply_user_id}')
            connect.commit()
        else:
            await message.reply(f'❗️Данная команда доступна от привилегии <b>РАЗРАБОТЧИК</b>', parse_mode='html')





# Выдача привилегии
    if message.text.lower() in ["выдать создателя", "Выдать создателя"]:
        if not message.reply_to_message:
            return await message.reply('❗️ Эта команда должна быть <b>ответом на сообщение</b>', parse_mode='html')
                
        reply_user_id = message.reply_to_message.from_user.id
        user_id = message.from_user.id

        reply_user_name = cursor.execute(f'SELECT user_name from users where user_id = {reply_user_id}').fetchone()
        reply_user_name = reply_user_name[0]

        user_name = cursor.execute(f'SELECT user_name from users where user_id = {user_id}').fetchone()
        user_name = user_name[0]

        user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
        user_status = user_status[0]

        if user_status == 'Rab':
            text = f'''
✅<b>Разработчик</b> <code>{user_name}</code> выдал <b>СОЗДАТЕЛЯ</b> игроку <code>{reply_user_name}</code>
            '''
            await bot.send_message(message.chat.id, text, parse_mode='html')
            cursor.execute(f'UPDATE users SET user_status = "Sosdatel" WHERE user_id = {reply_user_id}')
            connect.commit()
        else:
            await message.reply(f'❗️Данная команда доступна от привилегии <b>РАЗРАБОТЧИК</b>', parse_mode='html')







# Выдача привилегии
    if message.text.lower() in ["выдать гл админа",'выдать гл-админа']:
        if not message.reply_to_message:
            return await message.reply('❗️ Эта команда должна быть <b>ответом на сообщение</b>', parse_mode='html')
                
        reply_user_id = message.reply_to_message.from_user.id
        user_id = message.from_user.id

        reply_user_name = cursor.execute(f'SELECT user_name from users where user_id = {reply_user_id}').fetchone()
        reply_user_name = reply_user_name[0]

        user_name = cursor.execute(f'SELECT user_name from users where user_id = {user_id}').fetchone()
        user_name = user_name[0]

        user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
        user_status = user_status[0]

        if user_status == 'Rab':
            name_vidach = '✅<b>Разработчик</b>'
        elif user_status == 'Sponsor':
            name_vidach = '🌐<b>Спонсор</b>'
        else:
            name_vidach = None
        if user_status in ['Rab', 'Sponsor']:
            text = f'''
{name_vidach} <code>{user_name}</code> выдал <b>ГЛ-АДМИНА</b> игроку <code>{reply_user_name}</code>
            '''
            await bot.send_message(message.chat.id, text, parse_mode='html')
            cursor.execute(f'UPDATE users SET user_status = "Gl-Admin" WHERE user_id = {reply_user_id}')
            connect.commit()
        else:
            await message.reply(f'❗️Данная команда доступна от привилегии <b>СПОНСОР</b>', parse_mode='html')






# Выдача привилегии
    if message.text.lower() in ["выдать админа", "Выдать админа"]:
        if not message.reply_to_message:
            return await message.reply('❗️ Эта команда должна быть <b>ответом на сообщение</b>', parse_mode='html')
                
        reply_user_id = message.reply_to_message.from_user.id
        user_id = message.from_user.id

        reply_user_name = cursor.execute(f'SELECT user_name from users where user_id = {reply_user_id}').fetchone()
        reply_user_name = reply_user_name[0]

        user_name = cursor.execute(f'SELECT user_name from users where user_id = {user_id}').fetchone()
        user_name = user_name[0]

        user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
        user_status = user_status[0]

        if user_status == 'Rab':
            name_vidach = '✅<b>Разработчик</b>'
        elif user_status == 'Sponsor':
            name_vidach = '🌐<b>Спонсор</b>'
        else:
            name_vidach = None
        if user_status in ['Rab', 'Sponsor']:
            text = f'''
{name_vidach} <code>{user_name}</code> выдал <b>АДМИНА</b> игроку <code>{reply_user_name}</code>
            '''
            await bot.send_message(message.chat.id, text, parse_mode='html')
            cursor.execute(f'UPDATE users SET user_status = "Admin" WHERE user_id = {reply_user_id}')
            connect.commit()
        else:
            await message.reply(f'❗️Данная команда доступна от привилегии <b>СПОНСОР</b>', parse_mode='html')





# Выдача привилегии
    if message.text.lower() in ["выдать неполного админа", "Выдать неполного админа"]:
        if not message.reply_to_message:
            return await message.reply('❗️ Эта команда должна быть <b>ответом на сообщение</b>', parse_mode='html')
                
        reply_user_id = message.reply_to_message.from_user.id
        user_id = message.from_user.id

        reply_user_name = cursor.execute(f'SELECT user_name from users where user_id = {reply_user_id}').fetchone()
        reply_user_name = reply_user_name[0]

        user_name = cursor.execute(f'SELECT user_name from users where user_id = {user_id}').fetchone()
        user_name = user_name[0]

        user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
        user_status = user_status[0]

        if user_status == 'Rab':
            name_vidach = '✅<b>Разработчик</b>'
        elif user_status == 'Sponsor':
            name_vidach = '🌐<b>Спонсор</b>'
        elif user_status == 'Zam':
            name_vidach = '🚫<b>Зам</b>'
        else:
            name_vidach = None

        if user_status in ['Rab', 'Sponsor', 'Zam']:
            text = f'''
{name_vidach} <code>{user_name}</code> выдал <b>НЕПОЛНОГО АДМИНА</b> игроку <code>{reply_user_name}</code>
            '''
            await bot.send_message(message.chat.id, text, parse_mode='html')
            cursor.execute(f'UPDATE users SET user_status = "Ne-Admin" WHERE user_id = {reply_user_id}')
            connect.commit()
        else:
            await message.reply(f'❗️Данная команда доступна от привилегии <b>ЗАМ</b>', parse_mode='html')







# Выдача привилегии
    if message.text.lower() in ["выдать премиум", "Выдать премиум"]:
        if not message.reply_to_message:
            return await message.reply('❗️ Эта команда должна быть <b>ответом на сообщение</b>', parse_mode='html')
                
        reply_user_id = message.reply_to_message.from_user.id
        user_id = message.from_user.id

        reply_user_name = cursor.execute(f'SELECT user_name from users where user_id = {reply_user_id}').fetchone()
        reply_user_name = reply_user_name[0]

        user_name = cursor.execute(f'SELECT user_name from users where user_id = {user_id}').fetchone()
        user_name = user_name[0]

        user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
        user_status = user_status[0]

        if user_status == 'Rab':
            name_vidach = '✅<b>Разработчик</b>'
        elif user_status == 'Sponsor':
            name_vidach = '🌐<b>Спонсор</b>'
        elif user_status == 'Zam':
            name_vidach = '🚫<b>Зам</b>'
        elif user_status == 'Vladelec':
            name_vidach = '🦠<b>Владелец</b>'
        else:
            name_vidach = None
            
        if user_status in ['Rab', 'Sponsor', 'Zam', 'Vladelec']:
            text = f'''
{name_vidach} <code>{user_name}</code> выдал <b>ПРЕМИУМ</b> игроку <code>{reply_user_name}</code>
            '''
            await bot.send_message(message.chat.id, text, parse_mode='html')
            cursor.execute(f'UPDATE users SET user_status = "Premium" WHERE user_id = {reply_user_id}')
            connect.commit()
        else:
            await message.reply(f'❗️Данная команда доступна от привилегии <b>ВЛАДЕЛЕЦ</b>', parse_mode='html')





# Выдача привилегии
    if message.text.lower() in ["выдать вип", "Выдать вип"]:
        if not message.reply_to_message:
            return await message.reply('❗️ Эта команда должна быть <b>ответом на сообщение</b>', parse_mode='html')
                
        reply_user_id = message.reply_to_message.from_user.id
        user_id = message.from_user.id

        reply_user_name = cursor.execute(f'SELECT user_name from users where user_id = {reply_user_id}').fetchone()
        reply_user_name = reply_user_name[0]

        user_name = cursor.execute(f'SELECT user_name from users where user_id = {user_id}').fetchone()
        user_name = user_name[0]

        user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
        user_status = user_status[0]

        if user_status == 'Rab':
            name_vidach = '✅<b>Разработчик</b>'
        elif user_status == 'Sponsor':
            name_vidach = '🌐<b>Спонсор</b>'
        elif user_status == 'Zam':
            name_vidach = '🚫<b>Зам</b>'
        elif user_status == 'Vladelec':
            name_vidach = '🦠<b>Владелец</b>'
        else:
            name_vidach = None
            
        if user_status in ['Rab', 'Sponsor', 'Zam', 'Vladelec']:
            text = f'''
{name_vidach} <code>{user_name}</code> выдал <b>ВИП</b> игроку <code>{reply_user_name}</code>
            '''
            await bot.send_message(message.chat.id, text, parse_mode='html')
            cursor.execute(f'UPDATE users SET user_status = "Vip" WHERE user_id = {reply_user_id}')
            connect.commit()
        else:
            await message.reply(f'❗️Данная команда доступна от привилегии <b>ВЛАДЕЛЕЦ</b>', parse_mode='html')





# Выдача денег
    if message.text.startswith("Умножить") or message.text.startswith("умножить") or message.text.startswith("*"):
        if not message.reply_to_message:
            return await message.reply('❗️ Эта команда должна быть <b>ответом на сообщение</b>', parse_mode='html')

        user_id = message.from_user.id
        reply_user_id = message.reply_to_message.from_user.id

        user_name = cursor.execute(f'SELECT user_name from users where user_id = {user_id}').fetchone()
        user_name = user_name[0]

        reply_user_name = cursor.execute(f'SELECT user_name from users where user_id = {reply_user_id}').fetchone()
        reply_user_name = reply_user_name[0]

        reply_balance = cursor.execute(f"SELECT balance from users where user_id = {reply_user_id}").fetchone()
        reply_balance = reply_balance[0]

        user_status = cursor.execute(f"SELECT user_status from users where user_id = {user_id}").fetchone()
        user_status = user_status[0]

        su1 = message.text.split()[1]
        su2 = (su1).replace(',', '').replace('.', '').replace('к', 'k').replace('k', '000').replace('е', 'e').replace('$', '')
        su3 = float(su2)
        summ = int(su3)
        summ2 = '{:,}'.format(summ).replace(',', '.')
        summ3 = int(reply_balance * summ)
        summ4 = '{:,}'.format(summ3).replace(',', '.')

        if user_status == 'Rab':
            name_vidach = '✅ Разработчик'
        elif user_status == 'Sponsor':
            name_vidach = '🌐 Спонсор'
        elif user_status == 'Zam':
            name_vidach = '🚫 Зам'
        elif user_status == 'Vladelec':
            name_vidach = '🦠Владелец'
        else:
            name_vidach = None

        if user_status in ['Rab', 'Sponsor', 'Zam', 'Vladelec']:
            text = f'''
✖️ Вы <b>умножили</b> баланс <code>{reply_user_name}</code> в <code>{summ2}</code> <b>раз(a)</b>
❕ Теперь <b>баланс</b> <code>{reply_user_name}</code> равен: <code>{summ4}$</code>
            '''
            if summ3 >= config.limit:
                return await message.reply('❗️ Нельзя выдавать <b>лимит и больше</b>', parse_mode='html')
            
            await message.reply(text, parse_mode='html')
            cursor.execute(f'UPDATE users SET balance = {summ3} WHERE user_id = {reply_user_id}')
            connect.commit()
        else:
            return await message.reply('❗️ Данная команда доступна от привилегии <b>ВЛАДЕЛЕЦ</b>', parse_mode='html')









# Выдача денег
    if message.text.startswith("выдать") or message.text.startswith("Выдать") or message.text.startswith("+"):
        if not message.reply_to_message:
            return await message.reply('❗️ Эта команда должна быть <b>ответом на сообщение</b>', parse_mode='html')

        user_id = message.from_user.id
        reply_user_id = message.reply_to_message.from_user.id

        user_name = cursor.execute(f'SELECT user_name from users where user_id = {user_id}').fetchone()
        user_name = user_name[0]

        reply_user_name = cursor.execute(f'SELECT user_name from users where user_id = {reply_user_id}').fetchone()
        reply_user_name = reply_user_name[0]

        reply_balance = cursor.execute(f"SELECT balance from users where user_id = {reply_user_id}").fetchone()
        reply_balance = reply_balance[0]

        user_status = cursor.execute(f"SELECT user_status from users where user_id = {user_id}").fetchone()
        user_status = user_status[0]

        su1 = message.text.split()[1]
        su2 = (su1).replace(',', '').replace('.', '').replace('к', 'k').replace('k', '000').replace('е', 'e').replace('$', '')
        su3 = float(su2)
        summ = int(su3)
        summ2 = '{:,}'.format(summ).replace(',', '.')
        summ3 = int(reply_balance + summ)
        summ4 = '{:,}'.format(summ3).replace(',', '.')

        if user_status == 'Rab':
            limit_vidach = config.limit
            name_vidach = '✅ Разработчик'
        elif user_status == 'Sponsor':
            limit_vidach = config.limit
            name_vidach = '🌐 Спонсор'
        elif user_status == 'Zam':
            limit_vidach = config.limit
            name_vidach = '🚫 Зам'
        elif user_status == 'Vladelec':
            limit_vidach = config.limit
            name_vidach = '🦠 Владелец'
        elif user_status == 'Sosdatel':
            limit_vidach = config.limit_sosdatel
            name_vidach = '🧬 Создатель'
        elif user_status == 'Gl-Admin':
            limit_vidach = config.limit_gl_admin
            name_vidach = '🔥️ Гл-Админ'
        elif user_status == 'Admin':
            limit_vidach = config.limit_admin
            name_vidach = '⚡️ Админ'
        elif user_status == 'Ne-Admin':
            limit_vidach = config.limit_ne_admin
            name_vidach = '🕸Неполный админ'
        else:
            name_vidach = None

        if user_status in ['Rab', 'Sponsor', 'Zam', 'Vladelec', 'Sosdatel', 'Gl-Admin', 'Admin', 'Ne-Admin']:
            
            if summ3 >= limit_vidach:
                return await message.reply('Нельзя выдавать <b>лимит и больше</b>', parse_mode='html')
            
            text = f'''
➕ Вы <b>выдали</b> на баланс <code>{reply_user_name}</code> в <b>размере</b> <code>{summ2}$</code>
❕ Теперь <b>баланс</b> <code>{reply_user_name}</code> равен: <code>{summ4}$</code>
            '''
            await message.reply(text, parse_mode='html')
            cursor.execute(f'UPDATE users SET balance = {summ3} WHERE user_id = {reply_user_id}')
            connect.commit()
        else:
            return await message.reply('❗️ Данная команда доступна от привилегии <b>НЕПОЛНОГО АДМИНА</b>', parse_mode='html')








# Выдача денег
    if message.text.startswith("забрать") or message.text.startswith("Забрать") or message.text.startswith("-"):
        if not message.reply_to_message:
            return await message.reply('❗️ Эта команда должна быть <b>ответом на сообщение</b>', parse_mode='html')

        user_id = message.from_user.id
        reply_user_id = message.reply_to_message.from_user.id

        user_name = cursor.execute(f'SELECT user_name from users where user_id = {user_id}').fetchone()
        user_name = user_name[0]

        reply_user_name = cursor.execute(f'SELECT user_name from users where user_id = {reply_user_id}').fetchone()
        reply_user_name = reply_user_name[0]

        reply_balance = cursor.execute(f"SELECT balance from users where user_id = {reply_user_id}").fetchone()
        reply_balance = reply_balance[0]

        user_status = cursor.execute(f"SELECT user_status from users where user_id = {user_id}").fetchone()
        user_status = user_status[0]

        su1 = message.text.split()[1]
        su2 = (su1).replace(',', '').replace('.', '').replace('к', 'k').replace('k', '000').replace('е', 'e').replace('$', '')
        su3 = float(su2)
        summ = int(su3)
        summ2 = '{:,}'.format(summ).replace(',', '.')
        summ3 = int(reply_balance - summ)
        summ4 = '{:,}'.format(summ3).replace(',', '.')

        if user_status == 'Rab':
            limit_vidach = config.limit
            name_vidach = '✅ Разработчик'
        elif user_status == 'Sponsor':
            limit_vidach = config.limit
            name_vidach = '🌐 Спонсор'
        elif user_status == 'Zam':
            limit_vidach = config.limit
            name_vidach = '🚫 Зам'
        elif user_status == 'Vladelec':
            limit_vidach = config.limit
            name_vidach = '🦠 Владелец'
        elif user_status == 'Sosdatel':
            limit_vidach = config.limit_sosdatel
            name_vidach = '🧬 Создатель'
        elif user_status == 'Gl-Admin':
            limit_vidach = config.limit_gl_admin
            name_vidach = '🔥️ Гл-Админ'
        elif user_status == 'Admin':
            limit_vidach = config.limit_admin
            name_vidach = '⚡️ Админ'
        else:
            limit_vadach = None
            name_vidach = None

        if user_status in ['Rab','Sponsor', 'Zam', 'Vladelec', 'Sosdatel', 'Gl-Admin', 'Admin']:
            
            if summ3 <= 0:
                return await message.reply('❗️ Нельзя забирать отрицательное число <b>[0 и меньше]</b>', parse_mode='html')
            elif summ3 >= limit_vidach:
                return await message.reply('Нельзя выдавать <b>лимит и больше</b>', parse_mode='html')

            text = f'''
➖ Вы <b>забрали</b> с баланса <code>{reply_user_name}</code> в <b>размере</b> <code>{summ2}$</code>
❕ Теперь <b>баланс</b> <code>{reply_user_name}</code> равен: <code>{summ4}$</code>
            '''        

            await message.reply(text, parse_mode='html')
            cursor.execute(f'UPDATE users SET balance = {summ3} WHERE user_id = {reply_user_id}')
            connect.commit()
        else:
            return await message.reply('❗️ Данная команда доступна от привилегии <b>АДМИНА</b>', parse_mode='html')










# Обнуление
    if message.text.lower() in ["обнулить профиль", "обнулить п"]:
        if not message.reply_to_message:
            return await message.reply('❗️ Эта команда должна быть <b>ответом на сообщение</b>', parse_mode='html')

        user_id = message.from_user.id
        reply_user_id = message.reply_to_message.from_user.id

        user_name = cursor.execute(f'SELECT user_name from users where user_id = {user_id}').fetchone()
        user_name = user_name[0]

        reply_user_name = cursor.execute(f'SELECT user_name from users where user_id = {reply_user_id}').fetchone()
        reply_user_name = reply_user_name[0]

        user_status = cursor.execute(f"SELECT user_status from users where user_id = {user_id}").fetchone()
        user_status = user_status[0]

        if user_status == 'Rab':
            name_vidach = '✅ <b>Разработчик</b>'
        elif user_status == 'Sponsor':
            name_vidach = '🌐 <b>Спонсор</b>'
        elif user_status == 'Zam':
            name_vidach = '🚫 <b>Зам</b>'
        else:
            name_vidach = None

        if user_status in ['Rab', 'Sponsor', 'Zam']:
            text = f'''
{name_vidach} <code>{user_name}</code> обнулил <b>профиль</b> <code>{reply_user_name}</code>
            '''

            await bot.send_message(message.chat.id, text, parse_mode='html')
            cursor.execute(f'UPDATE users SET balance = {0} WHERE user_id = "{reply_user_id}"')
            cursor.execute(f'UPDATE users SET bank = {0} WHERE user_id = "{reply_user_id}"')
            cursor.execute(f'UPDATE users SET cripto = {0} WHERE user_id = "{reply_user_id}"')
            cursor.execute(f'UPDATE users SET rating = {0} WHERE user_id = "{reply_user_id}"')
            cursor.execute(f'UPDATE users SET Avto = "" WHERE user_id = "{reply_user_id}"')
            cursor.execute(f'UPDATE users SET House = "" WHERE user_id = "{reply_user_id}"')
            cursor.execute(f'UPDATE users SET Phone = "" WHERE user_id = "{reply_user_id}"')
            cursor.execute(f'UPDATE users SET Biz = "" WHERE user_id = "{reply_user_id}"')
            cursor.execute(f'UPDATE users SET Farm = "" WHERE user_id = "{reply_user_id}"')
            cursor.execute(f'UPDATE Ферма SET Баланс = {0} WHERE user_id = "{reply_user_id}"')
            cursor.execute(f'UPDATE Бизнес SET Баланс = {0} WHERE user_id = "{reply_user_id}"')
            cursor.execute(f'UPDATE Бизнес SET Рабочие = {0} WHERE user_id = "{reply_user_id}"')
            cursor.execute(f'UPDATE mine SET iron = {0} WHERE user_id = "{reply_user_id}"')
            cursor.execute(f'UPDATE mine SET gold = {0} WHERE user_id = "{reply_user_id}"')
            cursor.execute(f'UPDATE mine SET diamonds = {0} WHERE user_id = "{reply_user_id}"')
            cursor.execute(f'UPDATE mine SET amethysts = {0} WHERE user_id = "{reply_user_id}"')
            cursor.execute(f'UPDATE mine SET aquamarine = {0} WHERE user_id = "{reply_user_id}"')
            cursor.execute(f'UPDATE mine SET emeralds = {0} WHERE user_id = "{reply_user_id}"')
            cursor.execute(f'UPDATE mine SET matter = {0} WHERE user_id = "{reply_user_id}"')
            cursor.execute(f'UPDATE mine SET plasma = {0} WHERE user_id = "{reply_user_id}"')
            connect.commit()
        
        else:
            return await message.reply('❗️ Данная команда доступна от привилегии <b>ЗАМА</b>', parse_mode='html')










# Обнуление
    if message.text.lower() in ["обнулить б"]:
        if not message.reply_to_message:
            return await message.reply('❗️ Эта команда должна быть <b>ответом на сообщение</b>', parse_mode='html')

        user_id = message.from_user.id
        reply_user_id = message.reply_to_message.from_user.id

        user_name = cursor.execute(f'SELECT user_name from users where user_id = {user_id}').fetchone()
        user_name = user_name[0]

        reply_user_name = cursor.execute(f'SELECT user_name from users where user_id = {reply_user_id}').fetchone()
        reply_user_name = reply_user_name[0]

        user_status = cursor.execute(f"SELECT user_status from users where user_id = {user_id}").fetchone()
        user_status = user_status[0]

        if user_status == 'Rab':
            name_vidach = '✅ Разработчик'
        elif user_status == 'Sponsor':
            name_vidach = '🌐 Спонсор'
        elif user_status == 'Zam':
            name_vidach = '🚫 Зам'
        elif user_status == 'Vladelec':
            name_vidach = '🦠 Владелец'
        else:
            name_vidach = None

        if user_status in ['Rab', 'Sponsor', 'Zam', 'Vladelec']:
            text = f'''
<b>{name_vidach}</b> <code>{user_name}</code> обнулил <b>баланс</b> <code>{reply_user_name}</code>
            '''

            await bot.send_message(message.chat.id , text , parse_mode='html')
            cursor.execute(f'UPDATE users SET balance = {0} WHERE user_id = "{reply_user_id}"')
            cursor.execute(f'UPDATE users SET bank = {0} WHERE user_id = "{reply_user_id}"')
            cursor.execute(f'UPDATE users SET cripto = {0} WHERE user_id = "{reply_user_id}"')
            connect.commit()
        else:
            return await message.reply('❗️ Данная команда доступна от привилегии <b>ВЛАДЕЛЬЦА</b>', parse_mode='html')








# Бан\ разбан
    if message.text.lower() in ["забанить", "бан"]:
        if not message.reply_to_message:
            return await message.reply('❗️ Эта команда должна быть <b>ответом на сообщение</b>', parse_mode='html')

        user_id = message.from_user.id
        reply_user_id = message.reply_to_message.from_user.id

        user_name = cursor.execute(f'SELECT user_name from users where user_id = {user_id}').fetchone()
        user_name = user_name[0]

        reply_user_name = cursor.execute(f'SELECT user_name from users where user_id = {reply_user_id}').fetchone()
        reply_user_name = reply_user_name[0]

        user_status = cursor.execute(f"SELECT user_status from users where user_id = {user_id}").fetchone()
        user_status = user_status[0]

        if user_status == 'Rab':
            text = f'''
✅ <b>Разработчик</b> <code>{user_name}</code> выдал <b>BAN</b> игроку <code>{reply_user_name}</code>
            '''

            text2 = f'''
🆘 Ваш аккаунт был <b>заблокирован</b>.
❗️ для его <b>разблокировки</b>, обратитесь к владельцу бота <b>[{config.owner}]</b>
            '''

            await bot.send_message(reply_user_id, text2, parse_mode='html')
            await bot.send_message(message.chat.id , text, parse_mode='html')
            cursor.execute(f'UPDATE users SET ban_status = "ON" WHERE user_id = {user_id}')
            connect.commit()
        else:
            return await message.reply('❗️ Данная команда доступна от привилегии <b>РАЗРАБОТЧИК</b>', parse_mode='html')






# Бан\ разбан
    if message.text.lower() in ["разбанить", "разбан"]:
        if not message.reply_to_message:
            return await message.reply('❗️ Эта команда должна быть <b>ответом на сообщение</b>', parse_mode='html')

        user_id = message.from_user.id
        reply_user_id = message.reply_to_message.from_user.id

        user_name = cursor.execute(f'SELECT user_name from users where user_id = {user_id}').fetchone()
        user_name = user_name[0]

        reply_user_name = cursor.execute(f'SELECT user_name from users where user_id = {reply_user_id}').fetchone()
        reply_user_name = reply_user_name[0]

        user_status = cursor.execute(f"SELECT user_status from users where user_id = {user_id}").fetchone()
        user_status = user_status[0]

        if user_status == 'Rab':
            text = f'''
✅ <b>Разработчик</b> <code>{user_name}</code> выдал <b>UNBAN</b> игроку <code>{reply_user_name}</code>
            '''

            text2 = f'''
✅ Ваш аккаунт был <b>разблокирован</b>.
            '''

            await bot.send_message(reply_user_id, text2, parse_mode='html')
            await bot.send_message(message.chat.id , text, parse_mode='html')
            cursor.execute(f'UPDATE users SET ban_status = "OFF" WHERE user_id = {user_id}')
            connect.commit()
        else:
            return await message.reply('❗️ Данная команда доступна от привилегии <b>РАЗРАБОТЧИК</b>', parse_mode='html')













    ###########################################МАЙНИНГ-ФЕРМА####################################



# покупка фермы
    if message.text.startswith('купить ферму') or message.text.startswith('Купить ферму') or message.text.startswith('Ферму купить') or message.text.startswith('ферму купить'):
        user_id = message.from_user.id

        user_name = cursor.execute(f'SELECT user_name from users where user_id = {user_id}').fetchone()
        user_name = user_name[0]

        cripto = cursor.execute(f'SELECT cripto from users where user_id = {user_id}').fetchone()
        cripto = int(cripto[0])

        farm = cursor.execute(f'SELECT farm from users where user_id = {user_id}').fetchone()
        farm = int(farm[0])

        summ = int(message.text.split()[2])

        if summ == 1:
            summ_farm = 500000000

            if cripto < summ_farm:
                return await message.reply('❗️ У вас не хватает <b>крипто</b>', parse_mode='html')
            
            if farm > 0 and farm < 0:
                return await message.reply('❗️ У вас уже есть <b>майнинг ферма</b>', parse_mode='html')
            
            await message.reply('')
            
            


    if message.text.startswith("Ферма снять"):
        msg = message
        user_id = msg.from_user.id
        user_name = message.from_user.get_mention(as_html=True)
        summ = int(msg.text.split()[2])
        chat_id = message.chat.id
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        cripto = cursor.execute("SELECT cripto from users where user_id = ?", (message.from_user.id,)).fetchone()
        cripto = int(cripto[0])
        Баланс = cursor.execute("SELECT Баланс from Ферма where user_id = ?", (message.from_user.id,)).fetchone()
        Баланс = int(Баланс[0])
        Баланс2 = '{:,}'.format(summ)
        c = summ
        c2 = '{:,}'.format(c)
        if summ > 0:
            if int(Баланс) >= int(c):
                await bot.send_message(message.chat.id,
                                       f'{user_name},вы сняли с Баланса майнинг фермы {c2}💾 на свой Крипто-Баланс{rwin}',
                                       parse_mode='html')
                cursor.execute(f'UPDATE users SET cripto = {cripto + c} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE Ферма SET Баланс = {Баланс - c} WHERE user_id = "{user_id}"')
                connect.commit()
            if int(Баланс) < int(c):
                await bot.send_message(message.chat.id, f'{user_name}, недостаточно средств! {rloser}',
                                       parse_mode='html')
            if summ <= 0:
                await bot.send_message(message.chat.id, f'{user_name}, нельзя снять отрицательное число! {rloser}',
                                       parse_mode='html')

    if message.text.lower() in ['Запустить ферму', "запустить ферму"]:
        msg = message
        user_id = msg.from_user.id
        chat_id = message.chat.id

        win = ['🙂', '😋', '😄', '😃']
        loser = ['😔', '😕', '😣', '😞', '😢']
        rwin = random.choice(win)
        rloser = random.choice(loser)

        msg = message
        name1 = message.from_user.get_mention(as_html=True)
        name = msg.from_user.last_name
        Баланс = cursor.execute("SELECT Баланс from Ферма where user_id = ?", (message.from_user.id,)).fetchone()
        Баланс = round(int(Баланс[0]))
        Farm = cursor.execute("SELECT Farm from users where user_id = ?", (message.from_user.id,)).fetchone()
        Farm = str(Farm[0])
        period = 5
        get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
        last_stavka = f"{int(get[0])}"
        stavkatime = time.time() - float(last_stavka)
        if stavkatime > period:
            if Farm == 'Calisto' :
                await bot.send_message(chat_id,
                                       f'{name1}, Майнинг-ферма была остановлена  📡️\n📡️ | Ферма: Calisto\n💰 | Заработано: 1.000.000.000💾',
                                       parse_mode='html')
                cursor.execute(f'UPDATE Ферма SET Баланс = {Баланс + 1000000000} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                connect.commit()
                return

            if Farm == 'Saturn' :
                await bot.send_message(chat_id,
                                       f'{name1}, Майнинг-ферма была остановлена  📡️\n🛢 | Ферма: Saturn\n💰 | Заработано: 250.000.000💾',
                                       parse_mode='html')
                cursor.execute(f'UPDATE Ферма SET Баланс = {Баланс + 250000000} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                connect.commit()
                return

            if Farm == 'TI-Miner' :
                await bot.send_message(chat_id,
                                       f'{name1}, Майнинг-ферма была остановлена  📡️\n🔋 | Ферма: TI-Miner\n💰 | Заработано: 10.000.000💾',
                                       parse_mode='html')
                cursor.execute(f'UPDATE Ферма SET Баланс = {Баланс + 10000000} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                connect.commit()
                return
        else:
            await bot.send_message(chat_id,
                                   f'{name1}, Запускать ферму можно только раз в 3h {rloser}',
                                   parse_mode='html')


    if message.text.lower() in ['Моя ферма', "моя ферма"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        Farm = cursor.execute("SELECT Farm from users where user_id = ?", (message.from_user.id,)).fetchone()
        Баланс = cursor.execute("SELECT Баланс from Ферма where user_id = ?", (message.from_user.id,)).fetchone()
        Баланс = int(Баланс[0])
        Баланс2 = '{:,}'.format(Баланс)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)

        if Farm[0] == 'Calisto':
            await bot.send_message(message.chat.id,
                                   f'📡 | Майнинг-Ферма: Calisto\n👤 | Владелец: {user_name}\n💰 | Баланс Фермы: {Баланс2}💾\n\nℹ️Что бы запустить майнинг-ферму введите команду\nℹ️Запустить ферму\n\n🆘Что бы снять с баланса майнинг-фермы введите команду\n🆘Ферма снять [Сумма]',
                                   parse_mode='html')

        if Farm[0] == 'Saturn':
            await bot.send_message(message.chat.id,
                                   f'🛢 | Майнинг-Ферма: Saturn\n👤 | Владелец: {user_name}\n💰 | Баланс Фермы: {Баланс2}💾\n\nℹ️Что бы запустить майнинг-ферму введите команду\nℹ️Запустить ферму\n\n🆘Что бы снять с баланса майнинг-фермы введите команду\n🆘Ферма снять [Сумма]',
                                   parse_mode='html')

        if Farm[0] == 'TI-Miner':
            await bot.send_message(message.chat.id,
                                   f'🔋️ | Майнинг-Ферма: TI-Miner\n👤 | Владелец: {user_name}\n💰 | Баланс Фермы: {Баланс2}💾\n\nℹ️Что бы запустить майнинг-ферму введите команду\nℹ️Запустить ферму\n\n🆘Что бы снять с баланса майнинг-фермы введите команду\n🆘Ферма снять [Сумма]',
                                   parse_mode='html')

        if Farm[0] == '':
            await bot.send_message(message.chat.id,f'{user_name}, Извините . Но у вас нету майнинг-фермы{rloser}\nℹ️Что бы посмотреть список Майнинг-Ферм для покупки введите команду\nℹ️Фермы',parse_mode='html')


    if message.text.lower() in ['Фермы', "фермы"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        await bot.send_message(message.chat.id,f'{user_name}, вот список Майнинг-Ферм📡\n🔋 | [1] TI-Miner - 500.000.000💾\n🛢 | [2] Saturn - 4.333.333.333💾\n📡 | [3] Calisto - 100,000,000,000💾\n\nℹ️Что бы купить майнинг-ферму введите команду\nℹ️Купить ферму [Номер фермы]',parse_mode='html')
    if message.text.lower() in ['Ферма', "ферма"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        await bot.send_message(message.chat.id,f'{user_name}, Вот все команды связаные с Майнинг-Фермой📡\n📡 | Моя ферма - показует всю информацию про вашу майнинг-ферму \n🔋 | Фермы - показывает список майнинг-ферм в продаже',parse_mode='html')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    ###########################################БИЗНЕСЫ##########################################
    if message.text.startswith("Бизнес снять"):
        msg = message
        user_id = msg.from_user.id
        user_name = message.from_user.get_mention(as_html=True)
        summ = int(msg.text.split()[2])
        chat_id = message.chat.id
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        Баланс = cursor.execute("SELECT Баланс from Бизнес where user_id = ?", (message.from_user.id,)).fetchone()
        Баланс = int(Баланс[0])
        Баланс2 = '{:,}'.format(summ)
        c = summ
        c2 = '{:,}'.format(c)
        if summ > 0:
            if int(Баланс) >= int(summ):
                await bot.send_message(message.chat.id,
                                       f'{user_name},вы сняли с Баланса бизнеса {c2}$ на свой баланс{rwin}',
                                       parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + c} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE Бизнес SET Баланс = {Баланс - summ} WHERE user_id = "{user_id}"')
                connect.commit()
            if int(Баланс) < int(summ):
                await bot.send_message(message.chat.id, f'{user_name}, недостаточно средств! {rloser}',
                                       parse_mode='html')
        if summ <= 0:
            await bot.send_message(message.chat.id, f'{user_name}, нельзя снять отрицательное число! {rloser}',
                                   parse_mode='html')
    if message.text.lower() in ['Бизнес начать', "бизнес начать"]:
        msg = message
        user_id = msg.from_user.id
        chat_id = message.chat.id

        win = ['🙂', '😋', '😄', '😃']
        loser = ['😔', '😕', '😣', '😞', '😢']
        rwin = random.choice(win)
        rloser = random.choice(loser)

        msg = message
        name1 = message.from_user.get_mention(as_html=True)
        name = msg.from_user.last_name
        Баланс = cursor.execute("SELECT Баланс from Бизнес where user_id = ?", (message.from_user.id,)).fetchone()
        Баланс = round(int(Баланс[0]))

        Biz = cursor.execute("SELECT Biz from users where user_id = ?", (message.from_user.id,)).fetchone()
        Biz = str(Biz[0])
        period = 10800
        get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
        last_stavka = f"{int(get[0])}"
        stavkatime = time.time() - float(last_stavka)
        if stavkatime > period:
            if Biz == '' :
                await bot.send_message(chat_id,
                                       f'{name1}, извините. У вас нету бизнеса{rloser}',
                                       parse_mode='html')
                return
            if Biz == 'Забигаловка' :
                await bot.send_message(chat_id,
                                       f'{name1}, Рабочий день закончился☁️\n🫔 | Бизнес: Забигаловка\n💰 | Заработано: 1.000.000.000$',
                                       parse_mode='html')
                cursor.execute(f'UPDATE Бизнес SET Баланс = {Баланс + 1000000000} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                connect.commit()


            if Biz == 'Банк' :
                await bot.send_message(chat_id,
                                       f'{name1}, Рабочий день закончился☁️\n🏦 | Бизнес: Банк\n💰 | Заработано: 5.000.000.000.000.000$',
                                       parse_mode='html')
                cursor.execute(f'UPDATE Бизнес SET Баланс = {Баланс + 5000000000000000} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                connect.commit()


            if Biz == 'Завод' :
                await bot.send_message(chat_id,
                                       f'{name1}, Рабочий день закончился☁️\n🏭 | Бизнес: Завод\n💰 | Заработано: 999.000.000.000.000$',
                                       parse_mode='html')
                cursor.execute(f'UPDATE Бизнес SET Баланс = {Баланс + 999000000000000} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                connect.commit()


            if Biz == 'Стоительная компания' :
                await bot.send_message(chat_id,
                                       f'{name1}, Рабочий день закончился☁️\n🏗 | Бизнес: Стоительная компания\n💰 | Заработано: 235.000.000.000.000$',
                                       parse_mode='html')
                cursor.execute(f'UPDATE Бизнес SET Баланс = {Баланс + 235000000000000} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                connect.commit()


            if Biz == 'Парк Аткракционов' :
                await bot.send_message(chat_id,
                                       f'{name1}, Рабочий день закончился☁️\n🎠 | Бизнес: Парк Аткракционов\n💰 | Заработано: 75.000.000.000.000$',
                                       parse_mode='html')
                cursor.execute(f'UPDATE Бизнес SET Баланс = {Баланс + 75000000000000} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                connect.commit()


            if Biz == 'Магазин 24/7' :
                await bot.send_message(chat_id,
                                       f'{name1}, Рабочий день закончился☁️\n🏬️ | Бизнес: Магазин 24/7\n💰 | Заработано: 5.000.000.000.000$',
                                       parse_mode='html')
                cursor.execute(f'UPDATE Бизнес SET Баланс = {Баланс + 5000000000000} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                connect.commit()


            if Biz == 'Кафе' :
                await bot.send_message(chat_id,
                                       f'{name1}, Рабочий день закончился☁️\n☕️ | Бизнес: Кафе\n💰 | Заработано: 1.000.000.000.000$',
                                       parse_mode='html')
                cursor.execute(f'UPDATE Бизнес SET Баланс = {Баланс + 1000000000000} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                connect.commit()


        else:
            await bot.send_message(chat_id,
                                   f'{name1}, извини. Но можно будет начать рабочий день только через 3h. {rloser}',
                                   parse_mode='html')



    if message.text.lower() in ["Купить бизнес 7", "купить бизнес 7"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        user_id = msg.from_user.id
        rwin = random.choice(win)
        Biz = cursor.execute("SELECT Biz from users where user_id = ?", (message.from_user.id,)).fetchone()
        Biz = str(Biz[0])
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        if int(balance) >= 50000000000000000:
            await bot.send_message(message.chat.id,
                                   f'{user_name}, вы успешно купили бизнес Банк 🏦 за 50.000.000.000.000.000$ {rwin} ',
                                   parse_mode='html')
            cursor.execute(f'UPDATE users SET Biz = "Банк" WHERE user_id = "{user_id}"')
            cursor.execute(f'UPDATE users SET balance = {balance - 50000000000000000} WHERE user_id = "{user_id}"')
            connect.commit()
        if int(balance) < 50000000000000000:
            await bot.send_message(message.chat.id, f'{user_name}, у вас не достаточно средств! {rloser} ',
                                   parse_mode='html')
    if message.text.lower() in ["Купить бизнес 6", "купить бизнес 6"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        user_id = msg.from_user.id
        rwin = random.choice(win)
        Biz = cursor.execute("SELECT Biz from users where user_id = ?", (message.from_user.id,)).fetchone()
        Biz = str(Biz[0])
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        if int(balance) >= 15000000000000000:
            await bot.send_message(message.chat.id,
                                   f'{user_name}, вы успешно купили бизнес Завод 🏭 за 15.000.000.000.000.000$ {rwin} ',
                                   parse_mode='html')
            cursor.execute(f'UPDATE users SET Biz = "Завод" WHERE user_id = "{user_id}"')
            cursor.execute(f'UPDATE users SET balance = {balance - 15000000000000000} WHERE user_id = "{user_id}"')
            connect.commit()
        if int(balance) < 15000000000000000:
            await bot.send_message(message.chat.id, f'{user_name}, у вас не достаточно средств! {rloser} ',
                                   parse_mode='html')
    if message.text.lower() in ["Купить бизнес 5", "купить бизнес 5"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        user_id = msg.from_user.id
        rwin = random.choice(win)
        Biz = cursor.execute("SELECT Biz from users where user_id = ?", (message.from_user.id,)).fetchone()
        Biz = str(Biz[0])
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        if int(balance) >= 1000000000000000:
            await bot.send_message(message.chat.id,
                                   f'{user_name}, вы успешно купили бизнес Стоительная компания 🏗 за 1.000.000.000.000.000$ {rwin} ',
                                   parse_mode='html')
            cursor.execute(f'UPDATE users SET Biz = "Стоительная компания" WHERE user_id = "{user_id}"')
            cursor.execute(f'UPDATE users SET balance = {balance - 1000000000000000} WHERE user_id = "{user_id}"')
            connect.commit()
        if int(balance) < 1000000000000000:
            await bot.send_message(message.chat.id, f'{user_name}, у вас не достаточно средств! {rloser} ',
                                   parse_mode='html')
    if message.text.lower() in ["Купить бизнес 4", "купить бизнес 4"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        user_id = msg.from_user.id
        rwin = random.choice(win)
        Biz = cursor.execute("SELECT Biz from users where user_id = ?", (message.from_user.id,)).fetchone()
        Biz = str(Biz[0])
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        if int(balance) >= 500000000000000:
            await bot.send_message(message.chat.id,
                                   f'{user_name}, вы успешно купили бизнес Парк Аткракционов 🎠 за 500.000.000.000.000$ {rwin} ',
                                   parse_mode='html')
            cursor.execute(f'UPDATE users SET Biz = "Парк Аткракционов" WHERE user_id = "{user_id}"')
            cursor.execute(f'UPDATE users SET balance = {balance - 500000000000000} WHERE user_id = "{user_id}"')
            connect.commit()
        if int(balance) < 500000000000000:
            await bot.send_message(message.chat.id, f'{user_name}, у вас не достаточно средств! {rloser} ',
                                   parse_mode='html')
    if message.text.lower() in ["Купить бизнес 3", "купить бизнес 3"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        user_id = msg.from_user.id
        rwin = random.choice(win)
        Biz = cursor.execute("SELECT Biz from users where user_id = ?", (message.from_user.id,)).fetchone()
        Biz = str(Biz[0])
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        if int(balance) >= 150000000000000:
            await bot.send_message(message.chat.id,
                                   f'{user_name}, вы успешно купили бизнес Магазин 24/7 🏬 за 150.000.000.000.000$ {rwin} ',
                                   parse_mode='html')
            cursor.execute(f'UPDATE users SET Biz = "Магазин 24/7" WHERE user_id = "{user_id}"')
            cursor.execute(f'UPDATE users SET balance = {balance - 150000000000000} WHERE user_id = "{user_id}"')
            connect.commit()
        if int(balance) < 150000000000000:
            await bot.send_message(message.chat.id, f'{user_name}, у вас не достаточно средств! {rloser} ',
                                   parse_mode='html')
    if message.text.lower() in ["Купить бизнес 2", "купить бизнес 2"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        user_id = msg.from_user.id
        rwin = random.choice(win)
        Biz = cursor.execute("SELECT Biz from users where user_id = ?", (message.from_user.id,)).fetchone()
        Biz = str(Biz[0])
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        if int(balance) >= 2000000000000:
            await bot.send_message(message.chat.id,
                                   f'{user_name}, вы успешно купили бизнес Кафе ☕️ за 2.000.000.000.000$ {rwin} ',
                                   parse_mode='html')
            cursor.execute(f'UPDATE users SET Biz = "Кафе" WHERE user_id = "{user_id}"')
            cursor.execute(f'UPDATE users SET balance = {balance - 2000000000000} WHERE user_id = "{user_id}"')
            connect.commit()
        if int(balance) < 2000000000000:
            await bot.send_message(message.chat.id, f'{user_name}, у вас не достаточно средств! {rloser} ',
                                   parse_mode='html')
    if message.text.lower() in ["Купить бизнес 1", "купить бизнес 1"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        user_id = msg.from_user.id
        rwin = random.choice(win)
        Biz = cursor.execute("SELECT Biz from users where user_id = ?", (message.from_user.id,)).fetchone()
        Biz = str(Biz[0])
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        if int(balance) >= 500000000000:
            await bot.send_message(message.chat.id,
                                   f'{user_name}, вы успешно купили бизнес Забигаловка 🫔 за 500.000.000.000$ {rwin} ',
                                   parse_mode='html')
            cursor.execute(f'UPDATE users SET Biz = "Забигаловка" WHERE user_id = "{user_id}"')
            cursor.execute(f'UPDATE users SET balance = {balance - 500000000000} WHERE user_id = "{user_id}"')
            connect.commit()
        if int(balance) < 500000000000:
            await bot.send_message(message.chat.id, f'{user_name}, у вас не достаточно средств! {rloser} ',
                                   parse_mode='html')


    if message.text.lower() in ['Мой бизнес', "мой бизнес"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        Biz = cursor.execute("SELECT Biz from users where user_id = ?", (message.from_user.id,)).fetchone()
        Рабочие = cursor.execute("SELECT Рабочие from Бизнес where user_id = ?", (message.from_user.id,)).fetchone()
        Рабочие = int(Рабочие[0])
        Баланс = cursor.execute("SELECT Баланс from Бизнес where user_id = ?", (message.from_user.id,)).fetchone()
        Баланс = int(Баланс[0])
        Рабочие2 = '{:,}'.format(Рабочие)
        Баланс2 = '{:,}'.format(Баланс)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        if Biz[0] == '':
            await bot.send_message(message.chat.id,f'{user_name}, Извините . Но у вас нету бизнеса{rloser}\nℹ️Что бы посмотреть список Бизнесов для покупки введите команду\nℹ️Бизнесы',parse_mode='html')

        if Biz[0] == 'Кафе':
            await bot.send_message(message.chat.id,
                                   f'☕️ | Бизнес: Кафе\n👤 | Владелец: {user_name}\n💰 | Баланс бизнеса: {Баланс2}$\n\nℹ️Что бы начать рабочий день введите команду\nℹ️Бизнес начать\n\n🆘Что бы снять с баланса Бизнеса введите команду\n🆘Бизнес снять [Сумма]',parse_mode='html')

        if Biz[0] == 'Банк':
            await bot.send_message(message.chat.id,
                                   f'🏦 | Бизнес: Банк\n👤 | Владелец: {user_name}\n💰 | Баланс бизнеса: {Баланс2}$\n\nℹ️Что бы начать рабочий день введите команду\nℹ️Бизнес начать\n\n🆘Что бы снять с баланса Бизнеса введите команду\n🆘Бизнес снять [Сумма]',parse_mode='html')

        if Biz[0] == 'Завод':
            await bot.send_message(message.chat.id,
                                   f'🏭 | Бизнес: Завод\n👤 | Владелец: {user_name}\n💰 | Баланс бизнеса: {Баланс2}$\n\nℹ️Что бы начать рабочий день введите команду\nℹ️Бизнес начать\n\n🆘Что бы снять с баланса Бизнеса введите команду\n🆘Бизнес снять [Сумма]',parse_mode='html')

        if Biz[0] == 'Стоительная компания':
            await bot.send_message(message.chat.id,
                                   f'🏗 | Бизнес: Стоительная компания\n👤 | Владелец: {user_name}\n💰 | Баланс бизнеса: {Баланс2}$\n\nℹ️Что бы начать рабочий день введите команду\nℹ️Бизнес начать',parse_mode='html')

        if Biz[0] == 'Парк Аткракционов':
            await bot.send_message(message.chat.id,
                                   f'🎠 | Бизнес: Парк Аткракционов\n👤 | Владелец: {user_name}\n💰 | Баланс бизнеса: {Баланс2}$\n\nℹ️Что бы начать рабочий день введите команду\nℹ️Бизнес начать\n\n🆘Что бы снять с баланса Бизнеса введите команду\n🆘Бизнес снять [Сумма]',parse_mode='html')

        if Biz[0] == 'Магазин 24/7':
            await bot.send_message(message.chat.id,
                                   f'🏬 | Бизнес: Магазин 24/7\n👤 | Владелец: {user_name}\n💰 | Баланс бизнеса: {Баланс2}$\n\nℹ️Что бы начать рабочий день введите команду\nℹ️Бизнес начать\n\n🆘Что бы снять с баланса Бизнеса введите команду\n🆘Бизнес снять [Сумма]',parse_mode='html')

        if Biz[0] == 'Забигаловка':
            await bot.send_message(message.chat.id,
                                   f'🫔 | Бизнес: Забигаловка\n👤 | Владелец: {user_name}\n💰 | Баланс бизнеса: {Баланс2}$\n\nℹ️Что бы начать рабочий день введите команду\nℹ️Бизнес начать\n\n🆘Что бы снять с баланса Бизнеса введите команду\n🆘Бизнес снять [Сумма]',parse_mode='html')


    if message.text.lower() in ['Бизнесы', "бизнесы"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        await bot.send_message(message.chat.id,f'{user_name},вот список бизнесов 🏭\n🫔 | [1] Бомжатник - 500.000.000.000$\n☕ | [2] Кафе - 2.000.000.000.000$\n🏬 | [3] Магазин 24/7 - 150.000.000.000.000$\n🎠 | [4] Парк Аткракционов - 500.000.000.000.000$\n🏗 | [5] Стоительная компания - 1.000.000.000.000.000$\n🏭 | [6]Завод - 15.000.000.000.000.000$\n🏦 | [7] Банк - 50.000.000.000.000.000$\n\nℹ️ Что бы купить бизнес введите команду \nℹ️Купить бизнес [Номер бизнеса]',parse_mode='html')
    if message.text.lower() in ['Бизнес', "бизнес"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        await bot.send_message(message.chat.id,f'{user_name}, Вот все команды связаные с Бизнесами 🏭\n🏭 | Мой бизнес - показывает всю информацию про ваш бизнес\n🏭 | Бизнесы - показует список бизнесов в продаже',parse_mode='html')
    
    
    
    
    
    
    
    
    ###########################################ТЕЛЕФОНЫ#########################################
    if message.text.lower() in ["Мой телефон", "мой телефон", "Мой Телефон", "мой Телефон"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🏠', '🏡']
        user_id = msg.from_user.id
        rwin = random.choice(win)
        Phone = cursor.execute("SELECT Phone from users where user_id = ?", (message.from_user.id,)).fetchone()

        if Phone[0] == 'Samsung A31':
            await bot.send_message(message.chat.id,
                                 f'👤 Владелец: {user_name}\n📱 Телефон: Samsung A31\n📁 Память : 16ГБ \n🔋 Количество ядер : 2',
                                 parse_mode='html')
        if Phone[0] == 'iPhone XS MAX':
            await bot.send_message(message.chat.id,
                                 f'👤 Владелец: {user_name}\n📱 Телефон: iPhone XS MAX\n📁 Память : 1024ГБ \n🔋 Количество ядер : 64',
                                 parse_mode='html')

        if Phone[0] == 'iPhone XS':
            await bot.send_message(message.chat.id,
                                 f'👤 Владелец: {user_name}\n📱 Телефон: iPhone XS\n📁 Память : 256ГБ \n🔋 Количество ядер : 32',
                                 parse_mode='html')

        if Phone[0] == 'iPhone 13 pro max':
            await bot.send_message(message.chat.id,
                                 f'👤 Владелец: {user_name}\n📱 Телефон: iPhone 13 pro max\n📁 Память : 256ГБ \n🔋 Количество ядер : 16',
                                 parse_mode='html')

        if Phone[0] == 'iPhone 12 pro max':
            await bot.send_message(message.chat.id,
                                 f'👤 Владелец: {user_name}\n📱 Телефон: iPhone 12 pro max\n📁 Память : 128ГБ \n🔋 Количество ядер : 8',
                                 parse_mode='html')

        if Phone[0] == 'Samsung A71':
            await bot.send_message(message.chat.id,
                                 f'👤 Владелец: {user_name}\n📱 Телефон: Samsung A71\n📁 Память : 128ГБ \n🔋 Количество ядер : 6',
                                 parse_mode='html')

        if Phone[0] == 'Samsung A51':
            await bot.send_message(message.chat.id,
                                 f'👤 Владелец: {user_name}\n📱 Телефон: Samsung A51\n📁 Память : 64ГБ \n🔋 Количество ядер : 4',
                                 parse_mode='html')

        if Phone[0] == 'RedMagic 6+':
            await bot.send_message(message.chat.id,
                                 f'👤 Владелец: {user_name}\n📱 Телефон: RedMagic 6+\n📁 Память : 64ГБ \n🔋 Количество ядер : 3',
                                 parse_mode='html')

        if Phone[0] == 'Redmi 10T':
            await bot.send_message(message.chat.id,
                                 f'👤 Владелец: {user_name}\n📱 Телефон: Redmi 10T\n📁 Память : 32ГБ \n🔋 Количество ядер : 3',
                                 parse_mode='html')

        if Phone[0] == 'Samsung A41':
            await bot.send_message(message.chat.id,
                                 f'👤 Владелец: {user_name}\n📱 Телефон: Samsung A41\n📁 Память : 32ГБ \n🔋 Количество ядер : 3',
                                 parse_mode='html')

        if Phone[0] == 'Samsung A32':
            await bot.send_message(message.chat.id,
                                 f'👤 Владелец: {user_name}\n📱 Телефон: Samsung A32\n📁 Память : 16ГБ \n🔋 Количество ядер : 3',
                                 parse_mode='html')

        if Phone[0] == '':
            await bot.send_message(message.chat.id,
                                   f'{user_name} у вас нету телефона , что бы посмотреть список для покупки телефона введите \nℹ️ Телефоны',
                                   parse_mode='html')
        if Phone[0] == 'Nokia 12 02':
            await bot.send_message(message.chat.id,
                                 f'👤 Владелец: {user_name}\n📱 Телефон: Nokia 12 02\n📁 Память : 4ГБ \n🔋 Количество ядер : 1',
                                 parse_mode='html')

    if message.text.lower() in ["Купить телефон 12", "купить телефон 12"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        user_id = msg.from_user.id
        rwin = random.choice(win)
        Phone = cursor.execute("SELECT Phone from users where user_id = ?", (message.from_user.id,)).fetchone()
        Phone = str(Phone[0])
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        if int(balance) >= 500000000000000000:
            await bot.send_message(message.chat.id,
                                   f'{user_name}, вы успешно купили телефон iPhone XS MAX 📱 за 500.000.000.000.000.000$ {rwin} ',
                                   parse_mode='html')
            cursor.execute(f'UPDATE users SET Phone = "iPhone XS MAX" WHERE user_id = "{user_id}"')
            cursor.execute(f'UPDATE users SET balance = {balance - 500000000000000000} WHERE user_id = "{user_id}"')
            connect.commit()
        if int(balance) < 500000000000000000:
            await bot.send_message(message.chat.id, f'{user_name}, у вас не достаточно средств! {rloser} ',
                                   parse_mode='html')
    if message.text.lower() in ["Купить телефон 11", "купить телефон 11"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        user_id = msg.from_user.id
        rwin = random.choice(win)
        Phone = cursor.execute("SELECT Phone from users where user_id = ?", (message.from_user.id,)).fetchone()
        Phone = str(Phone[0])
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        if int(balance) >= 180000000000000000:
            await bot.send_message(message.chat.id,
                                   f'{user_name}, вы успешно купили телефон iPhone XS 📱 за 180.000.000.000.000.000$ {rwin} ',
                                   parse_mode='html')
            cursor.execute(f'UPDATE users SET Phone = "iPhone XS" WHERE user_id = "{user_id}"')
            cursor.execute(f'UPDATE users SET balance = {balance - 180000000000000000} WHERE user_id = "{user_id}"')
            connect.commit()
        if int(balance) < 180000000000000000:
            await bot.send_message(message.chat.id, f'{user_name}, у вас не достаточно средств! {rloser} ',
                                   parse_mode='html')
    if message.text.lower() in ["Купить телефон 10", "купить телефон 10"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        user_id = msg.from_user.id
        rwin = random.choice(win)
        Phone = cursor.execute("SELECT Phone from users where user_id = ?", (message.from_user.id,)).fetchone()
        Phone = str(Phone[0])
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        if int(balance) >= 20000000000000000:
            await bot.send_message(message.chat.id,
                                   f'{user_name}, вы успешно купили телефон iPhone 13 pro max 📱 за 20.000.000.000.000.000$ {rwin} ',
                                   parse_mode='html')
            cursor.execute(f'UPDATE users SET Phone = "iPhone 13 pro max" WHERE user_id = "{user_id}"')
            cursor.execute(f'UPDATE users SET balance = {balance - 20000000000000000} WHERE user_id = "{user_id}"')
            connect.commit()
        if int(balance) < 20000000000000000:
            await bot.send_message(message.chat.id, f'{user_name}, у вас не достаточно средств! {rloser} ',
                                   parse_mode='html')
    if message.text.lower() in ["Купить телефон 9", "купить телефон 9"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        user_id = msg.from_user.id
        rwin = random.choice(win)
        Phone = cursor.execute("SELECT Phone from users where user_id = ?", (message.from_user.id,)).fetchone()
        Phone = str(Phone[0])
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        if int(balance) >= 2000000000000000:
            await bot.send_message(message.chat.id,
                                   f'{user_name}, вы успешно купили телефон iPhone 12 pro max 📱 за 2.000.000.000.000.000$ {rwin} ',
                                   parse_mode='html')
            cursor.execute(f'UPDATE users SET Phone = "iPhone 12 pro max" WHERE user_id = "{user_id}"')
            cursor.execute(f'UPDATE users SET balance = {balance - 2000000000000000} WHERE user_id = "{user_id}"')
            connect.commit()
        if int(balance) < 2000000000000000:
            await bot.send_message(message.chat.id, f'{user_name}, у вас не достаточно средств! {rloser} ',
                                   parse_mode='html')
    if message.text.lower() in ["Купить телефон 8", "купить телефон 8"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        user_id = msg.from_user.id
        rwin = random.choice(win)
        Phone = cursor.execute("SELECT Phone from users where user_id = ?", (message.from_user.id,)).fetchone()
        Phone = str(Phone[0])
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        if int(balance) >= 900000000000000:
            await bot.send_message(message.chat.id,
                                   f'{user_name}, вы успешно купили телефон Samsung A71 📱 за 900.000.000.000.000$ {rwin} ',
                                   parse_mode='html')
            cursor.execute(f'UPDATE users SET balance = {balance - 900000000000000} WHERE user_id = "{user_id}"')
            cursor.execute(f'UPDATE users SET Phone = "Samsung A71" WHERE user_id = "{user_id}"')
            connect.commit()
        if int(balance) < 900000000000000:
            await bot.send_message(message.chat.id, f'{user_name}, у вас не достаточно средств! {rloser} ',
                                   parse_mode='html')
    if message.text.lower() in ["Купить телефон 7", "купить телефон 7"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        user_id = msg.from_user.id
        rwin = random.choice(win)
        Phone = cursor.execute("SELECT Phone from users where user_id = ?", (message.from_user.id,)).fetchone()
        Phone = str(Phone[0])
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        if int(balance) >= 350000000000000:
            await bot.send_message(message.chat.id,
                                   f'{user_name}, вы успешно купили телефон Samsung A51 📱 за 350.000.000.000.000$ {rwin} ',
                                   parse_mode='html')
            cursor.execute(f'UPDATE users SET balance = {balance - 350000000000000} WHERE user_id = "{user_id}"')
            cursor.execute(f'UPDATE users SET Phone = "Samsung A51" WHERE user_id = "{user_id}"')
            connect.commit()
        if int(balance) < 350000000000000:
            await bot.send_message(message.chat.id, f'{user_name}, у вас не достаточно средств! {rloser} ',
                                   parse_mode='html')
    if message.text.lower() in ["Купить телефон 6", "купить телефон 6"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        user_id = msg.from_user.id
        rwin = random.choice(win)
        Phone = cursor.execute("SELECT Phone from users where user_id = ?", (message.from_user.id,)).fetchone()
        Phone = str(Phone[0])
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        if int(balance) >= 15000000000000:
            await bot.send_message(message.chat.id,
                                   f'{user_name}, вы успешно купили телефон RedMagic 6+ 📱 за 15.000.000.000.000$ {rwin} ',
                                   parse_mode='html')
            cursor.execute(f'UPDATE users SET balance = {balance - 15000000000000} WHERE user_id = "{user_id}"')
            cursor.execute(f'UPDATE users SET Phone = "RedMagic 6+" WHERE user_id = "{user_id}"')
            connect.commit()
        if int(balance) < 15000000000000:
            await bot.send_message(message.chat.id, f'{user_name}, у вас не достаточно средств! {rloser} ',
                                   parse_mode='html')
    if message.text.lower() in ["Купить телефон 5", "купить телефон 5"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        user_id = msg.from_user.id
        rwin = random.choice(win)
        Phone = cursor.execute("SELECT Phone from users where user_id = ?", (message.from_user.id,)).fetchone()
        Phone = str(Phone[0])
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        if int(balance) >= 2000000000000:
            await bot.send_message(message.chat.id,
                                   f'{user_name}, вы успешно купили телефон Redmi 10T 📱 за 2.000.000.000.000$ {rwin} ',
                                   parse_mode='html')
            cursor.execute(f'UPDATE users SET balance = {balance - 2000000000000} WHERE user_id = "{user_id}"')
            cursor.execute(f'UPDATE users SET Phone = "Redmi 10T" WHERE user_id = "{user_id}"')
            connect.commit()
        if int(balance) < 2000000000000:
            await bot.send_message(message.chat.id, f'{user_name}, у вас не достаточно средств! {rloser} ',
                                   parse_mode='html')
    if message.text.lower() in ["Купить телефон 4", "купить телефон 4"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        user_id = msg.from_user.id
        rwin = random.choice(win)
        Phone = cursor.execute("SELECT Phone from users where user_id = ?", (message.from_user.id,)).fetchone()
        Phone = str(Phone[0])
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        if int(balance) >= 800000000000:
            await bot.send_message(message.chat.id,
                                   f'{user_name}, вы успешно купили телефон Samsung A41 📱 за  800.000.000.000$ {rwin} ',
                                   parse_mode='html')
            cursor.execute(f'UPDATE users SET balance = {balance - 800000000000} WHERE user_id = "{user_id}"')
            cursor.execute(f'UPDATE users SET Phone = "Samsung A41" WHERE user_id = "{user_id}"')
            connect.commit()
        if int(balance) < 800000000000:
            await bot.send_message(message.chat.id, f'{user_name}, у вас не достаточно средств! {rloser} ',
                                   parse_mode='html')
    if message.text.lower() in ["Купить телефон 3", "купить телефон 3"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        user_id = msg.from_user.id
        rwin = random.choice(win)
        Phone = cursor.execute("SELECT Phone from users where user_id = ?", (message.from_user.id,)).fetchone()
        Phone = str(Phone[0])
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        if int(balance) >= 250000000000:
            await bot.send_message(message.chat.id,
                                   f'{user_name}, вы успешно купили телефон Samsung A32 📱 за 250.000.000.000$ {rwin} ',
                                   parse_mode='html')
            cursor.execute(f'UPDATE users SET balance = {balance - 250000000000} WHERE user_id = "{user_id}"')
            cursor.execute(f'UPDATE users SET Phone = "Samsung A32" WHERE user_id = "{user_id}"')
            connect.commit()
        if int(balance) < 250000000000:
            await bot.send_message(message.chat.id, f'{user_name}, у вас не достаточно средств! {rloser} ',
                                   parse_mode='html')
    if message.text.lower() in ["Купить телефон 2", "купить телефон 2"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        user_id = msg.from_user.id
        rwin = random.choice(win)
        Phone = cursor.execute("SELECT Phone from users where user_id = ?", (message.from_user.id,)).fetchone()
        Phone = str(Phone[0])
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        if int(balance) >= 100000000000:
            await bot.send_message(message.chat.id,
                                   f'{user_name}, вы успешно купили телефон Samsung A31 📱 за 100.000.000.000$ {rwin} ',
                                   parse_mode='html')
            cursor.execute(f'UPDATE users SET balance = {balance - 100000000000} WHERE user_id = "{user_id}"')
            cursor.execute(f'UPDATE users SET Phone = "Samsung A31" WHERE user_id = "{user_id}"')
            connect.commit()
        if int(balance) < 100000000000:
            await bot.send_message(message.chat.id, f'{user_name}, у вас не достаточно средств! {rloser} ',
                                   parse_mode='html')
    if message.text.lower() in ["Купить телефон 1", "купить телефон 1"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        user_id = msg.from_user.id
        rwin = random.choice(win)
        Phone = cursor.execute("SELECT Phone from users where user_id = ?", (message.from_user.id,)).fetchone()
        Phone = str(Phone[0])
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        if int(balance) >= 15000000000:
            await bot.send_message(message.chat.id,
                                   f'{user_name}, вы успешно купили телефон Nokia 12 02 📱 за 15.000.000.000$ {rwin} ',
                                   parse_mode='html')
            cursor.execute(f'UPDATE users SET balance = {balance - 15000000000} WHERE user_id = "{user_id}"')
            cursor.execute(f'UPDATE users SET Phone = "Nokia 12 02" WHERE user_id = "{user_id}"')
            connect.commit()
        if int(balance) < 15000000000:
            await bot.send_message(message.chat.id, f'{user_name}, у вас не достаточно средств! {rloser} ',
                                   parse_mode='html')

    if message.text.lower() in ["Телефоны", "телефоны"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🏠', '🏡']
        user_id = msg.from_user.id
        rwin = random.choice(win)
        Phone = cursor.execute("SELECT Phone from users where user_id = ?", (message.from_user.id,)).fetchone()
        await bot.send_message(message.chat.id,
                               f'{user_name}, Вот список Телефонов для покупки 📲\n📱 | [1] Nokia 12 02 - 1.000.000.000$\n📱 | [2] Samsung A31 - 100.000.000.000$\n📱 | [3] Samsung A32 - 250.000.000.000$\n📱 | [4] Samsung A41 - 800.000.000.000$\n📱 | [5] Chery QQ - 2.000.000.000.000$\n📱 | [6] Baojun 310 - 15.000.000.000.000$\n📱 | [7] Samsung A51 - 350.000.000.000.000$\n📱 | [8] Samsung A71 - 900.000.000.000.000$\n📱 | [9] iPhone 12 pro max - 2.000.000.000.000.000$\n📱 | [10] iPhone 13 pro max - 20.000.000.000.000.000$\n📱 | [11] iPhone XS - 180.000.000.000.000.000$\n📱 | [12] iPhone XS MAX - 500.000.000.000.000.000$\n\nℹ️ Для покупки телефона введите команду\nℹ Купить телефон [Номер телефона]',
                               parse_mode='html')
    if message.text.lower() in ["Телефон", "телефон"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['📱', '📲']
        user_id = msg.from_user.id
        rwin = random.choice(win)
        Avto = cursor.execute("SELECT Avto from users where user_id = ?", (message.from_user.id,)).fetchone()
        await bot.send_message(message.chat.id,
                               f'{user_name},Вот команды связаные с Телефонами{rwin}\n\n📲 Мой телефон - Вся информация про ваш телефон\n📱 Телефоны - Показует список телефонов в продаже ',
                               parse_mode='html')
    ###########################################МАШИНЫ###########################################
    if message.text.lower() in ["Моя машина", "моя машина", "Моя Машина", "моя Машина"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🏠', '🏡']
        user_id = msg.from_user.id
        rwin = random.choice(win)
        Avto = cursor.execute("SELECT Avto from users where user_id = ?", (message.from_user.id,)).fetchone()

        if Avto[0] == 'Bajaj Qute':
            await bot.send_message(message.chat.id,
                                 f'👤 Владелец: {user_name}\n🚘 Транспорт: Bajaj Qute\n👥 Мест в транспорте: 4\n📌 Класс транспорта : Низкий',
                                 parse_mode='html')
        if Avto[0] == 'SD-HZ 1':
            await bot.send_message(message.chat.id,
                                 f'👤 Владелец: {user_name}\n🚘 Транспорт: SD-HZ 1\n👥 Мест в транспорте: 1\n📌 Класс транспорта : Низкий',
                                 parse_mode='html')
        if Avto[0] == 'Tata Nano':
            await bot.send_message(message.chat.id,
                                 f'👤 Владелец: {user_name}\n🚘 Транспорт: Tata Nano\n👥 Мест в транспорте: 2\n📌 Класс транспорта : Низкий',
                                 parse_mode='html')
        if Avto[0] == 'Duesenberg SSJ':
            await bot.send_message(message.chat.id,
                                 f'👤 Владелец: {user_name}\n🚘 Транспорт: Duesenberg SSJ\n👥 Мест в транспорте: 2\n📌 Класс транспорта : Премиум Люкс',
                                 parse_mode='html')
        if Avto[0] == 'Pagani Zonda HP Barchetta':
            await bot.send_message(message.chat.id,
                                 f'👤 Владелец: {user_name}\n🚘 Транспорт: Pagani Zonda HP Barchetta\n👥 Мест в транспорте: 2\n📌 Класс транспорта : Люкс',
                                 parse_mode='html')
        if Avto[0] == 'Rolls-Royce Ghost':
            await bot.send_message(message.chat.id,
                                 f'👤 Владелец: {user_name}\n🚘 Транспорт: Rolls-Royce Ghost\n👥 Мест в транспорте: 4\n📌 Класс транспорта : Люкс',
                                 parse_mode='html')
        if Avto[0] == 'Bugatti Chiron':
            await bot.send_message(message.chat.id,
                                 f'👤 Владелец: {user_name}\n🚘 Транспорт: Bugatti Chiron\n👥 Мест в транспорте: 2\n📌 Класс транспорта : Высокий',
                                 parse_mode='html')
        if Avto[0] == 'McLaren P1 LM':
            await bot.send_message(message.chat.id,
                                 f'👤 Владелец: {user_name}\n🚘 Транспорт: McLaren P1 LM\n👥 Мест в транспорте: 2\n📌 Класс транспорта : Высокий',
                                 parse_mode='html')
        if Avto[0] == 'Lamborghini Veneno Roadster':
            await bot.send_message(message.chat.id,
                                 f'👤 Владелец: {user_name}\n🚘 Транспорт: Lamborghini Veneno Roadster\n👥 Мест в транспорте: 2\n📌 Класс транспорта : Высокий',
                                 parse_mode='html')
        if Avto[0] == 'Baojun 310':
            await bot.send_message(message.chat.id,
                                 f'👤 Владелец: {user_name}\n🚘 Транспорт: Baojun 310\n👥 Мест в транспорте: 4\n📌 Класс транспорта : Средний',
                                 parse_mode='html')
        if Avto[0] == 'Chery QQ':
            await bot.send_message(message.chat.id,
                                 f'👤 Владелец: {user_name}\n🚘 Транспорт: Chery QQ\n👥 Мест в транспорте: 4\n📌 Класс транспорта : Средний',
                                 parse_mode='html')
        if Avto[0] == 'Datsun Redi-Go':
            await bot.send_message(message.chat.id,
                                 f'👤 Владелец: {user_name}\n🚘 Транспорт: Datsun Redi-Go\n👥 Мест в транспорте: 4\n📌 Класс транспорта : Средний',
                                 parse_mode='html')
        if Avto[0] == 'Велосипед':
            await bot.send_message(message.chat.id,
                                 f'👤 Владелец: {user_name}\n🚘 Транспорт: Велосипед\n👥 Мест в транспорте: 2\n📌 Класс транспорта : Низкий',
                                 parse_mode='html')

    if message.text.lower() in ["Купить машину 12", "купить машину 12"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        user_id = msg.from_user.id
        rwin = random.choice(win)
        Avto = cursor.execute("SELECT Avto from users where user_id = ?", (message.from_user.id,)).fetchone()
        Avto = str(Avto[0])
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        if int(balance) >= 500000000000000000:
            await bot.send_message(message.chat.id,
                                   f'{user_name}, вы успешно купили машину Duesenberg SSJ 🏎 за 500.000.000.000.000.000$ {rwin} ',
                                   parse_mode='html')
            cursor.execute(f'UPDATE users SET Avto = "Duesenberg SSJ" WHERE user_id = "{user_id}"')
            cursor.execute(f'UPDATE users SET balance = {balance - 500000000000000000} WHERE user_id = "{user_id}"')
            connect.commit()
        if int(balance) < 500000000000000000:
            await bot.send_message(message.chat.id, f'{user_name}, у вас не достаточно средств! {rloser} ',
                                   parse_mode='html')
    if message.text.lower() in ["Купить машину 11", "купить машину 11"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        user_id = msg.from_user.id
        rwin = random.choice(win)
        Avto = cursor.execute("SELECT Avto from users where user_id = ?", (message.from_user.id,)).fetchone()
        Avto = str(Avto[0])
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        if int(balance) >= 180000000000000000:
            await bot.send_message(message.chat.id,
                                   f'{user_name}, вы успешно купили машину Pagani Zonda HP Barchetta 🏎 за 180.000.000.000.000.000$ {rwin} ',
                                   parse_mode='html')
            cursor.execute(f'UPDATE users SET Avto = "Pagani Zonda HP Barchetta" WHERE user_id = "{user_id}"')
            cursor.execute(f'UPDATE users SET balance = {balance - 180000000000000000} WHERE user_id = "{user_id}"')
            connect.commit()
        if int(balance) < 180000000000000000:
            await bot.send_message(message.chat.id, f'{user_name}, у вас не достаточно средств! {rloser} ',
                                   parse_mode='html')
    if message.text.lower() in ["Купить машину 10", "купить машину 10"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        user_id = msg.from_user.id
        rwin = random.choice(win)
        Avto = cursor.execute("SELECT Avto from users where user_id = ?", (message.from_user.id,)).fetchone()
        Avto = str(Avto[0])
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        if int(balance) >= 20000000000000000:
            await bot.send_message(message.chat.id,
                                   f'{user_name}, вы успешно купили машину Rolls-Royce Ghost 🏎 за 20.000.000.000.000.000$ {rwin} ',
                                   parse_mode='html')
            cursor.execute(f'UPDATE users SET Avto = "Rolls-Royce Ghost" WHERE user_id = "{user_id}"')
            cursor.execute(f'UPDATE users SET balance = {balance - 20000000000000000} WHERE user_id = "{user_id}"')
            connect.commit()
        if int(balance) < 20000000000000000:
            await bot.send_message(message.chat.id, f'{user_name}, у вас не достаточно средств! {rloser} ',
                                   parse_mode='html')
    if message.text.lower() in ["Купить машину 9", "купить машину 9"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        user_id = msg.from_user.id
        rwin = random.choice(win)
        Avto = cursor.execute("SELECT Avto from users where user_id = ?", (message.from_user.id,)).fetchone()
        Avto = str(Avto[0])
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        if int(balance) >= 2000000000000000:
            await bot.send_message(message.chat.id,
                                   f'{user_name}, вы успешно купили машину Bugatti Chiron 🏎 за 2.000.000.000.000.000$ {rwin} ',
                                   parse_mode='html')
            cursor.execute(f'UPDATE users SET Avto = "Bugatti Chiron" WHERE user_id = "{user_id}"')
            cursor.execute(f'UPDATE users SET balance = {balance - 2000000000000000} WHERE user_id = "{user_id}"')
            connect.commit()
        if int(balance) < 2000000000000000:
            await bot.send_message(message.chat.id, f'{user_name}, у вас не достаточно средств! {rloser} ',
                                   parse_mode='html')
    if message.text.lower() in ["Купить машину 8", "купить машину 8"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        user_id = msg.from_user.id
        rwin = random.choice(win)
        Avto = cursor.execute("SELECT Avto from users where user_id = ?", (message.from_user.id,)).fetchone()
        Avto = str(Avto[0])
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        if int(balance) >= 900000000000000:
            await bot.send_message(message.chat.id,
                                   f'{user_name}, вы успешно купили машину McLaren P1 LM 🏎 за 900.000.000.000.000$ {rwin} ',
                                   parse_mode='html')
            cursor.execute(f'UPDATE users SET balance = {balance - 900000000000000} WHERE user_id = "{user_id}"')
            cursor.execute(f'UPDATE users SET Avto = "McLaren P1 LM" WHERE user_id = "{user_id}"')
            connect.commit()
        if int(balance) < 900000000000000:
            await bot.send_message(message.chat.id, f'{user_name}, у вас не достаточно средств! {rloser} ',
                                   parse_mode='html')
    if message.text.lower() in ["Купить машину 7", "купить машину 7"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        user_id = msg.from_user.id
        rwin = random.choice(win)
        Avto = cursor.execute("SELECT Avto from users where user_id = ?", (message.from_user.id,)).fetchone()
        Avto = str(Avto[0])
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        if int(balance) >= 350000000000000:
            await bot.send_message(message.chat.id,
                                   f'{user_name}, вы успешно купили машину Lamborghini Veneno Roadster 🚗 за 350.000.000.000.000$ {rwin} ',
                                   parse_mode='html')
            cursor.execute(f'UPDATE users SET balance = {balance - 350000000000000} WHERE user_id = "{user_id}"')
            cursor.execute(f'UPDATE users SET Avto = "Lamborghini Veneno Roadster" WHERE user_id = "{user_id}"')
            connect.commit()
        if int(balance) < 350000000000000:
            await bot.send_message(message.chat.id, f'{user_name}, у вас не достаточно средств! {rloser} ',
                                   parse_mode='html')
    if message.text.lower() in ["Купить машину 6", "купить машину 6"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        user_id = msg.from_user.id
        rwin = random.choice(win)
        Avto = cursor.execute("SELECT Avto from users where user_id = ?", (message.from_user.id,)).fetchone()
        Avto = str(Avto[0])
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        if int(balance) >= 15000000000000:
            await bot.send_message(message.chat.id,
                                   f'{user_name}, вы успешно купили машину Baojun 310 🚗 за 15.000.000.000.000$ {rwin} ',
                                   parse_mode='html')
            cursor.execute(f'UPDATE users SET balance = {balance - 15000000000000} WHERE user_id = "{user_id}"')
            cursor.execute(f'UPDATE users SET Avto = "Baojun 310" WHERE user_id = "{user_id}"')
            connect.commit()
        if int(balance) < 15000000000000:
            await bot.send_message(message.chat.id, f'{user_name}, у вас не достаточно средств! {rloser} ',
                                   parse_mode='html')
    if message.text.lower() in ["Купить машину 5", "купить машину 5"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        user_id = msg.from_user.id
        rwin = random.choice(win)
        Avto = cursor.execute("SELECT Avto from users where user_id = ?", (message.from_user.id,)).fetchone()
        Avto = str(Avto[0])
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        if int(balance) >= 2000000000000:
            await bot.send_message(message.chat.id,
                                   f'{user_name}, вы успешно купили машину Chery QQ 🚗 за 2.000.000.000.000$ {rwin} ',
                                   parse_mode='html')
            cursor.execute(f'UPDATE users SET balance = {balance - 2000000000000} WHERE user_id = "{user_id}"')
            cursor.execute(f'UPDATE users SET Avto = "Chery QQ" WHERE user_id = "{user_id}"')
            connect.commit()
        if int(balance) < 2000000000000:
            await bot.send_message(message.chat.id, f'{user_name}, у вас не достаточно средств! {rloser} ',
                                   parse_mode='html')
    if message.text.lower() in ["Купить машину 4", "купить машину 4"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        user_id = msg.from_user.id
        rwin = random.choice(win)
        Avto = cursor.execute("SELECT Avto from users where user_id = ?", (message.from_user.id,)).fetchone()
        Avto = str(Avto[0])
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        if int(balance) >= 800000000000:
            await bot.send_message(message.chat.id,
                                   f'{user_name}, вы успешно купили машину Datsun Redi-Go за  800.000.000.000$ {rwin} ',
                                   parse_mode='html')
            cursor.execute(f'UPDATE users SET balance = {balance - 800000000000} WHERE user_id = "{user_id}"')
            cursor.execute(f'UPDATE users SET Avto = "Datsun Redi-Go" WHERE user_id = "{user_id}"')
            connect.commit()
        if int(balance) < 800000000000:
            await bot.send_message(message.chat.id, f'{user_name}, у вас не достаточно средств! {rloser} ',
                                   parse_mode='html')
    if message.text.lower() in ["Купить машину 3", "купить машину 3"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        user_id = msg.from_user.id
        rwin = random.choice(win)
        Avto = cursor.execute("SELECT Avto from users where user_id = ?", (message.from_user.id,)).fetchone()
        Avto = str(Avto[0])
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        if int(balance) >= 250000000000:
            await bot.send_message(message.chat.id,
                                   f'{user_name}, вы успешно купили машину Tata Nano 🚗 за 250.000.000.000$ {rwin} ',
                                   parse_mode='html')
            cursor.execute(f'UPDATE users SET balance = {balance - 250000000000} WHERE user_id = "{user_id}"')
            cursor.execute(f'UPDATE users SET Avto = "Tata Nano" WHERE user_id = "{user_id}"')
            connect.commit()
        if int(balance) < 250000000000:
            await bot.send_message(message.chat.id, f'{user_name}, у вас не достаточно средств! {rloser} ',
                                   parse_mode='html')
    if message.text.lower() in ["Купить машину 2", "купить машину 2"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        user_id = msg.from_user.id
        rwin = random.choice(win)
        Avto = cursor.execute("SELECT Avto from users where user_id = ?", (message.from_user.id,)).fetchone()
        Avto = str(Avto[0])
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        if int(balance) >= 100000000000:
            await bot.send_message(message.chat.id,
                                   f'{user_name}, вы успешно купили машину SD-HZ 1 🚗 за 100.000.000.000$ {rwin} ',
                                   parse_mode='html')
            cursor.execute(f'UPDATE users SET balance = {balance - 100000000000} WHERE user_id = "{user_id}"')
            cursor.execute(f'UPDATE users SET Avto = "SD-HZ 1" WHERE user_id = "{user_id}"')
            connect.commit()
        if int(balance) < 100000000000:
            await bot.send_message(message.chat.id, f'{user_name}, у вас не достаточно средств! {rloser} ',
                                   parse_mode='html')
    if message.text.lower() in ["Купить машину 1", "купить машину 1"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        user_id = msg.from_user.id
        rwin = random.choice(win)
        Avto = cursor.execute("SELECT Avto from users where user_id = ?", (message.from_user.id,)).fetchone()
        Avto = str(Avto[0])
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        if int(balance) >= 15000000000:
            await bot.send_message(message.chat.id,
                                   f'{user_name}, вы успешно купили машину Bajaj Qute 🚗 за 15.000.000.000$ {rwin} ',
                                   parse_mode='html')
            cursor.execute(f'UPDATE users SET balance = {balance - 15000000000} WHERE user_id = "{user_id}"')
            cursor.execute(f'UPDATE users SET Avto = "Bajaj Qute" WHERE user_id = "{user_id}"')
            connect.commit()
        if int(balance) < 15000000000:
            await bot.send_message(message.chat.id, f'{user_name}, у вас не достаточно средств! {rloser} ',
                                   parse_mode='html')

    if message.text.lower() in ["Машины", "машины"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🏠', '🏡']
        user_id = msg.from_user.id
        rwin = random.choice(win)
        Avto = cursor.execute("SELECT Avto from users where user_id = ?", (message.from_user.id,)).fetchone()
        await bot.send_message(message.chat.id,
                               f'{user_name}, Вот список Машин для покупки 🚘\n🚗 | [1] Bajaj Qute - 15.000.000.000$\n🚗 | [2] SD-HZ 1 - 100.000.000.000$\n🚗 | [3] Tata Nano - 250.000.000.000$\n🚗 | [4] Datsun Redi-Go - 800.000.000.000$\n🚗 | [5] Chery QQ - 2.000.000.000.000$\n🚗 | [6] Baojun 310 - 15.000.000.000.000$\n🚗 | [7] Lamborghini Veneno Roadster - 350.000.000.000.000$\n🏎 | [8] McLaren P1 LM - 900.000.000.000.000$\n🏎 | [9] Bugatti Chiron - 2.000.000.000.000.000$\n🏎 | [10] Rolls-Royce Ghost. - 20.000.000.000.000.000$\n🏎 | [11] Pagani Zonda HP Barchetta - 180.000.000.000.000.000$\n🏎 | [12] Duesenberg SSJ - 500.000.000.000.000.000$\n\nℹ️ Для покупки машины введите команду\nКупить машину [Номер Машины]',
                               parse_mode='html')
    if message.text.lower() in ["Машина", "машина"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🚗', '🚘']
        user_id = msg.from_user.id
        rwin = random.choice(win)
        Avto = cursor.execute("SELECT Avto from users where user_id = ?", (message.from_user.id,)).fetchone()
        await bot.send_message(message.chat.id,
                               f'{user_name},Вот команды связаные с Машинами{rwin}\n\n🚘 Моя машина - Вся информация про вашу Машину\n🚗 Машины - Показывает список Машин в продаже ',
                               parse_mode='html')
    ###########################################ДОМА#############################################
    if message.text.lower() in ["Мой дом", "мой дом", "Мой Дом", "мой Дом"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🏠', '🏡']
        user_id = msg.from_user.id
        rwin = random.choice(win)
        House = cursor.execute("SELECT House from users where user_id = ?", (message.from_user.id,)).fetchone()
        if House[0] == 'Канава':
            await bot.send_message(message.chat.id,
                                 f'👤 Владелец: {user_name}\n🏠 Дом: Канава\n🚪 Комнат в доме: 1\n🖼Ремонт в доме: Не имеиться',
                                 parse_mode='html')
        if House[0] == 'Коробка':
            await bot.send_message(message.chat.id,
                                 f'👤 Владелец: {user_name}\n🏠 Дом: Коробка\n🚪 Комнат в доме: 1\n🖼Ремонт в доме: Не имеиться',
                                 parse_mode='html')
        if House[0] == 'Халабуда':
            await bot.send_message(message.chat.id,
                                 f'👤 Владелец: {user_name}\n🏠 Дом: Халабуда\n🚪 Комнат в доме: 2\n🖼Ремонт в доме: Не имеиться',
                                 parse_mode='html')
        if House[0] == 'Палатка':
            await bot.send_message(message.chat.id,
                                 f'👤 Владелец: {user_name}\n🏠 Дом: Палатка\n🚪 Комнат в доме: 2\n🖼Ремонт в доме: Не имеиться',
                                 parse_mode='html')
        if House[0] == 'Заброшка':
            await bot.send_message(message.chat.id,
                                 f'👤 Владелец: {user_name}\n🏠 Дом: Заброшка\n🚪 Комнат в доме: 3\n🖼Ремонт в доме: Не имеиться',
                                 parse_mode='html')
        if House[0] == 'Сельский Домик':
            await bot.send_message(message.chat.id,
                                 f'👤 Владелец: {user_name}\n🏠 Дом: Сельский Домик\n🚪 Комнат в доме: 5\n🖼Ремонт в доме: Ремонт не имеиться',
                                 parse_mode='html')
        if House[0] == 'Квартира на обочине города':
            await bot.send_message(message.chat.id,
                                 f'👤 Владелец: {user_name}\n🏠 Дом: Квартира на обочине города\n🚪 Комнат в доме: 3\n🖼Ремонт в доме: Не имеиться',
                                 parse_mode='html')
        if House[0] == 'Квартира в центре города':
            await bot.send_message(message.chat.id,
                                 f'👤 Владелец: {user_name}\n🏠 Дом: Квартира в центре города\n🚪 Комнат в доме: 4\n🖼Ремонт в доме:имеиться',
                                 parse_mode='html')
        if House[0] == '3-х этажный дом':
            await bot.send_message(message.chat.id,
                                 f'👤 Владелец: {user_name}\n🏠 Дом: 3-х этажный дом\n🚪 Комнат в доме: 23\n🖼Ремонт в доме: Имеиться',
                                 parse_mode='html')
        if House[0] == '2-х этажный дом':
            await bot.send_message(message.chat.id,
                                 f'👤 Владелец: {user_name}\n🏠 Дом: 2-х этажный дом\n🚪 Комнат в доме: 15\n🖼Ремонт в доме: Имеиться',
                                 parse_mode='html')
        if House[0] == 'Особняк':
            await bot.send_message(message.chat.id,
                                 f'👤 Владелец: {user_name}\n🏠 Дом: Особняк\n🚪 Комнат в доме: 50\n🖼Ремонт в доме: Имеиться',
                                 parse_mode='html')
        if House[0] == 'Президента Особняк':
            await bot.send_message(message.chat.id,
                                 f'👤 Владелец: {user_name}\n🏠 Дом: Президента Особняк\n🚪 Комнат в доме: 113\n🖼Ремонт в доме: Имеиться',
                                 parse_mode='html')
        if House[0] == 'Часть Марса':
            await bot.send_message(message.chat.id,
                                 f'👤 Владелец: {user_name}\n🏠 Дом: Часть Марса\n🚪 Комнат в доме: ∞ \n🖼Ремонт в доме: Имеиться',
                                 parse_mode='html')
        if House[0] == 'Кусочек Луны':
            await bot.send_message(message.chat.id,
                                 f'👤 Владелец: {user_name}\n🏠 Дом: Кусочек Луны\n🚪 Комнат в доме: ∞ \n🖼Ремонт в доме: Имеиться',
                                 parse_mode='html')
        if House[0] == 'Яма':
            await bot.send_message(message.chat.id,
                                 f'👤 Владелец: {user_name}\n🏠 Дом: Яма\n🚪 Комнат в доме: 1\n🖼Ремонт в доме: Не имеиться',
                                 parse_mode='html')

    if message.text.lower() in ["Купить дом 14", "купить дом 14"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        user_id = msg.from_user.id
        rwin = random.choice(win)
        House = cursor.execute("SELECT House from users where user_id = ?", (message.from_user.id,)).fetchone()
        House = str(House[0])
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        if int(balance) >= 15000000000000:
            await bot.send_message(message.chat.id,
                                   f'{user_name}, вы успешно купили дом Часть Марса ☄️ за 15.000.000.000.000$ {rwin} ',
                                   parse_mode='html')
            cursor.execute(f'UPDATE users SET House = "Часть Марса" WHERE user_id = "{user_id}"')
            cursor.execute(f'UPDATE users SET balance = {balance - 15000000000000} WHERE user_id = "{user_id}"')
            connect.commit()
        if int(balance) < 15000000000000:
            await bot.send_message(message.chat.id, f'{user_name}, у вас не достаточно средств! {rloser} ',
                                   parse_mode='html')
    if message.text.lower() in ["Купить дом 13", "купить дом 13"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        user_id = msg.from_user.id
        rwin = random.choice(win)
        House = cursor.execute("SELECT House from users where user_id = ?", (message.from_user.id,)).fetchone()
        House = str(House[0])
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        if int(balance) >= 500000000000:
            await bot.send_message(message.chat.id,
                                   f'{user_name}, вы успешно купили дом Кусочек Луны 🌑 за 500.000.000.000$ {rwin} ',
                                   parse_mode='html')
            cursor.execute(f'UPDATE users SET House = "Кусочек Луны" WHERE user_id = "{user_id}"')
            cursor.execute(f'UPDATE users SET balance = {balance - 500000000000} WHERE user_id = "{user_id}"')
            connect.commit()
        if int(balance) < 500000000000:
            await bot.send_message(message.chat.id, f'{user_name}, у вас не достаточно средств! {rloser} ',
                                   parse_mode='html')
    if message.text.lower() in ["Купить дом 12", "купить дом 12"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        user_id = msg.from_user.id
        rwin = random.choice(win)
        House = cursor.execute("SELECT House from users where user_id = ?", (message.from_user.id,)).fetchone()
        House = str(House[0])
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        if int(balance) >= 2000000000:
            await bot.send_message(message.chat.id,
                                   f'{user_name}, вы успешно купили дом Президента Особняк 🏰 за 2.000.000.000$ {rwin} ',
                                   parse_mode='html')
            cursor.execute(f'UPDATE users SET House = "Президента Особняк" WHERE user_id = "{user_id}"')
            cursor.execute(f'UPDATE users SET balance = {balance - 2000000000} WHERE user_id = "{user_id}"')
            connect.commit()
        if int(balance) < 2000000000:
            await bot.send_message(message.chat.id, f'{user_name}, у вас не достаточно средств! {rloser} ',
                                   parse_mode='html')
    if message.text.lower() in ["Купить дом 11", "купить дом 11"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        user_id = msg.from_user.id
        rwin = random.choice(win)
        House = cursor.execute("SELECT House from users where user_id = ?", (message.from_user.id,)).fetchone()
        House = str(House[0])
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        if int(balance) >= 900000000:
            await bot.send_message(message.chat.id,
                                   f'{user_name}, вы успешно купили дом Особняк 🛕 за 900.000.000$ {rwin} ',
                                   parse_mode='html')
            cursor.execute(f'UPDATE users SET House = "Особняк" WHERE user_id = "{user_id}"')
            cursor.execute(f'UPDATE users SET balance = {balance - 900000000} WHERE user_id = "{user_id}"')
            connect.commit()
        if int(balance) < 900000000:
            await bot.send_message(message.chat.id, f'{user_name}, у вас не достаточно средств! {rloser} ',
                                   parse_mode='html')
    if message.text.lower() in ["Купить дом 10", "купить дом 10"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        user_id = msg.from_user.id
        rwin = random.choice(win)
        House = cursor.execute("SELECT House from users where user_id = ?", (message.from_user.id,)).fetchone()
        House = str(House[0])
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        if int(balance) >= 300000000:
            await bot.send_message(message.chat.id,
                                   f'{user_name}, вы успешно купили дом 3-х этажный дом 🏘 за 300.000.000$ {rwin} ',
                                   parse_mode='html')
            cursor.execute(f'UPDATE users SET House = "3-х этажный дом" WHERE user_id = "{user_id}"')
            cursor.execute(f'UPDATE users SET balance = {balance - 300000000} WHERE user_id = "{user_id}"')
            connect.commit()
        if int(balance) < 300000000:
            await bot.send_message(message.chat.id, f'{user_name}, у вас не достаточно средств! {rloser} ',
                                   parse_mode='html')
    if message.text.lower() in ["Купить дом 9", "купить дом 9"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        user_id = msg.from_user.id
        rwin = random.choice(win)
        House = cursor.execute("SELECT House from users where user_id = ?", (message.from_user.id,)).fetchone()
        House = str(House[0])
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        if int(balance) >= 100000000:
            await bot.send_message(message.chat.id,
                                   f'{user_name}, вы успешно купили дом 2-х этажный дом 🏘 за 100.000.000$ {rwin} ',
                                   parse_mode='html')
            cursor.execute(f'UPDATE users SET House = "2-х этажный дом" WHERE user_id = "{user_id}"')
            cursor.execute(f'UPDATE users SET balance = {balance - 100000000} WHERE user_id = "{user_id}"')
            connect.commit()
        if int(balance) < 100000000:
            await bot.send_message(message.chat.id, f'{user_name}, у вас не достаточно средств! {rloser} ',
                                   parse_mode='html')
    if message.text.lower() in ["Купить дом 8", "купить дом 8"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        user_id = msg.from_user.id
        rwin = random.choice(win)
        House = cursor.execute("SELECT House from users where user_id = ?", (message.from_user.id,)).fetchone()
        House = str(House[0])
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        if int(balance) >= 50000000:
            await bot.send_message(message.chat.id,
                                   f'{user_name}, вы успешно купили дом Квартира в центре города 🏢 за 50.000.000$ {rwin} ',
                                   parse_mode='html')
            cursor.execute(f'UPDATE users SET balance = {balance - 50000000} WHERE user_id = "{user_id}"')
            cursor.execute(f'UPDATE users SET House = "Квартира в центре города" WHERE user_id = "{user_id}"')
            connect.commit()
        if int(balance) < 50000000:
            await bot.send_message(message.chat.id, f'{user_name}, у вас не достаточно средств! {rloser} ',
                                   parse_mode='html')
    if message.text.lower() in ["Купить дом 7", "купить дом 7"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        user_id = msg.from_user.id
        rwin = random.choice(win)
        House = cursor.execute("SELECT House from users where user_id = ?", (message.from_user.id,)).fetchone()
        House = str(House[0])
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        if int(balance) >= 15000000:
            await bot.send_message(message.chat.id,
                                   f'{user_name}, вы успешно купили дом Квартира на обочине города 🏢 за 15.000.000$ {rwin} ',
                                   parse_mode='html')
            cursor.execute(f'UPDATE users SET balance = {balance - 15000000} WHERE user_id = "{user_id}"')
            cursor.execute(f'UPDATE users SET House = "Квартира на обочине города" WHERE user_id = "{user_id}"')
            connect.commit()
        if int(balance) < 15000000:
            await bot.send_message(message.chat.id, f'{user_name}, у вас не достаточно средств! {rloser} ',
                                   parse_mode='html')
    if message.text.lower() in ["Купить дом 6", "купить дом 6"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        user_id = msg.from_user.id
        rwin = random.choice(win)
        House = cursor.execute("SELECT House from users where user_id = ?", (message.from_user.id,)).fetchone()
        House = str(House[0])
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        if int(balance) >= 5000000:
            await bot.send_message(message.chat.id,
                                   f'{user_name}, вы успешно купили дом Сельский Домик 🏠 за 5.000.000$ {rwin} ',
                                   parse_mode='html')
            cursor.execute(f'UPDATE users SET balance = {balance - 5000000} WHERE user_id = "{user_id}"')
            cursor.execute(f'UPDATE users SET House = "Сельский Домик" WHERE user_id = "{user_id}"')
            connect.commit()
        if int(balance) < 5000000:
            await bot.send_message(message.chat.id, f'{user_name}, у вас не достаточно средств! {rloser} ',
                                   parse_mode='html')
    if message.text.lower() in ["Купить дом 5", "купить дом 5"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        user_id = msg.from_user.id
        rwin = random.choice(win)
        House = cursor.execute("SELECT House from users where user_id = ?", (message.from_user.id,)).fetchone()
        House = str(House[0])
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        if int(balance) >= 1600000:
            await bot.send_message(message.chat.id,
                                   f'{user_name}, вы успешно купили дом Заброшка 🏚 за 1.600.000$ {rwin} ',
                                   parse_mode='html')
            cursor.execute(f'UPDATE users SET balance = {balance - 1600000} WHERE user_id = "{user_id}"')
            cursor.execute(f'UPDATE users SET House = "Заброшка" WHERE user_id = "{user_id}"')
            connect.commit()
        if int(balance) < 1600000:
            await bot.send_message(message.chat.id, f'{user_name}, у вас не достаточно средств! {rloser} ',
                                   parse_mode='html')
    if message.text.lower() in ["Купить дом 4", "купить дом 4"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        user_id = msg.from_user.id
        rwin = random.choice(win)
        House = cursor.execute("SELECT House from users where user_id = ?", (message.from_user.id,)).fetchone()
        House = str(House[0])
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        if int(balance) >= 800000:
            await bot.send_message(message.chat.id, f'{user_name}, вы успешно купили дом Палатка ⛺ за 800.000$ {rwin} ',
                                   parse_mode='html')
            cursor.execute(f'UPDATE users SET balance = {balance - 800000} WHERE user_id = "{user_id}"')
            cursor.execute(f'UPDATE users SET House = "Палатка" WHERE user_id = "{user_id}"')
            connect.commit()
        if int(balance) < 800000:
            await bot.send_message(message.chat.id, f'{user_name}, у вас не достаточно средств! {rloser} ',
                                   parse_mode='html')
    if message.text.lower() in ["Купить дом 3", "купить дом 3"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        user_id = msg.from_user.id
        rwin = random.choice(win)
        House = cursor.execute("SELECT House from users where user_id = ?", (message.from_user.id,)).fetchone()
        House = str(House[0])
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        if int(balance) >= 400000:
            await bot.send_message(message.chat.id,
                                   f'{user_name}, вы успешно купили дом Халабуда 🛖 за 400.000$ {rwin} ',
                                   parse_mode='html')
            cursor.execute(f'UPDATE users SET balance = {balance - 400000} WHERE user_id = "{user_id}"')
            cursor.execute(f'UPDATE users SET House = "Халабуда" WHERE user_id = "{user_id}"')
            connect.commit()
        if int(balance) < 400000:
            await bot.send_message(message.chat.id, f'{user_name}, у вас не достаточно средств! {rloser} ',
                                   parse_mode='html')
    if message.text.lower() in ["Купить дом 2", "купить дом 2"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        user_id = msg.from_user.id
        rwin = random.choice(win)
        House = cursor.execute("SELECT House from users where user_id = ?", (message.from_user.id,)).fetchone()
        House = str(House[0])
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        if int(balance) >= 200000:
            await bot.send_message(message.chat.id, f'{user_name}, вы успешно купили дом Коробка📦 за 200.000$ {rwin} ',
                                   parse_mode='html')
            cursor.execute(f'UPDATE users SET balance = {balance - 200000} WHERE user_id = "{user_id}"')
            cursor.execute(f'UPDATE users SET House = "Коробка" WHERE user_id = "{user_id}"')
            connect.commit()
        if int(balance) < 200000:
            await bot.send_message(message.chat.id, f'{user_name}, у вас не достаточно средств! {rloser} ',
                                   parse_mode='html')
    if message.text.lower() in ["Купить дом 1", "купить дом 1"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        user_id = msg.from_user.id
        rwin = random.choice(win)
        House = cursor.execute("SELECT House from users where user_id = ?", (message.from_user.id,)).fetchone()
        House = str(House[0])
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        if int(balance) >= 100000:
            await bot.send_message(message.chat.id, f'{user_name}, вы успешно купили дом Канава🤎 за 100.000$ {rwin} ',
                                   parse_mode='html')
            cursor.execute(f'UPDATE users SET balance = {balance - 100000} WHERE user_id = "{user_id}"')
            cursor.execute(f'UPDATE users SET House = "Канава" WHERE user_id = "{user_id}"')
            connect.commit()
        if int(balance) < 100000:
            await bot.send_message(message.chat.id, f'{user_name}, у вас не достаточно средств! {rloser} ',
                                   parse_mode='html')

    if message.text.lower() in ["Дома", "дома"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🏠', '🏡']
        user_id = msg.from_user.id
        rwin = random.choice(win)
        House = cursor.execute("SELECT House from users where user_id = ?", (message.from_user.id,)).fetchone()
        await bot.send_message(message.chat.id,
                               f'{user_name}, Вот список домов для покупки🏡 \n\n🤎 | [1] Канава - 100.000$\n📦 | [2] Коробка - 200.000$\n🛖 | [3] Халабуда - 400.000$\n⛺ | [4] Палатка - 800.000$\n🏚 | [5] Заброшка - 1.600.000$\n🏠 | [6] Cельский Домик - 5.000.000$\n🏢 | [7] Квартира на обочине города - 15.000.000$\n🏢 | [8] Квартира в центре города - 50.000.000$\n🏘 | [9] 2-х этажный дом - 100.000.000$\n🏘 | [10] 3-х этажный дом - 300.000.000$\n🛕 | [11] Особняк - 900.000.000%\n🏰 | [12] Президента Особняк - 2.000.000.000$\n🌑 | [13]Кусочек Луны - 500.000.000.000%\n☄ | [14] Часть Марса - 15.000.000.000.000$ \n\nℹ Для покупки дома введите команду\n"Купить дом [Номер дома]',
                               parse_mode='html')
    if message.text.lower() in ["Дом", "дом"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🏠', '🏡']
        user_id = msg.from_user.id
        rwin = random.choice(win)
        House = cursor.execute("SELECT House from users where user_id = ?", (message.from_user.id,)).fetchone()
        await bot.send_message(message.chat.id,
                               f'{user_name},Вот команды связаные с Домами{rwin}\n\n🏠 Мой дом - Вся информация про ваш дом\n📗Дома - Показует список домов в продаже ',
                               parse_mode='html')
    ###########################################МАГАЗИН##########################################
    if message.text.lower() in ["Магазин", "магазин"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🏬', '🏢']
        rwin = random.choice(win)
        await bot.send_message(message.chat.id,
                               f'{user_name}, добро пожаловать в магазин {config.full_name_bot}{rwin}\n\n🏠 Дом - Узнать всю информацию про покупки домов , и информацию\n🚘 Машина - Узнать всю информацию про покупки Машин , ы информацию\n📱 Телефон - Узнать информацию про покупки Телефонов , и информацию\n🏭 Бизнес - Узнать всю информацию про покупки Бизнесов , и информацию\n📡 Ферма - Узнать всю информацию про покупки Майнинг-Ферм , и информацию',
                               parse_mode='html')
    ###########################################ПРИВИЛЕГИИ#######################################
    if message.text.lower() in ["разработчик", "Разработчик","РАЗРАБОТЧИК"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        await bot.send_message(message.chat.id,
                               f'{user_name},Вот все возможности привилегии РАЗРАБОТЧИК  ✅\n\n1️⃣ | РАЗРАБОТЧИК-БОНУС  ✅\n2️⃣ | ПРЕФИКС В БОТЕ - РАЗРАБОТЧИК  ✅\n3️⃣ | ПРЕФИКС В ОФИЦИАЛЬНОМ ЧАТЕ - РАЗРАБОТЧИК ✅\n4️⃣ | СПОСОБНОСТЬ ВЫДАВАТЬ ДЕНЬГИ БЕЗ ОГРАНИЧЕНИЙ  ✅\n5️⃣ | СПОСОБНОСТЬ ЗАБИРАТЬ ДЕНЬГИ С БАЛАНСА С ОГРАНИЧЕНИЕМ БЕЗ ОГРАНИЧЕНИЙ ✅', parse_mode='html')

    if message.text.lower() in ["спонсор", "Спонсор","СПОНСОР"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        await bot.send_message(message.chat.id,
                               f'{user_name},Вот все возможности привилегии СПОНСОР  🌐\n\n1️⃣ | СПОНСОР-БОНУС  🌐\n2️⃣ | ПРЕФИКС В БОТЕ - СПОНСОР  🌐\n3️⃣ | ПРЕФИКС В ОФИЦИАЛЬНОМ ЧАТЕ - СПОНСОР 🌐\n4️⃣ | СПОСОБНОСТЬ ВЫДАВАТЬ ДЕНЬГИ БЕЗ ОГРАНИЧЕНИЙ 🌐\n5️⃣ | СПОСОБНОСТЬ ЗАБИРАТЬ ДЕНЬГИ С БАЛАНСА С ОГРАНИЧЕНИЕМ БЕЗ ОГРАНИЧЕНИЙ 🌐\n6️⃣ | ДОБОВЛЕНИЕ В ЧАТ АДМИНИСТРАЦИИ 🌐\n7️⃣ | ВЫДАЧА ПРАВА АДМИНИСТРАТОР 6 УРОВНЯ В ОФИЦИАЛЬНОМ ЧАТЕ  🌐\n8️⃣ | СПОСОБНОСТЬ ЗАБИРАТЬ ДЕНЬГИ С БАНКА И КРИПТО-БАЛАНС БЕЗ ОГРАНИЧЕНИЙ🌐\n9️⃣ | СПОСОБНОСТЬ ОБНУЛЯТЬ ПРОФИЛЬ🌐\n1️⃣0️⃣ | СПОСОБНОСТЬ ОБНУЛЯТЬ НЕДВИЖЕМОСТЬ🌐\n1️⃣1️⃣| СПОСОБНОСТЬ УМНОЖАТЬ БАЛАНС ИГРОКОВ  🌐\n🆘ВОЗМОЖНОСТЬ ВЫДАТЬ ИГРОКУ ПРИВИЛЕГИЮ НЕ ВИШЕ ГЛ-АДМИНА🔥\n\n💰 | Стоимость: 500Р', parse_mode='html')

    if message.text.lower() in ["зам", "Зам","ЗАМ"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        await bot.send_message(message.chat.id,
                               f'{user_name},Вот все возможности привилегии ЗАМ  🚫\n\n1️⃣ | ЗАМ-БОНУС  🚫\n2️⃣ | ПРЕФИКС В БОТЕ - ЗАМ  🚫\n3️⃣ | ПРЕФИКС В ОФИЦИАЛЬНОМ ЧАТЕ - ЗАМ 🚫\n4️⃣ | СПОСОБНОСТЬ ВЫДАВАТЬ ДЕНЬГИ🚫\n5️⃣ | СПОСОБНОСТЬ ЗАБИРАТЬ ДЕНЬГИ С БАЛАНСА🚫\n6️⃣ | ДОБОВЛЕНИЕ В ЧАТ АДМИНИСТРАЦИИ 🚫\n7️⃣ | ВЫДАЧА ПРАВА АДМИНИСТРАТОР 5 УРОВНЯ В ОФИЦИАЛЬНОМ ЧАТЕ  🚫\n8️⃣ | СПОСОБНОСТЬ ЗАБИРАТЬ ДЕНЬГИ С БАНКА И КРИПТО-БАЛАНСА 🚫\n9️⃣ | СПОСОБНОСТЬ ОБНУЛЯТЬ ПРОФИЛЬ 🚫\n1️⃣0️⃣ | СПОСОБНОСТЬ УМНОЖАТЬ БАЛАНС ИГРОКОВ🚫\n\n🆘ВОЗМОЖНОСТЬ ВЫДАТЬ ИГРОКУ ПРИВИЛЕГИЮ НЕ ВЫШЕ НЕПОЛНОГО-АДМИНА 🕸\n\n💰 | Стоимость: 350Р', parse_mode='html')

    if message.text.lower() in ["владелец", "Владелец","ВЛАДЕЛЕЦ"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        await bot.send_message(message.chat.id,
                               f'{user_name},Вот все возможности привилегии ВЛАДЕЛЕЦ  🦠\n\n1️⃣ | ВЛАДЕЛЕЦ-БОНУС  🦠\n2️⃣ | ПРЕФИКС В БОТЕ - ВЛАДЕЛЕЦ  🦠\n3️⃣ | ПРЕФИКС В ОФИЦИАЛЬНОМ ЧАТЕ - ВЛАДЕЛЕЦ 🦠\n4️⃣ | СПОСОБНОСТЬ ВЫДАВАТЬ ДЕНЬГИ🦠\n5️⃣ | СПОСОБНОСТЬ ЗАБИРАТЬ ДЕНЬГИ С БАЛАНСА🦠\n6️⃣ | ДОБОВЛЕНИЕ В ЧАТ АДМИНИСТРАЦИИ 🦠\n7️⃣ | ВЫДАЧА ПРАВА АДМИНИСТРАТОР 3 УРОВНЯ В ОФИЦИАЛЬНОМ ЧАТЕ  🦠\n8️⃣ | СПОСОБНОСТЬ ЗАБИРАТЬ ДЕНЬГИ С БАНКА И КРИПТО-БАЛАНСА   🦠\n9️⃣ | СПОСОБНОСТЬ УМНОЖАТЬ БАЛАНС ИГРОКОВ 🦠\n\n🆘ВОЗМОЖНОСТЬ ВЫДАТЬ ИГРОКУ ПРИВИЛЕГИЮ НЕ ВЫШЕ ПРЕМИУМ🦋\n\n💰 | Стоимость: 300Р', parse_mode='html')

    if message.text.lower() in ["создатель", "Создатель","СОЗДАТЕЛЬ"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        await bot.send_message(message.chat.id,
                               f'{user_name},Вот все возможности привилегии СОЗДАТЕЛЬ  🧬\n\n1️⃣ | СОЗДАТЕЛЬ-БОНУС  🧬\n2️⃣ | ПРЕФИКС В БОТЕ - СОЗДАТЕЛЬ  🧬\n3️⃣ | ПРЕФИКС В ОФИЦИАЛЬНОМ ЧАТЕ - СОЗДАТЕЛЬ 🧬\n4️⃣ | СПОСОБНОСТЬ ВЫДАВАТЬ ДЕНЬГИ С ОГРАНИЧЕНИЕМ [ ДО 5КВРД] 🧬\n5️⃣ | СПОСОБНОСТЬ ЗАБИРАТЬ ДЕНЬГИ С БАЛАНСА С ОГРАНИЧЕНИЕМ [ДО 5КВРД] 🧬\n6️⃣ | ДОБОВЛЕНИЕ В ЧАТ АДМИНИСТРАЦИИ 🧬\n7️⃣ | ВЫДАЧА ПРАВА АДМИНИСТРАТОР 2 УРОВНЯ В ОФИЦИАЛЬНОМ ЧАТЕ  🧬\n\n💰 | Стоимость: 200Р', parse_mode='html')

    if message.text.lower() in ["гл-админ", "Гл-админ","ГЛ-АДМИН"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        await bot.send_message(message.chat.id,
                               f'{user_name},Вот все возможности привилегии ГЛ-АДМИН 🔥\n\n1️⃣ | ГЛ-АДМИН-БОНУС 🔥\n2️⃣ | ПРЕФИКС В БОТЕ - ГЛ-АДМИН 🔥\n3️⃣ | ПРЕФИКС В ОФИЦИАЛЬНОМ ЧАТЕ - ГЛ-АДМИН 🔥\n4️⃣ | СПОСОБНОСТЬ ВЫДАВАТЬ ДЕНЬГИ С ОГРАНИЧЕНИЕМ [ДО 300ТРЛН] 🔥\n5️⃣ | СПОСОБНОСТЬ ЗАБИРАТЬ ДЕНЬГИ С БАЛАНСА С ОГРАНИЧЕНИЕМ [ДО 300ТРЛН] 🔥\n6️⃣ | ДОБОВЛЕНИЕ В ЧАТ АДМИНИСТРАЦИИ 🔥\n\n💰 | Стоимость: 125Р', parse_mode='html')
    if message.text.lower() in ["админ", "Админ","АДМИН"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        await bot.send_message(message.chat.id,
                               f'{user_name},Вот все возможности привилегии АДМИН⚡️\n\n1️⃣ | АДМИН-БОНУС ⚡️\n2️⃣ | ПРЕФИКС В БОТЕ - АДМИН ⚡️\n3️⃣ | ПРЕФИКС В ОФИЦИАЛЬНОМ ЧАТЕ - АДМИН⚡️\n4️⃣ | СПОСОБНОСТЬ ВЫДАВАТЬ ДЕНЬГИ С ОГРАНИЧЕНИЕМ [ДО 50ТРЛН] ⚡️\n5️⃣ | СПОСОБНОСТЬ ЗАБИРАТЬ ДЕНЬГИ С БАЛАНСА С ОГРАНИЧЕНИЕМ [ДО 50ТРЛН] ⚡️\n\n💰 | Стоимость: 75Р', parse_mode='html')
    if message.text.lower() in ["неполный админ", "Неполный админ","НЕПОЛНЫЙ АДМИН"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        await bot.send_message(message.chat.id,
                               f'{user_name},Вот все возможности привилегии НЕПОЛНЫЙ АДМИН🕸\n\n1️⃣ | НЕПОЛНЫЙ АДМИН-БОНУС 🕸\n2️⃣ | ПРЕФИКС В БОТЕ - НЕПОЛНЫЙ АДМИН 🕸\n3️⃣ | ПРЕФИКС В ОФИЦИАЛЬНОМ ЧАТЕ - НЕПОЛНЫЙ АДМИН🕸\n4️⃣ | СПОСОБНОСТЬ ВЫДАВАТЬ ДЕНЬГИ С ОГРАНИЧЕНИЕМ [ДО 2ТРЛН] 🕸\n\n💰 | Стоимость: 50Р', parse_mode='html')
    if message.text.lower() in ["Премиум", "премиум","ПРЕМИУМ"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        await bot.send_message(message.chat.id,
                               f'{user_name},Вот все возможности привилегии ПРЕМИУМ🦋\n\n1️⃣ | ПРЕМИУМ-БОНУС 🦋\n2️⃣ | ПРЕФИКС В БОТЕ - ПРЕМИУМ 🦋\n3️⃣ | ПРЕФИКС В ОФИЦИАЛЬНОМ ЧАТЕ - ПРЕМИУМ 🦋\n\n💰 | Стоимость: 30Р', parse_mode='html')
    if message.text.lower() in ["Вип", "вип","ВИП"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        await bot.send_message(message.chat.id,
                               f'{user_name},Вот все возможности привилегии ВИП🐶\n\n1️⃣ | ВИП-БОНУС\n2️⃣ | ПРЕФИКС В БОТЕ - ВИП\n3️⃣ | ПРЕФИКС В ОФИЦИАЛЬНОМ ЧАТЕ - ВИП\n\n💰 | Стоимость: 15Р', parse_mode='html')
    if message.text.lower() in ["Привилегии", "привилегии"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        await bot.send_message(message.chat.id,
                               f'{user_name}, Вот список всех привилегий на {config.full_name_bot}🦾\n\n🐶 | [1] ВИП \n🦋 | [2] ПРЕМИУМ\n🕸 | [3] НЕПОЛНЫЙ-АДМИН\n⚡️ | [4] АДМИН\n🔥 | [5] ГЛ-АДМИН\n🧬 | [6] СОЗДАТЕЛЬ\n🦠 | [7] ВЛАДЕЛЕЦ\n🚫 | [8] ЗАМ\n🌐 | [9] СПОНСОР\n✅ | [10] РАЗРАБОТЧИК\n\n📌Что бы узнать возможность привилегии введите просто её название например:\nℹ️Вип', parse_mode='html')
    ###########################################ШАНС#############################################
    if message.text.lower() in ["Шансы", "шансы"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        rx = random.randint(0,100)
        await bot.send_message(message.chat.id, f'🔮 | {user_name}, шанс этого: {rx}%', parse_mode='html')
    if message.text.lower() in ["Шанс", "шанс"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        await bot.send_message(message.chat.id,f'{user_name}, Вот как правильно пользоваться🔮\n\nℹ️Отвечаем на сообщение командой "Шансы"', parse_mode='html')
      
   ######################################РП КОМАНДЫ#################################################
    if message.text.lower() in ["рп-команды", "РП-команды"]:
       user_name = message.from_user.get_mention(as_html=True)
       await bot.send_message(message.chat.id, f"{user_name}, список РП-команд:\n🤗 | Обнять\n👏 | Похлопать\n👨‍💻 | Заскамить\n☕️ | Пригласить на чай\n👉👌 | Изнасиловать\n🤝 | Взять за руку\n📱 | Подарить айфон\n✋ | Дать пять\n😬 | Укусить\n🤛 | Ударить\n🤲 | Прижать\n💋 | Чмок\n💋 | Поцеловать\n😼 | Кусь\n🤲 | Прижать\n🔪 | Убить\n🤜 | Уебать\n💰 | Украсть\n🔞 | Выебать\n👅 | Отсосать\n👅 | Отлизать\n🔞 | Трахнуть\n🔥 | Сжечь", parse_mode='html')

    if message.text.lower() in ["чмок", "Чмок"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"💋 | {user_name} чмокнул(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["кусь", "Кусь"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"😼 | {user_name} кусьнул(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["обнять", "Обнять"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🤗 | {user_name} обнял(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["поцеловать", "Поцеловать"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"💋 | {user_name} поцеловал(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["дать пять", "Дать пять"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"✋ | {user_name} дал(-а) пять {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["подарить айфон", "Подарить айфон"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"📱 | {user_name} подарил(-а) айфон {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["ударить", "Ударить"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🤛 | {user_name} ударил(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["заскамить", "Заскамить"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"👨‍💻 | {user_name} заскамил(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["прижать", "Прижать"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🤲 | {user_name} прижал(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["укусить", "Укусить"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"😬 | {user_name} укусил(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["взять за руку", "Взять за руку"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🤝 | {user_name} взял(-а) за руку {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["прижать", "Прижать"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🤲 | {user_name} прижал(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["похлопать", "Похлопать"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"👏 | {user_name} похлопал(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["изнасиловать", "Изнасиловать"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"👉👌 | {user_name} изнасиловал(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["пригласить на чай", "Пригласить на чай"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"☕️ | {user_name} пригласил(-а) на чай {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["убить", "Убить"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🔪 | {user_name} убил(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["уебать", "Уебать"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🤜 | {user_name} уебал(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["украсть", "Украсть"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"💰 | {user_name} украл(-а) {reply_user_name}", parse_mode='html')

    if message.text.lower() in ["отсосать", "Отсосать"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"👅 | {user_name} отсосал(-а) {reply_user_name}", parse_mode='html')

    if message.text.lower() in ["отлизать", "Отлизать"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"👅 | {user_name} отлизал(-а) {reply_user_name}", parse_mode='html')

    if message.text.lower() in ["выебать", "Выебать"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🔞 | {user_name} выебал(-а) {reply_user_name}", parse_mode='html')

    if message.text.lower() in ["сжечь", "Сжечь"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🔥 | {user_name} сжёг {reply_user_name}", parse_mode='html')

    if message.text.lower() in ["трахнуть", "Трахнуть"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🔞 | {user_name} трахнул(-а) {reply_user_name}", parse_mode='html')  
    ###########################################ПОМОЩЬ###########################################
    if message.text.lower() in ["Остальное", "остальное"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        await bot.send_message(message.chat.id,
                               f'{user_name}, Остальные команды {rwin}\n⚠️Админ-команды - Команды для админов\n💰Донат - информация по поводу доната в {config.full_name_bot}',
                               parse_mode='html')
    if message.text.lower() in ["Игры", "игры"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        await bot.send_message(message.chat.id,
                               f'{user_name}, игры {config.full_name_bot} {rwin}\n🎰 Казино [ставка]\n🎮 Спин [ставка]\n🎲Чётное|Нечётное [Сумма]',
                               parse_mode='html')
    if message.text.lower() in ["Основные", "основные"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        await bot.send_message(message.chat.id,
                               f'{user_name}, основные команды{rwin}\n📒 Профиль - Показывает всю про вас информацию\n💳 Карта|Банк - вся инфомация связаная с Картой\n💸Б/Баланс - ваш баланс\n💾Крипто - Вся информация связанная с Крипто-Валютой\n🤝 Передать/дать [сумма] - Передача денег\n💡 Магазин - Магазин где вы можете что то купить\n👑Рейтинг - показывает всё связанное с вашим рейтингом\n👑Топ - показывает топ {config.full_name_bot}',
                               parse_mode='html')
    if message.text.lower() in ["развлекательные", "Развлекательные"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        await bot.send_message(message.chat.id,
                               f'{user_name}Вот все развлекательные команды {rwin} \n\n\n🔮 Шанс - Вся информация о дополнение Шанс', parse_mode='html')
    if message.text.lower() in ["помощь", "Помощь"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        await bot.send_message(message.chat.id,
                               f'{user_name} Разделы {rwin} \n\n 1⃣💎Основные\n 2⃣🚀Игры\n 3⃣Остальное\n 4⃣🎉Развлекательные\n 5️⃣ 🛡Привилегии\n ℹ Разработчики бота - {config.owner}',
                               parse_mode='html')

    ###########################################КРИПТО###########################################
    if message.text.startswith("крипто продать"):
        msg = message
        user_id = msg.from_user.id
        user_name = message.from_user.get_mention(as_html=True)
        summ = int(msg.text.split()[2])
        chat_id = message.chat.id
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        cripto = cursor.execute("SELECT cripto from users where user_id = ?", (message.from_user.id,)).fetchone()
        cripto = int(cripto[0])
        cripto2 = '{:,}'.format(summ)
        c = summ * 150000
        c2 = '{:,}'.format(c)
        if summ > 0:
            if int(cripto) >= int(summ):
                await bot.send_message(message.chat.id,
                                       f'{user_name}, вы продали {cripto2}💾 за {c2}$! {rwin}',
                                       parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + c} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET cripto = {cripto - summ} WHERE user_id = "{user_id}"')
                connect.commit()

            if int(cripto) < int(summ):
                await bot.send_message(message.chat.id, f'{user_name}, недостаточно средств! {rloser}',
                                       parse_mode='html')
        if summ <= 0:
            await bot.send_message(message.chat.id, f'{user_name}, нельзя купить отрицательное число! {rloser}',
                                   parse_mode='html')
    if message.text.startswith("Крипто продать"):
        msg = message
        user_id = msg.from_user.id
        user_name = message.from_user.get_mention(as_html=True)
        summ = int(msg.text.split()[2])
        chat_id = message.chat.id
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        cripto = cursor.execute("SELECT cripto from users where user_id = ?", (message.from_user.id,)).fetchone()
        cripto = int(cripto[0])
        cripto2 = '{:,}'.format(summ)
        c = summ * 150000
        c2 = '{:,}'.format(c)
        if summ > 0:
            if int(cripto) >= int(summ):
                await bot.send_message(message.chat.id,
                                       f'{user_name}, вы продали {cripto2}💾 за {c2}$! {rwin}',
                                       parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + c} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET cripto = {cripto - summ} WHERE user_id = "{user_id}"')
                connect.commit()

            if int(cripto) < int(summ):
                await bot.send_message(message.chat.id, f'{user_name}, недостаточно средств! {rloser}',
                                       parse_mode='html')
        if summ <= 0:
            await bot.send_message(message.chat.id, f'{user_name}, нельзя купить отрицательное число! {rloser}',
                                   parse_mode='html')
    if message.text.startswith("крипто купить"):
        msg = message
        user_id = msg.from_user.id
        user_name = message.from_user.get_mention(as_html=True)
        summ = int(msg.text.split()[2])
        chat_id = message.chat.id
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        cripto = cursor.execute("SELECT cripto from users where user_id = ?", (message.from_user.id,)).fetchone()
        cripto = int(cripto[0])
        cripto2 = '{:,}'.format(summ)
        c = summ * 150000
        c2 = '{:,}'.format(c)
        if summ > 0:
            if int(balance) >= int(summ * 150000):
                await bot.send_message(message.chat.id,
                                       f'{user_name}, вы купили {cripto2}💾 за {c2}$! {rwin}',
                                       parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET cripto = {cripto + summ} WHERE user_id = "{user_id}"')
                connect.commit()

            if int(balance) < int(summ * 150000):
                await bot.send_message(message.chat.id, f'{user_name}, недостаточно средств! {rloser}',
                                       parse_mode='html')
        if summ <= 0:
            await bot.send_message(message.chat.id, f'{user_name}, нельзя купить отрицательное число! {rloser}',
                                   parse_mode='html')
    if message.text.startswith("Крипто купить"):
        msg = message
        user_id = msg.from_user.id
        user_name = message.from_user.get_mention(as_html=True)
        summ = int(msg.text.split()[2])
        chat_id = message.chat.id
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        cripto = cursor.execute("SELECT cripto from users where user_id = ?", (message.from_user.id,)).fetchone()
        cripto = int(cripto[0])
        cripto2 = '{:,}'.format(summ)
        c = summ * 150000
        c2 = '{:,}'.format(c)
        if summ > 0:
            if int(balance) >= int(summ * 150000):
                await bot.send_message(message.chat.id,
                                       f'{user_name}, вы купили {cripto2}💾 за {c2}$! {rwin}',
                                       parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET cripto = {cripto + summ} WHERE user_id = "{user_id}"')
                connect.commit()

            if int(balance) < int(summ * 150000):
                await bot.send_message(message.chat.id, f'{user_name}, недостаточно средств! {rloser}',
                                       parse_mode='html')
        if summ <= 0:
            await bot.send_message(message.chat.id, f'{user_name}, нельзя купить отрицательное число! {rloser}',
                                   parse_mode='html')
    if message.text.lower() in ["Крипто", "крипто"]:
        chat_id = message.chat.id
        user_name = message.from_user.get_mention(as_html=True)
        name1 = message.from_user.full_name
        user_id = message.from_user.id
        cripto = cursor.execute("SELECT cripto from users where user_id = ?", (message.from_user.id,)).fetchone()
        cripto = int(cripto[0])
        cripto2 = '{:,}'.format(cripto)
        price = 150000
        price2 = '{:,}'.format(price)
        await bot.send_message(message.chat.id,
                               f'{user_name},Вот информация про КриптоВалюту💾\n\n👤 Владелец: {name1}\n💾 КриптоВалюта: {cripto2}шт\n💡 Цена 1 Крипто-Валюты💾: {price2}$\n\nℹ Команды:\n1️⃣ Крипто купить [Количество] - Для покупки КриптоВалюты\n2️⃣ Крипто продать [Количество] - для продажи КриптоВалюты',
                               parse_mode='html')
    ###########################################ДОНАТ###########################################
    if message.text.lower() in ["донат", "Донат"]:
        await bot.send_message(message.chat.id,
                               f'Вот все разделы по донату💸\n\n1️⃣ | Привилегии\n2️⃣ | Админ чата\n3️⃣ | Деньги\n4️⃣ | Услуги Разработчика\n\n📌Что бы посмотреть информацию про разделы введите их название , пример:\nℹ️Привилегии\n\n✅По поводу покупки обращаться к {config.owner} ‼️', parse_mode='html')
    ###########################################СПИН#############################################
    if message.text.startswith("спин"):
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        balance2 = '{:,}'.format(balance)
        msg = message
        user_id = msg.from_user.id
        chat_id = message.chat.id
        rx = random.randint(0, 105)
        msg = message
        name1 = message.from_user.get_mention(as_html=True)
        name = msg.from_user.last_name
        summ = int(msg.text.split()[1])
        print(f"{name} поставил в спин: {summ} и выиграл/проиграл: {rx}")
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = round(int(balance[0]))
        period = 5
        get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
        last_stavka = f"{int(get[0])}"
        stavkatime = time.time() - float(last_stavka)
        loz = ['💩|👑|👑', '💩|🖕|👑', '💎|🖕|👑', '💎|💣|🍌', '👑|🍌|🖕', '💎|🍓|💣']
        win = ['💎|🍓|🍌', '👑|💎|🍓', '🍓|👑|💎', '💎|🍓|🍌', '💎|🍓|🍓', '🍌|🍌|💎']
        Twin = ['💎|💎|💎', '🍓|🍓|🍓', '👑|👑|👑', '🍌|🍌|🍌']
        smtwin = ['🤯', '🤩', '😵', '🙀']
        smwin = ['🙂', '😋', '😄', '🤑', '😃']
        loser = ['😔', '😕', '😣', '😞', '😢']
        rsmtwin = random.choice(smtwin)
        rsmtwin2 = random.choice(smtwin)
        rtwin = random.choice(Twin)
        rloser = random.choice(loser)
        rloser2 = random.choice(loser)
        rwin = random.choice(win)
        rloz = random.choice(loz)
        rsmwin = random.choice(smwin)
        rsmwin2 = random.choice(smwin)
        if balance >= 999999999999999999999999:
            balance = 999999999999999999999999
            cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
            connect.commit()
            balance2 = '{:,}'.format(balance)
        if stavkatime > period:
            if balance >= summ:
                if summ > 0:
                    if int(rx) in range(80, 100):
                        c = Decimal(summ * 2)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id,
                                               f'{name1}, вот ваши результаты\n——————\n{rwin} - вы выиграли {c2}${rsmwin}\n——————\nПозравляю вас!{rsmwin2}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 2)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return

        if stavkatime > period:
            if balance >= summ:
                if summ > 0:
                    if int(rx) in range(0, 70):
                        c = Decimal(summ * 0)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id,
                                               f'{name1}, вот ваши результаты\n——————\n{rloz} - вы проиграли {c2}${rloser}\n——————\nПриймите мои соболезнования!{rloser2}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 0)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
        if stavkatime > period:
            if balance >= summ:
                if summ > 0:
                    if int(rx) in range(101, 103):
                        c = Decimal(summ * 25)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id,
                                               f'{name1}, вот ваши результаты\n——————\n{rtwin} - ДЖЕКПОТ, ВЫ ВЫИГРАЛИ {c2}${rsmtwin}\n——————\nПОЗДРАВЛЯЮ У ВАС ДЖЕКПОТ!{rsmtwin2}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 25)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                elif summ <= 1:
                    await bot.send_message(chat_id, f'{name1}, нельзя ставить отрицательное число! {rloser}',
                                           parse_mode='html')
            elif int(balance) <= int(summ):
                await bot.send_message(chat_id, f'{name1}, недостаточно средств! {rloser}', parse_mode='html')
        else:
            await bot.send_message(chat_id, f'{name1}, извини. но играть можно только каждые 5️⃣ секунд. {rloser}',
                                   parse_mode='html')
            return
    if message.text.startswith("Спин"):
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        balance2 = '{:,}'.format(balance)
        msg = message
        user_id = msg.from_user.id
        chat_id = message.chat.id
        rx = random.randint(0, 105)
        msg = message
        name1 = message.from_user.get_mention(as_html=True)
        name = msg.from_user.last_name
        summ = int(msg.text.split()[1])
        print(f"{name} поставил в спин: {summ} и выиграл/проиграл: {rx}")
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = round(int(balance[0]))
        period = 5
        get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
        last_stavka = f"{int(get[0])}"
        stavkatime = time.time() - float(last_stavka)
        loz = ['💩|👑|👑', '💩|🖕|👑', '💎|🖕|👑', '💎|💣|🍌', '👑|🍌|🖕', '💎|🍓|💣']
        win = ['💎|🍓|🍌', '👑|💎|🍓', '🍓|👑|💎', '💎|🍓|🍌', '💎|🍓|🍓', '🍌|🍌|💎']
        Twin = ['💎|💎|💎', '🍓|🍓|🍓', '👑|👑|👑', '🍌|🍌|🍌']
        smtwin = ['🤯', '🤩', '😵', '🙀']
        smwin = ['🙂', '😋', '😄', '🤑', '😃']
        loser = ['😔', '😕', '😣', '😞', '😢']
        rsmtwin = random.choice(smtwin)
        rsmtwin2 = random.choice(smtwin)
        rtwin = random.choice(Twin)
        rloser = random.choice(loser)
        rloser2 = random.choice(loser)
        rwin = random.choice(win)
        rloz = random.choice(loz)
        rsmwin = random.choice(smwin)
        rsmwin2 = random.choice(smwin)
        if balance >= 999999999999999999999999:
            balance = 999999999999999999999999
            cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
            connect.commit()
            balance2 = '{:,}'.format(balance)
        if stavkatime > period:
            if balance >= summ:
                if summ > 0:
                    if int(rx) in range(80, 100):
                        c = Decimal(summ * 2)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id,
                                               f'{name1}, вот ваши результаты\n——————\n{rwin} - вы выиграли {c2}${rsmwin}\n——————\nПозравляю вас!{rsmwin2}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 2)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return

        if stavkatime > period:
            if balance >= summ:
                if summ > 0:
                    if int(rx) in range(0, 70):
                        c = Decimal(summ * 0)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id,
                                               f'{name1}, вот ваши результаты\n——————\n{rloz} - вы проиграли {c2}${rloser}\n——————\nПриймите мои соболезнования!{rloser2}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 0)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
        if stavkatime > period:
            if balance >= summ:
                if summ > 0:
                    if int(rx) in range(101, 103):
                        c = Decimal(summ * 25)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id,
                                               f'{name1}, вот ваши результаты\n——————\n{rtwin} - ДЖЕКПОТ, ВЫ ВЫИГРАЛИ {c2}${rsmtwin}\n——————\nПОЗДРАВЛЯЮ У ВАС ДЖЕКПОТ!{rsmtwin2}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 25)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                elif summ <= 1:
                    await bot.send_message(chat_id, f'{name1}, нельзя ставить отрицательное число! {rloser}',
                                           parse_mode='html')
            elif int(balance) <= int(summ):
                await bot.send_message(chat_id, f'{name1}, недостаточно средств! {rloser}', parse_mode='html')
        else:
            await bot.send_message(chat_id, f'{name1}, извини. но играть можно только каждые 5️⃣ секунд. {rloser}',
                                   parse_mode='html')
            return

    ###########################################ЧЁТНОЕ\НЕ ЧЁТНОЕ#################################
    if message.text.startswith("Нечётное"):
        msg = message
        user_id = msg.from_user.id
        chat_id = message.chat.id

        win = ['🙂', '😋', '😄', '😃']
        loser = ['😔', '😕', '😣', '😞', '😢']
        rx = random.randint(0, 120)
        rwin = random.choice(win)
        rwin2 = random.choice(win)
        rloser = random.choice(loser)

        msg = message
        name1 = message.from_user.get_mention(as_html=True)
        name = msg.from_user.last_name
        summ = int(msg.text.split()[1])
        kyb = ['🎲1', '🎲2', '🎲3', '🎲4', '🎲5', '🎲6']
        rkyb = random.choice(kyb)
        print(f"{name} поставил на нечётное: {summ} и выпало: {rkyb}")
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = round(int(balance[0]))
        period = 5
        get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
        last_stavka = f"{int(get[0])}"
        stavkatime = time.time() - float(last_stavka)
        if stavkatime > period:
            if balance >= summ:
                if summ > 0:
                    if rkyb in ['🎲2', '🎲4', '🎲6']:
                        c = Decimal(summ)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1} , вам выпало: {rkyb}\nВы проиграли {c2}$ {rloser}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if rkyb in ['🎲1', '🎲3', '🎲5']:
                        c = Decimal(summ * 2)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1} , вам выпало: {rkyb}\nВы выиграли {c2}$ {rwin}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 2)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                elif summ <= 1:
                    await bot.send_message(chat_id, f'{name1}, нельзя ставить отрицательное число! {rloser}',
                                           parse_mode='html')
            elif int(balance) <= int(summ):
                await bot.send_message(chat_id, f'{name1}, недостаточно средств! {rloser}', parse_mode='html')
        else:
            await bot.send_message(chat_id, f'{name1}, извини. но играть можно только каждые 5️⃣ секунд. {rloser}',
                                   parse_mode='html')
            return
    if message.text.startswith("нечётное"):
        msg = message
        user_id = msg.from_user.id
        chat_id = message.chat.id

        win = ['🙂', '😋', '😄', '😃']
        loser = ['😔', '😕', '😣', '😞', '😢']
        rx = random.randint(0, 120)
        rwin = random.choice(win)
        rwin2 = random.choice(win)
        rloser = random.choice(loser)

        msg = message
        name1 = message.from_user.get_mention(as_html=True)
        name = msg.from_user.last_name
        summ = int(msg.text.split()[1])
        print(f"{name} поставил на нечётное: {summ} и выиграл/проиграл: {rx}")
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = round(int(balance[0]))
        period = 5
        kyb = ['🎲1', '🎲2', '🎲3', '🎲4', '🎲5', '🎲6']
        rkyb = random.choice(kyb)
        get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
        last_stavka = f"{int(get[0])}"
        stavkatime = time.time() - float(last_stavka)
        if stavkatime > period:
            if balance >= summ:
                if summ > 0:
                    if rkyb in ['🎲2', '🎲4', '🎲6']:
                        c = Decimal(summ)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1} , вам выпало: {rkyb}\nВы проиграли {c2}$ {rloser}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if rkyb in ['🎲1', '🎲3', '🎲5']:
                        c = Decimal(summ * 2)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1} , вам выпало: {rkyb}\nВы выиграли {c2}$ {rwin}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 2)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                elif summ <= 1:
                    await bot.send_message(chat_id, f'{name1}, нельзя ставить отрицательное число! {rloser}',
                                           parse_mode='html')
            elif int(balance) <= int(summ):
                await bot.send_message(chat_id, f'{name1}, недостаточно средств! {rloser}', parse_mode='html')
        else:
            await bot.send_message(chat_id, f'{name1}, извини. но играть можно только каждые 5️⃣ секунд. {rloser}',
                                   parse_mode='html')
            return
    if message.text.startswith("чётное"):
        msg = message
        user_id = msg.from_user.id
        chat_id = message.chat.id

        win = ['🙂', '😋', '😄', '😃']
        loser = ['😔', '😕', '😣', '😞', '😢']
        rx = random.randint(0, 120)
        rwin = random.choice(win)
        rwin2 = random.choice(win)
        rloser = random.choice(loser)

        msg = message
        name1 = message.from_user.get_mention(as_html=True)
        name = msg.from_user.last_name
        summ = int(msg.text.split()[1])
        print(f"{name} поставил на Чётное: {summ} и выиграл/проиграл: {rx}")
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = round(int(balance[0]))
        period = 5
        kyb = ['🎲1', '🎲2', '🎲3', '🎲4', '🎲5', '🎲6']
        rkyb = random.choice(kyb)
        get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
        last_stavka = f"{int(get[0])}"
        stavkatime = time.time() - float(last_stavka)
        if stavkatime > period:
            if balance >= summ:
                if summ > 0:
                    if rkyb in ['🎲2', '🎲4', '🎲6']:
                        c = Decimal(summ * 2)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1} , вам выпало: {rkyb}\nВы выиграли {c2}$ {rwin}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 2)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if rkyb in ['🎲1', '🎲3', '🎲5']:
                        c = Decimal(summ)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1} , вам выпало: {rkyb}\nВы проиграли {c2}$ {rloser}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                elif summ <= 1:
                    await bot.send_message(chat_id, f'{name1}, нельзя ставить отрицательное число! {rloser}',
                                           parse_mode='html')
            elif int(balance) <= int(summ):
                await bot.send_message(chat_id, f'{name1}, недостаточно средств! {rloser}', parse_mode='html')
        else:
            await bot.send_message(chat_id, f'{name1}, извини. но играть можно только каждые 5️⃣ секунд. {rloser}',
                                   parse_mode='html')
            return
    if message.text.startswith("Чётное"):
        msg = message
        user_id = msg.from_user.id
        chat_id = message.chat.id

        win = ['🙂', '😋', '😄', '😃']
        loser = ['😔', '😕', '😣', '😞', '😢']
        rx = random.randint(0, 120)
        rwin = random.choice(win)
        rwin2 = random.choice(win)
        rloser = random.choice(loser)

        msg = message
        name1 = message.from_user.get_mention(as_html=True)
        name = msg.from_user.last_name
        summ = int(msg.text.split()[1])
        print(f"{name} поставил на Чётное: {summ} и выиграл/проиграл: {rx}")
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = round(int(balance[0]))
        period = 5
        kyb = ['🎲1', '🎲2', '🎲3', '🎲4', '🎲5', '🎲6']
        rkyb = random.choice(kyb)
        get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
        last_stavka = f"{int(get[0])}"
        stavkatime = time.time() - float(last_stavka)
        if stavkatime > period:
            if balance >= summ:
                if summ > 0:
                    if rkyb in ['🎲2', '🎲4', '🎲6']:
                        c = Decimal(summ * 2)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1} , вам выпало: {rkyb}\nВы выиграли {c2}$ {rwin}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 2)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if rkyb in ['🎲1', '🎲3', '🎲5']:
                        c = Decimal(summ)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1} , вам выпало: {rkyb}\nВы проиграли {c2}$ {rloser}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                elif summ <= 1:
                    await bot.send_message(chat_id, f'{name1}, нельзя ставить отрицательное число! {rloser}',
                                           parse_mode='html')
            elif int(balance) <= int(summ):
                await bot.send_message(chat_id, f'{name1}, недостаточно средств! {rloser}', parse_mode='html')
        else:
            await bot.send_message(chat_id, f'{name1}, извини. но играть можно только каждые 5️⃣ секунд. {rloser}',
                                   parse_mode='html')
            return

    ###########################################КАЗИНО###########################################
    if message.text.startswith("Казино"):
        msg = message
        user_id = msg.from_user.id
        chat_id = message.chat.id

        win = ['🙂', '😋', '😄', '😃']
        loser = ['😔', '😕', '😣', '😞', '😢']
        rx = random.randint(0, 110)
        rwin = random.choice(win)
        rloser = random.choice(loser)

        msg = message
        name1 = message.from_user.get_mention(as_html=True)
        name = msg.from_user.last_name
        summ = int(msg.text.split()[1])
        print(f"{name} поставил в казино: {summ} и выиграл/проиграл: {rx}")
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = round(int(balance[0]))
        period = 5
        get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
        last_stavka = f"{int(get[0])}"
        stavkatime = time.time() - float(last_stavka)
        if stavkatime > period:
            if balance >= summ:
                if summ > 0:
                    if int(rx) in range(0, 15):
                        c = Decimal(summ)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, вы проиграли {c2}$ (x0) {rloser}', parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(16, 33):
                        c = Decimal(summ - summ * 0.25)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, вы проиграли {c2}$ (x0.25) {rloser}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {balance - summ * 0.75} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(34, 54):
                        c = Decimal(summ * 0.5)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, вы проиграли {c2}$ (x0.5) {rloser}',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - summ * 0.5} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(54, 62):
                        c = Decimal(summ - summ * 0.75)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, вы проиграли {c2}$ (x0.75) {rloser}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {balance - summ * 0.25} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(63, 73):
                        c = summ * 1
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, ваши деньги остаются при вас {c2}$ (x1) {rwin}',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(74, 83):
                        c = Decimal(summ * 1.25)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}$ (x1.25) {rwin}', parse_mode='html')

                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 1.25)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(84, 90):
                        c = Decimal(summ * 1.5)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}$ (x1.5) {rwin}', parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 1.5)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(91, 96):
                        c = Decimal(summ * 1.75)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}$ (x1.75) {rwin}', parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 1.75)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(97, 102):
                        c = Decimal(summ * 2)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}$ (x2) {rwin}', parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 2)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(103, 106):
                        c = Decimal(summ * 3)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}$ (x3) {rwin}', parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 3)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) == 110:
                        c = Decimal(summ * 50)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}$ (x50) {rwin}', parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 50)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                    if int(rx) in range(107, 109):
                        c = Decimal(summ * 10)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}$ (x10) {rwin}', parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 10)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                elif summ <= 1:
                    await bot.send_message(chat_id, f'{name1}, нельзя ставить отрицательное число! {rloser}',
                                           parse_mode='html')
            elif int(balance) <= int(summ):
                await bot.send_message(chat_id, f'{name1}, недостаточно средств! {rloser}', parse_mode='html')
        else:
            await bot.send_message(chat_id, f'{name1}, извини. но играть можно только каждые 5️⃣ секунд. {rloser}',
                                   parse_mode='html')
            return

    if message.text.startswith("казино"):
        msg = message
        user_id = msg.from_user.id
        chat_id = message.chat.id

        win = ['🙂', '😋', '😄', '😃']
        loser = ['😔', '😕', '😣', '😞', '😢']
        rx = random.randint(0, 110)
        rwin = random.choice(win)
        rloser = random.choice(loser)

        msg = message
        name1 = message.from_user.get_mention(as_html=True)
        name = msg.from_user.last_name
        summ = int(msg.text.split()[1])
        print(f"{name} поставил в казино: {summ} и выиграл/проиграл: {rx}")
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = round(int(balance[0]))
        period = 5
        get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
        last_stavka = f"{int(get[0])}"
        stavkatime = time.time() - float(last_stavka)
        if stavkatime > period:
            if balance >= summ:
                if summ > 0:
                    if int(rx) in range(0, 15):
                        c = Decimal(summ)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, вы проиграли {c2}$ (x0) {rloser}', parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(16, 33):
                        c = Decimal(summ - summ * 0.25)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, вы проиграли {c2}$ (x0.25) {rloser}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {balance - summ * 0.75} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(34, 54):
                        c = Decimal(summ * 0.5)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, вы проиграли {c2}$ (x0.5) {rloser}',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - summ * 0.5} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(54, 62):
                        c = Decimal(summ - summ * 0.75)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, вы проиграли {c2}$ (x0.75) {rloser}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {balance - summ * 0.25} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(63, 73):
                        c = summ * 1
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, ваши деньги остаются при вас {c2}$ (x1) {rwin}',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(74, 83):
                        c = Decimal(summ * 1.25)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}$ (x1.25) {rwin}', parse_mode='html')

                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 1.25)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(84, 90):
                        c = Decimal(summ * 1.5)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}$ (x1.5) {rwin}', parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 1.5)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(91, 96):
                        c = Decimal(summ * 1.75)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}$ (x1.75) {rwin}', parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 1.75)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(97, 102):
                        c = Decimal(summ * 2)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}$ (x2) {rwin}', parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 2)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(103, 106):
                        c = Decimal(summ * 3)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}$ (x3) {rwin}', parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 3)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) == 110:
                        c = Decimal(summ * 50)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}$ (x50) {rwin}', parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 50)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                    if int(rx) in range(107, 109):
                        c = Decimal(summ * 10)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}$ (x10) {rwin}', parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 10)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                elif summ <= 1:
                    await bot.send_message(chat_id, f'{name1}, нельзя ставить отрицательное число! {rloser}',
                                           parse_mode='html')
            elif int(balance) <= int(summ):
                await bot.send_message(chat_id, f'{name1}, недостаточно средств! {rloser}', parse_mode='html')
        else:
            await bot.send_message(chat_id, f'{name1}, извини. но играть можно только каждые 5️⃣ секунд. {rloser}',
                                   parse_mode='html')
            return

    ###########################################РЕЙТИНГ###########################################
    if message.text.startswith("рейтинг продать"):
        msg = message
        user_id = msg.from_user.id
        user_name = message.from_user.get_mention(as_html=True)
        summ = int(msg.text.split()[2])
        chat_id = message.chat.id
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        rating = cursor.execute("SELECT rating from users where user_id = ?", (message.from_user.id,)).fetchone()
        rating = int(rating[0])
        rating2 = '{:,}'.format(summ)
        c = summ * 10000000000
        c2 = '{:,}'.format(c)
        if summ > 0:
            if int(rating) >= int(summ):
                await bot.send_message(message.chat.id,
                                       f'{user_name}, вы продали {rating2}👑 Рейтинга,  за {c2}$! {rwin}',
                                       parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + c} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET rating = {rating - summ} WHERE user_id = "{user_id}"')
                connect.commit()

            if int(rating) < int(summ):
                await bot.send_message(message.chat.id, f'{user_name}, недостаточно средств! {rloser}',
                                       parse_mode='html')
        if summ <= 0:
            await bot.send_message(message.chat.id, f'{user_name}, нельзя купить отрицательное число! {rloser}',
                                   parse_mode='html')
    if message.text.startswith("Рейтинг продать"):
        msg = message
        user_id = msg.from_user.id
        user_name = message.from_user.get_mention(as_html=True)
        summ = int(msg.text.split()[2])
        chat_id = message.chat.id
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        rating = cursor.execute("SELECT rating from users where user_id = ?", (message.from_user.id,)).fetchone()
        rating = int(rating[0])
        rating2 = '{:,}'.format(summ)
        c = summ * 10000000000
        c2 = '{:,}'.format(c)
        if summ > 0:
            if int(rating) >= int(summ):
                await bot.send_message(message.chat.id,
                                       f'{user_name}, вы продали {rating2}👑 Рейтинга,  за {c2}$! {rwin}',
                                       parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + c} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET rating = {rating - summ} WHERE user_id = "{user_id}"')
                connect.commit()

            if int(rating) < int(summ):
                await bot.send_message(message.chat.id, f'{user_name}, недостаточно средств! {rloser}',
                                       parse_mode='html')
        if summ <= 0:
            await bot.send_message(message.chat.id, f'{user_name}, нельзя купить отрицательное число! {rloser}',
                                   parse_mode='html')
    if message.text.startswith("Рейтинг купить"):
        msg = message
        user_id = msg.from_user.id
        user_name = message.from_user.get_mention(as_html=True)
        summ = int(msg.text.split()[2])
        chat_id = message.chat.id
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        rating = cursor.execute("SELECT rating from users where user_id = ?", (message.from_user.id,)).fetchone()
        rating = int(rating[0])
        rating2 = '{:,}'.format(summ)
        c = summ * 10000000000
        c2 = '{:,}'.format(c)
        if summ > 0:
            if int(balance) >= int(summ * 10000000000):
                await bot.send_message(message.chat.id,
                                       f'{user_name}, вы купили {rating2}👑 Рейтинга,  за {c2}$! {rwin}',
                                       parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET rating = {rating + summ} WHERE user_id = "{user_id}"')
                connect.commit()

            if int(balance) < int(summ * 1000000000000):
                await bot.send_message(message.chat.id, f'{user_name}, недостаточно средств! {rloser}',
                                       parse_mode='html')
        if summ <= 0:
            await bot.send_message(message.chat.id, f'{user_name}, нельзя купить отрицательное число! {rloser}',
                                   parse_mode='html')
    if message.text.lower() in ["рейтинг", "Рейтинг"]:
        chat_id = message.chat.id
        user_name = message.from_user.get_mention(as_html=True)
        name1 = message.from_user.full_name
        user_id = message.from_user.id
        rating = cursor.execute("SELECT rating from users where user_id = ?", (message.from_user.id,)).fetchone()
        rating = int(rating[0])
        rating2 = '{:,}'.format(rating)
        price = 10000000000
        price2 = '{:,}'.format(price)
        await bot.send_message(message.chat.id,
                               f'{user_name},Вот информация про Рейтинг 👑\n\n👤 Владелец: {name1}\n👑 Рейтинг : {rating}👑\n💡 Цена 1 Рейтинга 👑: {price2}$\n\nℹ Команды:\n1️⃣ Рейтинг купить [Количество] - Для покупки Рейтинга 👑\n2️⃣ Рейтинг продать [Количество] - для продажи Рейтинга 👑',
                               parse_mode='html')
    ###########################################ПЕРЕВОДЫ###########################################
    if message.text.startswith("передать"):
        msg = message
        user_id = msg.from_user.id
        name = msg.from_user.last_name
        rname = msg.reply_to_message.from_user.last_name
        user_name = message.from_user.get_mention(as_html=True)
        reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
        reply_user_id = msg.reply_to_message.from_user.id
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)

        perevod = int(msg.text.split()[1])
        perevod2 = '{:,}'.format(perevod)
        print(f"{name} перевел: {perevod} игроку {rname}")

        cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = round(int(balance[0]))
        balance2 = cursor.execute("SELECT balance from users where user_id = ?",
                                  (message.reply_to_message.from_user.id,)).fetchone()
        balance2 = round(balance2[0])

        if not message.reply_to_message:
            await message.reply("Эта команда должна быть ответом на сообщение!")
            return

        if reply_user_id == user_id:
            await message.reply_to_message.reply(f'Вы не можете передать деньги сами себе! {rloser}', parse_mode='html')
            return

        if perevod > 0:
            if balance >= perevod:
                await message.reply_to_message.reply(f'Вы передали {perevod2}$ игроку {reply_user_name} {rwin}',
                                                     parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - perevod} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_user_id}"')
                connect.commit()

            elif int(balance) <= int(perevod):
                await message.reply(f'{user_name}, недостаточно средств! {rloser}', parse_mode='html')

        if perevod <= 0:
            await message.reply(f'{user_name}, нельзя перевести отрицательное число! {rloser}', parse_mode='html')

    if message.text.startswith("Передать"):
        msg = message
        user_id = msg.from_user.id
        name = msg.from_user.last_name
        rname = msg.reply_to_message.from_user.last_name
        user_name = message.from_user.get_mention(as_html=True)
        reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
        reply_user_id = msg.reply_to_message.from_user.id
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)

        perevod = int(msg.text.split()[1])
        perevod2 = '{:,}'.format(perevod)
        print(f"{name} перевел: {perevod} игроку {rname}")

        cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = round(int(balance[0]))
        balance2 = cursor.execute("SELECT balance from users where user_id = ?",
                                  (message.reply_to_message.from_user.id,)).fetchone()
        balance2 = round(balance2[0])

        if not message.reply_to_message:
            await message.reply("Эта команда должна быть ответом на сообщение!")
            return

        if reply_user_id == user_id:
            await message.reply_to_message.reply(f'Вы не можете передать деньги сами себе! {rloser}', parse_mode='html')
            return

        if perevod > 0:
            if balance >= perevod:
                await message.reply_to_message.reply(f'Вы передали {perevod2}$ игроку {reply_user_name} {rwin}',
                                                     parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - perevod} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_user_id}"')
                connect.commit()

            elif int(balance) <= int(perevod):
                await message.reply(f'{user_name}, недостаточно средств! {rloser}', parse_mode='html')

        if perevod <= 0:
            await message.reply(f'{user_name}, нельзя перевести отрицательное число! {rloser}', parse_mode='html')

    if message.text.startswith("дать"):
        msg = message
        user_id = msg.from_user.id
        name = msg.from_user.last_name
        rname = msg.reply_to_message.from_user.last_name
        user_name = message.from_user.get_mention(as_html=True)
        reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
        reply_user_id = msg.reply_to_message.from_user.id
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)

        perevod = int(msg.text.split()[1])
        perevod2 = '{:,}'.format(perevod)
        print(f"{name} перевел: {perevod} игроку {rname}")

        cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = round(int(balance[0]))
        balance2 = cursor.execute("SELECT balance from users where user_id = ?",
                                  (message.reply_to_message.from_user.id,)).fetchone()
        balance2 = round(balance2[0])

        if not message.reply_to_message:
            await message.reply("Эта команда должна быть ответом на сообщение!")
            return

        if reply_user_id == user_id:
            await message.reply_to_message.reply(f'Вы не можете передать деньги сами себе! {rloser}', parse_mode='html')
            return

        if perevod > 0:
            if balance >= perevod:
                await message.reply_to_message.reply(f'Вы передали {perevod2}$ игроку {reply_user_name} {rwin}',
                                                     parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - perevod} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_user_id}"')
                connect.commit()

            elif int(balance) <= int(perevod):
                await message.reply(f'{user_name}, недостаточно средств! {rloser}', parse_mode='html')

        if perevod <= 0:
            await message.reply(f'{user_name}, нельзя перевести отрицательное число! {rloser}', parse_mode='html')

    if message.text.startswith("Дать"):
        msg = message
        user_id = msg.from_user.id
        name = msg.from_user.last_name
        rname = msg.reply_to_message.from_user.last_name
        user_name = message.from_user.get_mention(as_html=True)
        reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
        reply_user_id = msg.reply_to_message.from_user.id
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)

        perevod = int(msg.text.split()[1])
        perevod2 = '{:,}'.format(perevod)
        print(f"{name} перевел: {perevod} игроку {rname}")

        cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = round(int(balance[0]))
        balance2 = cursor.execute("SELECT balance from users where user_id = ?",
                                  (message.reply_to_message.from_user.id,)).fetchone()
        balance2 = round(balance2[0])

        if not message.reply_to_message:
            await message.reply("Эта команда должна быть ответом на сообщение!")
            return

        if reply_user_id == user_id:
            await message.reply_to_message.reply(f'Вы не можете передать деньги сами себе! {rloser}', parse_mode='html')
            return

        if perevod > 0:
            if balance >= perevod:
                await message.reply_to_message.reply(f'Вы передали {perevod2}$ игроку {reply_user_name} {rwin}',
                                                     parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - perevod} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_user_id}"')
                connect.commit()

            elif int(balance) <= int(perevod):
                await message.reply(f'{user_name}, недостаточно средств! {rloser}', parse_mode='html')

        if perevod <= 0:
            await message.reply(f'{user_name}, нельзя перевести отрицательное число! {rloser}', parse_mode='html')

    ###########################################ТОП###########################################
    if message.text.lower() in ["топ", "Топ"]:
        list = cursor.execute(f"SELECT * FROM users ORDER BY rating DESC").fetchmany(10)
        top_list = []
        chat_id = message.chat.id
        name = message.from_user.get_mention(as_html=True)
        num = 0
        for user in list:
            if user[5] >= 999999999999999999999999:
                c6 = 999999999999999999999999
            else:
                c6 = user[5]

            if int(user[1]) < 0:
                balance3 = 0
            if int(user[1]) in range(1000, 999999):
                balance1 = user[1] / 1000
                balance2 = round(balance1)
                balance3 = f'{balance2} тыс'

            if int(user[1]) in range(1000000, 999999999):
                balance1 = user[1] / 1000000
                balance2 = round(balance1)
                balance3 = f'{balance2} млн'

            if int(user[1]) in range(1000000000, 999999999999):
                balance1 = user[1] / 1000000000
                balance2 = round(balance1)
                balance3 = f'{balance2} млрд'

            if int(user[1]) in range(1000000000000, 999999999999999):
                balance1 = user[1] / 1000000000000
                balance2 = round(balance1)
                balance3 = f'{balance2} трлн'

            if int(user[1]) in range(1000000000000000, 999999999999999999):
                balance1 = user[1] / 1000000000000000
                balance2 = round(balance1)
                balance3 = f'{balance2} квдр'

            if int(user[1]) in range(1000000000000000000, 999999999999999999999):
                balance1 = user[1] / 1000000000000000000
                balance2 = round(balance1)
                balance3 = f'{balance2} квнт'

            if int(user[1]) in range(1000000000000000000000, 999999999999999999999999):
                balance1 = user[1] / 1000000000000000000000
                balance2 = round(balance1)
                balance3 = f'{balance2} скст'
            num += 1
            c = Decimal(c6)
            c2 = '{:,}'.format(c)

            top_list.append(f"[{num}]. {user[4]}  — 👑{c2} | ${balance3}")
        top = "\n".join(top_list)
        await bot.send_message(message.chat.id, f"{name}, топ 10 игроков {config.full_name_bot}:\n" + top, parse_mode='html')
