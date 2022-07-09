from imports import *

connect = sqlite3.connect("users.db")
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS farm(
    user_id INT,
    balance INT,
    farm INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Бизнес(
    Рабочие INT,
    Баланс INT,
    user_id BIGINT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    user_id BIGINT,
    balance INT,
    bank BIGINT,
    cripto INT,
    user_name STRING,
    rating INT,
    user_status STRING,
    House STRING,
    Avto STRING,
    Phone STRING,
    Biz STRING,
    time_register STRING,
    ban_status STRING
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS bot(
    chat_id INT,
    last_stavka INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS mine(
    user_id BIGINT,
    user_name STRING,
    iron INT,
    gold INT,
    diamonds INT,
    amethysts INT,
    aquamarine INT,
    emeralds INT,
    matter INT,
    plasma INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS time_bot(
    user_id BIGINT,
    user_name STRING,
    biz INT,
    farm INT
)
""")



