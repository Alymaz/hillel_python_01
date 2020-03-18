#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 10:52:03 2020

@author: alyona
"""

def count_work_hours(in_time, out_time, rate):
    """
    Функция считает оплату за отработанные часы.
    :in_time int: время начала, в целых часах, например, 8
    :out_time int: время окончания, в целых часах, например, 19
    :rate float: стоимость полного часа
    Возвращает строку вида "57.63 for 9 hours"
    Если количество часов < 8, оплата не считается и равна 0.
    Если количество часов > 8, оплата за каждый сверхурочный час считается по
    полуторному рейту.
    """
    work_time = out_time - in_time
    payment = 0.0
    if work_time <= 8:
        payment = float(work_time * rate)
    elif work_time > 8:
        payment = (work_time * rate) + (work_time - 8) * (rate * 1.5)
    return f"${payment} for {work_time} hours"
count_work_hours(9,18,50)


def plan_trip(dest_list):
    """
    Функция считает стоимость путешествия.
    :destination_list list: список кортежей вида (длительность поездки, город),
    то есть, можно за один вызов посчитать несколько поездок.
    Возвращает цену для каждой поездки (float) списком.
    Стоимость путешествия = прямой перелет + обратный перелет + длительность *
    стоимость отеля.
    Цены:
    1. Получение стоимости отеля в заданном городе (за 1 ночь: Odesa - 33,
    Kyiv - 42, Larnaka - 49, Istanbul - 38);
    2. Получение стоимости перелета в заданный город или обратно (в 1 сторону:
    Odesa - 80, Kyiv - 97, Larnaka - 134, Istanbul - 149).
    """
    result = list()
    prices = {"Kyiv": {"hotel": 42, "flight": 97},
              "Istanbul":{"hotel": 38, "flight": 149}}
    for dest in dest_list:
        trip_days, dest_name = dest
        dest_data = prices[dest_name]
        flight_price = dest_data["flight"] * 2
        hotel_price = dest_data["hotel"] * trip_days
        result.append(hotel_price + flight_price)
    return result

dest_list =[(8,'Kyiv'), (5,'Istanbul')]
plan_trip(dest_list)

# HOME WORK


from datetime import date


data = ({"first_name": "Guido", "last_name": "Van Rossum", \
         "birth": date(1900,2,25), "email": "test@gmail.com"})
           
def validate_first_name(data):
    errors = {}
    if 'first_name' not in data.keys():
        errors.update(KeyError='There is no first name')
    elif len(data['first_name'].strip()) == 0:
        errors.update(ValueError='Empty first name')
    elif len(data['first_name'].strip()) > 48:
        errors.update(ValueError='First name must be less than 48 symbols')
    if errors:
        return False
    return True
first_name = validate_first_name(data)


def validate_last_name(data):
    errors = {}
    if 'last_name' not in data.keys():
        errors.update(KeyError='There is no last name')
    if len(data['last_name'].strip()) == 0:
        errors.update(ValueError='Empty last name')
    if len(data['last_name'].strip()) > 64:
        errors.update(ValueError='Last name must be less than 64 symbols')
    if errors:
        return False
    return True
last_name = validate_last_name(data)


def validate_birth(data):
    errors = {}
    if 'birth' not in data.keys():
        errors.update(KeyError = 'There is no birth.')
    elif not isinstance(data['birth'], date):
        errors.update(ValueError = 'Object must be datetime.date type')
    elif data['birth'] == 0:
        errors.update(ValueError = 'Age value is empty.')
    elif data['birth'] > date.today():
        errors.update(ValueError = 'Age cannot be in the future.')
    elif (date.today().year - data['birth'].year) > 100:
        errors.update(ValueError = 'Age cannot be more than 100.')
    if errors:
        return False
    return True
birth = validate_birth(data)


def validate_email(data):
    errors = {}
    if 'email' not in data.keys():
        errors.update(KeyError='There is no email.')
    elif not isinstance(data['email'],str):
        errors.update(ValueError = 'Object must be str type.')
    elif len(data['email'].split('@')) > 2:
        errors.update(ValueError = 'Symbol @ appears more than once.')
    elif '.' not in data['email'].split('@')[-1]:
        errors.update(ValueError = 'Email should end as .com, .net etc.')
                      
    if errors:
        return False
    return True
email = validate_email(data)


def validate_input(data: tuple) -> bool:
    list_func = [first_name,last_name,birth,email]
    for f in list_func:
        if f is False:
            return False
    return True
validate_input(data)


def handle_error(error_dict) -> None:
    """
    Функция принимает словарь ошибок и проблемных словарей и принтит их.
    Пример:
    ValueError found in:
    {"first_name": {"first_name": 42, "second_name": "Van Rossum"}}
    {"second_name": {"first_name": "Guido", "second_name": 42}}
    """
    pass


def save_to_db(data: list) -> bool:
    """
    Функция принимает кортеж словарей с данными, валидирует каждую запись с
    помощью вспомогательной функции validate_input, и если данные валидны,
    добавляет их в database.
    Возвращает bool по результатам успешного/неуспешного выполнения.
    """
    pass


def select_from_db(field, value):
    """
    Функция возвращает кортеж словарей, где переданное значение встречается в
    переданном ключе.
    """
    pass
