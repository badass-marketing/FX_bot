from cProfile import label

from aiogram.types import Message, ShippingOption, ShippingQuery, LabeledPrice, PreCheckoutQuery
from aiogram.types.message import ContentType

from messages import MESSAGES
from config import PAYCOM_TOKEN, item_url
from main import dp, bot

PRICES = [
    LabeledPrice(label='Smart Start', amount=100),
    LabeledPrice(label='Start Investor', amount=500),
    LabeledPrice(label='Optima Invest', amount=1000),
    LabeledPrice(label='Premium Start', amount=5000)
]


@dp.message_handler(commands=['start'])
async def start_cmd(message: Message):
    await message.answer(MESSAGES['start'])


@dp.message_handler(commands=['help'])
async def help_cmd(message: Message):
    await message.answer(MESSAGES['help'])


@dp.message_handler(commands=['terms'])
async def terms_cmd(message: Message):
    await message.answer(MESSAGES['terms'])


@dp.message_handler(commands=['buy'])
async def dep_process(message: Message):
    await bot.send_invoice(message.chat.id,
                           title=MESSAGES['item_title'],
                           description=MESSAGES['item_description'],
                           provider_token=PAYCOM_TOKEN,
                           currency='UZS',
                           photo_url=item_url,
                           photo_height=512,
                           photo_width=512,
                           photo_size=512,
                           need_email=True,
                           need_phone_number=True,
                           is_flexible=True,
                           prices=PRICES,
                           start_parameter='example',
                           payload='some_invoice'
                           )


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
