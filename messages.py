help_message = '''
В боте собраны самые распространенные платежные системы.\nВсе для твоего удобства и упрощения рабочего процесса.\n\n
Узнать правила можно воспользовавшись командой /terms.
'''

start_message = 'Привет! Здесь ты можешь заводить средства легко и просто.\n' + help_message

terms = '''\
Правила придуманы для того, чтобы их нарушать!\nЛибо мы заберем их деньги и отдадим ЗСУ, либо их деньги станут ракетами которые летят в наши города!\n\nЗвони заводи орков, не трать время!!!
'''

item_title100 = 'Beginner Pack'
item_title250 = 'Smart Start Pack'
item_title500 = 'Smart Investor Pack'
item_description = '''\
Стартовый пакет активации торгового счета.\nПосле подтверждения оплаты с Вами свяжется финансовый аналитик по указанному в платеже номеру.\nУдачной торговли с TradeFX24.net
'''

AU_error = '''\
В данную страну доставка не оформляется. Сорри
'''

successful_payment = '''
Платеж на сумму `{total_amount} {currency}` совершен успешно!
'''


MESSAGES = {
    'start': start_message,
    'help': help_message,
    'terms': terms,
    'item_title100': item_title100,
    'item_title250': item_title250,
    'item_title500': item_title500,
    'item_description': item_description,
    'AU_error': AU_error,
    'successful_payment': successful_payment,
}