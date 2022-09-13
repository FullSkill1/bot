import asyncio
import logging
from aiogram import Bot, Dispatcher, types
import markups as nav

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="5566593785:AAH4Eg0RwwPRTh3yWQh_cJGKcVHR7fV3IJQ")
# Диспетчер
dp = Dispatcher(bot)

# Хэндлер на команду /start
@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await bot.send_message(message.from_user.id, "Привет, я помогу тебе в Колледже(Украина, обл. Херсонская г.Геническ). Что вам нужно?", reply_markup = nav.profMenu)


@dp.message_handler()
async def urok(message: types.Message):
	if message.text == 'Росписание звонков':
		await bot.send_message(message.from_user.id, '1.8:00-9:10 2.9:20-10:30 3.10:40-11:50 4.12:00-13:10')
	elif message.text == 'Росписание пар':
		await bot.send_message(message.from_user.id, '1- Украинська литература.\n2-электро техника.\n3-Летература.\n4-документальное обеспечения свар робот')



@dp.message_handler()
async def Elektrik(message: types.Message):
	if message.text == 'Электрик':
		await bot.send_message(message.from_user.id, 'Отличная профессия, что вам нужно?', reply_markup = nav.mainMenu)
)
	elif message.text == 'Повар-Кондитер':
		await bot.send_message(message.from_user.id, 'В разроботке')




# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
