import asyncio
import logging
from aiogram.utils import executor
from aiogram import Bot, Dispatcher, types
from pycoingecko import CoinGeckoAPI
import random
import config as cfg
import markups as nav

logging.basicConfig(level=logging.INFO)

loop = asyncio.new_event_loop()
bot = Bot(token=cfg.TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, loop=loop)
# cg = CoinGeckoAPI()


# @dp.message_handler(commands=['start'])
# async def handle_start(message: types.Message):
#     if message.chat.type == 'private':
#         await bot.send_message(message.from_user.id, 'Привет {0.first_name}'.format(message.from_user), reply_markup=nav.mainMenu)
#
#
# @dp.message_handler()
# async def bot_message(message: types.Message):
#     if message.text == 'Internet Banking':
#         await bot.send_message(message.from_user.id, f"Your number: {random.randint(1000, 9999)}", reply_markup=nav.EBankingMenu)
#
#     elif message.text == 'Main Menu':
#         await bot.send_message(message.from_user.id, 'Main Menu', reply_markup=nav.mainMenu)
#
#     elif message.text == 'Internet Payments':
#         await bot.send_message(message.from_user.id, 'Enternet Payments', reply_markup=nav.EPaymentsMenu)
#
#     elif message.text == 'Money Transfer':
#         await bot.send_message(message.from_user.id, 'Money Transfer Systems', reply_markup=nav.MTransferMenu)
#
#     elif message.text == 'Cash':
#         await bot.send_message(message.from_user.id, 'Money Currencies')
#
#     elif message.text == 'Cryptocurrency':
#         await bot.send_message(message.from_user.id, 'Cryptocurrency', reply_markup=nav.CryptoMenu)
#
#     else:
#         await message.reply('Unknown Command!')


# @dp.message_handler()
# async def bot_msg(message: types.Message):
#     if message.chat.type == 'private':
#         result = cg.get_price(ids=message.text, vs_currencies='usd')
#         await bot.send_message(message.from_user.id,
#                                f"Криптовалюта: {message.text}\nСтоимость на данный момент: {result[message.text]['usd']}$"
#                                )

# @dp.callback_query_handler(text_contains="cc_")
# async def callback_crypto(call: types.CallbackQuery):
#     await bot.delete_message(call.from_user.id, call.message.message_id)
#     callback_data = call.data
#     currency = str(callback_data[3:])
#     result = cg.get_price(ids=currency, vs_currencies='usd')
#     await bot.send_message(call.from_user.id, f"Криптовалюта: {currency}\nСтоимость на данный момент: {result[currency]['usd']}$", reply_markup=nav.crypto_list)


if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dp, loop=loop)
