#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 19:54:17 2020

@author: alyona
"""

def validate_password(password):
       
    def letters_and_digits(password):
        letter_flag = False
        number_flag = False
        for i in password:
            if i.isalpha():
                letter_flag = True
            if i.isnumeric():
                number_flag = True
        return letter_flag and number_flag
    
    def odd_letters(password):
        letter_count=0
        for i in password:
            if i.isalpha():
                letter_count += 1
        if letter_count%2 == 0:
            return True
        else:
            return False

    def even_numbers(password):
        digit_count = 0
        for i in password:
            if i.isdigit():
                digit_count += 1
        if digit_count%2 != 0:
            return True
        else:
            return False

    if letters_and_digits(password) is True and odd_letters(password) is True \
    and even_numbers(password) is True:
        return True
    else:
        return False
    
validate_password('alyona123')


def int_converter(input_int):
    data = [["Decimal", "Octal", "Binary", "Hexadecimal"],[]]
    
    decim_format = format(input_int,'d')
    data[1].append(decim_format)
    
    oct_format = format(input_int,'o')
    data[1].append(oct_format)
    
    bin_format = format(input_int,'b')
    data[1].append(bin_format)
    
    hex_format = format(input_int,'x')
    data[1].append(hex_format)
    
    return data

x = int_converter(87)
y = int_converter(3)
print(x)
print(y)


def print_table(data):
    row1, row2 = data[0], data[1]
    print('-' * 14 * 4)     # upper bound
    print('| ' + ('| '.join(format(i,'12') for i in row1)) + ' |')  # intercell
    print('| ' + ('| '.join(format(j,'12') for j in row2)) + ' |')  # intercell
    print('-' * 14 * 4)     # lower bound

print_table(x)
print_table(y)

    
