from aiogram import Bot, Dispatcher, executor, types
from config import token

bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text="Shopping")
    keyboard.add(button_1)
    await message.answer("Введи артикул товара и я покажу цены", reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp)