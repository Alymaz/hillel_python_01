#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 17:12:05 2020

@author: alyona
"""
import json
import os


'''У вас есть список(list) IP адрессов. Вам необходимо создать
класс который сможет:
1) Получить и изменить список IP адресов
2) Получить список IP адресов в развернутом виде
(10.11.12.13 -> 13.12.11.10)
3) Получить список IP адресов без первых октетов
(10.11.12.13 -> 11.12.13)
4) Получить список последних октетов IP адресов
(10.11.12.13 -> 13)'''


class IpHandler:
    def __init__(self, ipList):
        self._ipList = ipList

    @property
    def ipList(self):
        print('Loading list of IPs ...')
        return self._ipList

    @ipList.setter
    def ipList(self, newList):
        print('Setting list of IPs to ', newList)
        self._ipList = newList

    def reverse_IP(self):
        print('Loading list of IPs in reversed order...')
        return self._ipList[::-1]

    def get_oct_1_3(self):
        print('Creating IPs without first octets...')
        res = ['.'.join(i.split('.')[1:]) for i in self._ipList]
        return res

    def get_oct_3(self):
        print('Creating last octets of IPs...')
        res = [i.split('.')[-1] for i in self._ipList]
        return res


ip = IpHandler(['10.11.12.13', '10.11.12.14', '10.11.12.15'])
print(ip.ipList)

ip.ipList = ['130.01.12.00', '15.11.55.10', '110.00.12.01']
print(ip.reverse_IP())


'''У вас несколько JSON файлов. В каждом из этих файлов есть
произвольная структура данных. Вам необходимо написать
класс (без реализации конструктора) который будет описывать работу с
этими файлами, а именно:
1) Запись в файл
2) Чтение из файла
3) Получить относительный путь к файлу
4) Получить абсолютный путь к файлу'''

path = '/Users/alyona/Desktop'


class JSONhandler:
    """Handles .json files: read, write, get abs/rel path"""
    def read(self, file):
        with open(file, 'r') as f:
            data = json.load(f)
            return data

    def write(self, input_data, file):
        with open(file, 'w') as f:
            return json.dump(input_data, f, indent=2)

    def get_absolute_path(self, file):
        """Returns absolute path to provided file"""
        current_path = os.path.join(path, file)
        if os.path.exists(current_path):
            return current_path
        else:
            return f'''Path {current_path} does not exist.
                        Enter valid directory.'''

    def get_relative_path(self, file):
        """Returns relative path to provided file"""
        start = os.path.dirname(path)
        rel_path = os.path.relpath(os.path.join(path, file), start)
        if os.path.isfile(os.path.join(path, file)):
            return rel_path
        else:
            return f'{file} have not been found.'


'''Создайте класс который будет хранить параметры для
подключения к физическому юниту (например сервер). В своем
списке атрибутов он должен иметь минимальный набор
(unit_name, mac_address, ip_address, login, password).
Вы должны описать каждый из этих атрибутов в виде гетеров и
сеттеров (@property). У вас должна быть возможность
получения и назначения этих атрибутов в классе.'''


class ConnHandler:
    __slots__ = ['_unit_name', '_mac_address', '_ip_address', '_login',
                 '_password']

    def __init__(self, unit_name='', mac_address='', ip_address='', login='',
                 password=''):
        self._unit_name = unit_name
        self._mac_address = mac_address
        self._ip_address = ip_address
        self._login = login
        self._password = password

    @property
    def unit_name(self):
        return self._unit_name

    @unit_name.setter
    def unit_name(self, unit_name):
        self._unit_name = unit_name

    @property
    def mac_address(self):
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        self._mac_address = mac_address

    @property
    def ip_address(self):
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        self._ip_address = ip_address

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, login):
        self._login = login

    @property
    def password(self):
        return self._password

    @password.setter
    def login(self, password):
        self._password = password


c = ConnHandler()
print(c.__slots__)
c._login = 'alyona123'


'''Создать класс для представления информации о времени. Ваш класс должен иметь
возможности установки времени и изменения его отдельных полей (час, минута,
секунда) с проверкой допустимости вводимых значений. В случае недопустимых
значений полей нужно установить максимально допустимое значение.
Создать методы изменения времени на заданное количество часов, минут и секунд.'''


class Time:
    def __init__(self, h=0, m=0, s=0):
        self.hours = h
        self.minutes = m
        self.seconds = s

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, h):
        if h > 24:
            raise ValueError('Hours must be between 0 and 24')
        self._hours = h

    @property
    def minutes(self):
        return self._minutes

    @minutes.setter
    def minutes(self, m):
        if m > 60:
            raise ValueError('Hours must be between 0 and 24')
        self._minutes = m

    @property
    def seconds(self):
        return self._seconds

    @seconds.setter
    def seconds(self, s):
        if s > 60:
            raise ValueError('Hours must be between 0 and 24')
        self._seconds = s

    def __repr__(self):
        return f'Time({self.hours},{self.minutes},{self.seconds})'

    def __str__(self):
        return f'{self.hours}:{self.minutes}:{self.seconds}'


t1 = Time(13, 30, 45)
print(t1)
print(repr(t1))

'''Создайте класс Student, который содержит атрибуты: фамилия и инициалы, номер
группы, успеваемость (массив из пяти элементов).
Создайте список студентов из десяти элементов (10 экземпляров вашего класса).
Напиши функции:
1. Упорядочить list по возрастанию среднего балла.
2. Вывести фамилии и номера групп студентов, имеющих оценки, равные
только 4 или 5.'''


class Student(object):

    def __init__(self, name, group, grades):
        self.name = name
        self.group = group
        self.grades = grades


def sort_by_avg_mark(s_list):
    res_list = list()
    for obj in s_list:
        avg = sum(obj.grades)/len(obj.grades)
        res_list.append((obj.name, avg))
    res_list.sort(key=lambda x: x[-1])
    return res_list


def get_best_by_mark(s_list):
    #ne poluchilos :((


s_list = [Student('Smith A.', 2, [4, 4, 4, 5, 3]),
          Student('Black J.', 2, [4, 5, 4, 5, 5]),
          Student('Clinton H.', 3, [3, 5, 5, 3, 4]),
          Student('Freeman G.', 1, [5, 5, 4, 5, 5]),
          Student('Smith A.', 3, [4, 4, 4, 4, 4]),
          Student('Gmurman S.', 1, [5, 5, 5, 4]),
          Student('Cook J.', 3, [5, 5, 5, 5, 5]),
          Student('Rorerts A.', 2, [3, 4, 3, 5, 3]),
          Student('Stone L.', 1, [3, 4, 3, 3, 4]),
          Student('Baron B.', 1, [4, 5, 4, 4, 5])]

sort_by_avg_mark(s_list)
