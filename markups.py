from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



btnOther = KeyboardButton('Росписание пар')
btnurok = KeyboardButton('Росписание звонков')
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnOther, btnurok)


btnOthe = KeyboardButton('Электрик')
btnuro = KeyboardButton('Повар-Кондитер')
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnOther, btnurok)"btnOther = KeyboardButton('Росписание пар')
btnurok = KeyboardButton('Росписание звонков')
profMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnOthe, btnuro)