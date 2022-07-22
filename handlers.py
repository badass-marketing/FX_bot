from cProfile import label

from aiogram.types import Message, ShippingOption, ShippingQuery, LabeledPrice, PreCheckoutQuery
from aiogram.types.message import ContentType

from messages import MESSAGES
from config import PAYCOM_TOKEN, item_url, YKASSA_TOKEN
from main import dp, bot
import markups as nav



PRICE100 = [
    LabeledPrice(label='Beginner', amount=6000*100)
]

PRICE250 = [
    LabeledPrice(label='Beginner', amount=15000*100)
]

PRICE500 = [
    LabeledPrice(label='Beginner', amount=29000*100)
]



START_PRICE = [LabeledPrice(label='Smart Start', amount=100*100)]



@dp.message_handler(commands=['start'])
async def start_cmd(message: Message):
    await message.answer(MESSAGES['start'], reply_markup=nav.mainMenu)


@dp.message_handler(commands=['help'])
async def help_cmd(message: Message):
    await message.answer(MESSAGES['help'])


@dp.message_handler(commands=['terms'])
async def terms_cmd(message: Message):
    await message.answer(MESSAGES['terms'])


@dp.pre_checkout_query_handler(lambda q: True)
async def checkout_process(pre_checkout_query: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: Message):
    await bot.send_message(
        message.chat.id,
        MESSAGES['successful_payment'].format(total_amount=message.successful_payment.total_amount,
                                              currency=message.successful_payment.currency)

    )


@dp.message_handler(text='Main Menu')
async def sales_menu(message: Message):
     await bot.send_message(message.from_user.id, 'Main Menu', reply_markup=nav.mainMenu)
     await bot.delete_message(message.from_user.id, message.message_id)



@dp.message_handler(text='Sales')
async def sales_menu(message: Message):
     await bot.send_message(message.from_user.id, 'Sales Menu', reply_markup=nav.SaleMenu)
     await bot.delete_message(message.from_user.id, message.message_id)


@dp.message_handler(text='Retention')
async def sales_menu(message: Message):
     await bot.send_message(message.from_user.id, 'Retention Menu', reply_markup=nav.retenMenu)
     await bot.delete_message(message.from_user.id, message.message_id)


@dp.message_handler(text='RU')
async def sale_pack(message: Message):
    await bot.send_message(message.from_user.id, 'Please, choose your starting pack.', reply_markup=nav.salePackMenu)


@dp.message_handler(text='RU/Beginner => 100$')
async def ru_dep_process(message: Message):
    await bot.send_invoice(message.chat.id, 
                            title=MESSAGES['item_title100'],
                            description=MESSAGES['item_description'],
                            provider_token=YKASSA_TOKEN,
                            currency='rub',
                            photo_url=item_url,
                            photo_width=512,
                            photo_height=512,
                            photo_size=512,
                            need_email=True,
                            need_phone_number=True,
                            prices=PRICE100,
                            start_parameter='Example',
                            payload='Some_INVOICE'
                            )


@dp.message_handler(text='RU/Smart Start => 250$')
async def ru_dep_process(message: Message):
    await bot.send_invoice(message.chat.id, 
                            title=MESSAGES['item_title250'],
                            description=MESSAGES['item_description'],
                            provider_token=YKASSA_TOKEN,
                            currency='rub',
                            photo_url=item_url,
                            photo_width=512,
                            photo_height=512,
                            photo_size=512,
                            need_email=True,
                            need_phone_number=True,
                            prices=PRICE250,
                            start_parameter='Example',
                            payload='Some_INVOICE'
                            )



@dp.message_handler(text='RU/Smart Trade => 500$')
async def ru_dep_process(message: Message):
    await bot.send_invoice(message.chat.id, 
                            title=MESSAGES['item_title500'],
                            description=MESSAGES['item_description'],
                            provider_token=YKASSA_TOKEN,
                            currency='rub',
                            photo_url=item_url,
                            photo_width=512,
                            photo_height=512,
                            photo_size=512,
                            need_email=True,
                            need_phone_number=True,
                            prices=PRICE500,
                            start_parameter='Example',
                            payload='Some_INVOICE'
                            )


