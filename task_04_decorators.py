#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 14:40:31 2020

@author: alyona
"""

# 1. Написать свой cache декоратор c максимальным размером кеша и его очисткой
# при необходимости.

def do_cache(maxsize):          # maxsize = 2
    def decorator(func):        # func = test()
        cache = dict()          # cache = {(v,i): v+i}
        def wrapper(*args):     # args = (v,i)
            if len(cache) >= maxsize:
                # удали самый первый закешированный элемен
                return dict(list(cache.items())[1:])
            if args in cache:
                # вернуть элемент в кеше, не вызывая декорируемой функции
                return cache[args]
            else:
                # Если элемента нет в кеше, нужно вызвать декорируемую функцию,
                # сохранить ее результат в кеш и вернуть ее результат
                result = func(*args)
                cache[args] = result
                return result
        return wrapper
    return decorator


@do_cache(maxsize=2)
def test(v, i):
    return v + i
test(1,3)
test(1,3)
test(2,3)


# 2. Написать свой декоратор который будет проверять остаток от деления числа 100
# на результат работы функции ниже. Если остаток от деления = 0, вывести
# сообщение "We are OK!», иначе «Bad news guys, we got {остаток от деления}».
# Этот декоратор не должен возвращать результат работы функции. Только один из
# указанных принтов.

def div100(func):
    def wrapper(*args):
        # my code here
        return func(*args)
    return wrapper


@div100         # test2 = div100(test2)
def test2(v):
    if v % 100 == 0:
        print('We are OK!')
    elif v%100 != 0:
        print(f'Bad news guys, we got {v%100}.')
test2(225)


# 3. Декоратор должен кэшировать значения аргументов, считать количество
# использований одних и тех же аргументов и печатать их перед исполнением
# декорируемой функции.

def count_args(func):
    cache = dict() # этот дикт будет доступен при следующих вызовах
    cache_count = dict() # этот дикт будет доступен при следующих вызовах
    def wrapper(*args):
        # your code here
    return wrapper