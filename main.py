from imports import *

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.token)
dp = Dispatcher(bot)

dp.register_message_handler(
    start_handler, commands=['start'], commands_prefix='./?!'
)

dp.register_message_handler(
    commands_handler
)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
    
