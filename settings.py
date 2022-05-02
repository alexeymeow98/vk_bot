TOKEN = ''

GROUP_ID = 212973809

INTENTS = [
    {
        'name': 'справка о работе бота',
        'tokens': ['привет', 'как заказать билет', 'хочу заказать билет', 'билет'],
        'scenario': None,
        'answer': 'Чтобы узнать как заказать билет, напишите /help.'

    },
    {
        'name': 'инструкция по работе с ботом',
        'tokens': ['/help'],
        'scenario': None,
        'answer': 'Чтобы заказать билет напиши /ticket и ответь на вопросы бота.'

    },
    {
        'name': 'Заказ билета',
        'tokens': ['Покупка', 'купить билет', '/ticket'],
        'scenario': 'booking_ticket',
        'answer': None
    }
]

SCENARIOS = {
    'booking_ticket': {
        'first_step': 'step1',
        'steps': {
            'step1': {
                'text': 'Введите город отправления, в формате "Москва".',
                'failure_text': 'Проверьте правильнсоть ввода города и попробуйте еще раз.',
                'handler': 'handle_takeoff_city',
                'next_step': 'step2'
            },
            'step2': {
                'text': 'Введите город прибытия, в формате "Санкт-Петербург".',
                'failure_text': 'Проверьте правильнсоть ввода города и попробуйте еще раз.',
                'handler': 'handle_coming_city',
                'next_step': 'step3'
            },
            'step3': {
                'text': 'Введите дату вылета в формате 21-05-2019.',
                'failure_text': 'Проверьте правильность вввода даты и попробуйте еще раз.',
                'handler': 'handle_date',
                'next_step': 'step4'
            },
            'step4': {
                'text': 'Выберите пожалуйста понравившийся рейс и введите его номер.',
                'failure_text': 'В списке нету ввиденоо вами номера.',
                'handler': 'handle_flight',
                'next_step': 'step5'
            },
            'step5': {
                'text': 'Выберите количество мест, от 1 до 5 и введите цифру.',
                'failure_text': 'Введенное вами количество мест недоступно.',
                'handler': 'handle_seats',
                'next_step': 'step6'
            },
            'step6': {
                'text': 'Напишите комментарий к заказу.',
                'failure_text': None,
                'handler': 'handle_wish',
                'next_step': 'step7'
            },
            'step7': {
                'text': 'Верны ли данные, которые вы заполнили ?, наишите Да/Нет',
                'failure_text': None,
                'handler': 'handle_choice',
                'next_step': 'step8'
            },
            'step8': {
                'text': 'Введите номер телефона',
                'failure_text': 'Проверьте правильность вввода номера телефона и попробуйте еще раз.',
                'handler': 'handle_telephone',
                'next_step': 'step9'
            },
            'step9': {
                'text': 'Спасибо за выбор нашего сервиса, с вами свяжутся по введеному вами телефону.',
                'failure_text': None,
                'handler': None,
                'next_step': None

            }

        }

    }
}

DEFAULT_ANSWER = 'Не знаю как ответить на это.' \
                 'Если хочешь узнать как заказать билет, то напиши /help.'
