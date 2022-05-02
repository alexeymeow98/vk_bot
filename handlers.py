import re

re_city = re.compile(r'^[\w\s\S]{3,25}$')
re_date = re.compile(r'^[\d\W]{8,12}$')
re_number = re.compile(r'^[1-5]{1}$')
re_telephone = re.compile(r'^[\d\S]{10,12}')
re_wish = re.compile(r'^[\w\s\S\W\d]{0,50}$')
re_choice = re.compile(r'^[Yes, yes, Да, да]{2,3}$')


def handle_takeoff_city(text, context):
    match = re.match(re_city, text)
    if match:
        context['takeoff_city'] = text
        return True
    else:
        return False


def handle_coming_city(text, context):
    match = re.match(re_city, text)
    if match:
        context['coming_city'] = text
        return True
    else:
        return False


def handle_date(text, context):
    match = re.match(re_date, text)
    if match:
        context['takeoff_date'] = text
        return True
    else:
        return False


def handle_flight(text, context):
    match = re.match(re_number, text)
    if match:
        context['selected_flight'] = text
        return True
    else:
        return False


def handle_seats(text, context):
    match = re.match(re_number, text)
    if match:
        context['flight_seats'] = text
        return True
    else:
        return False


def handle_wish(text, context):
    match = re.match(re_wish, text)
    if match:
        context['client_wish'] = text
        return True
    else:
        return False


def handle_choice(text, context):
    match = re.match(re_choice, text)
    if match:
        context['client_choice'] = text
        return True
    else:
        return False


def handle_telephone(text, context):
    match = re.match(re_telephone, text)
    if match:
        context['client_phone'] = text
        return True
    else:
        return False
