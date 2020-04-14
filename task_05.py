#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 17:11:14 2020

@author: alyona
"""

import os
from datetime import datetime
import shutil


# Напишите функцию копирования файлов. На вход ваша функция принимает два аргумента:
# - путь файла который необходимо скопировать
# - путь каталога куда этот файл необходимо скопировать

def copyFileDir(inFile, outDir):
    """inFile: file to search in current dir;
        outDir: path to where the file should be copied"""
    # my code here
    for file in os.listdir(os.getcwd()):
        file_name = os.path.join(os.getcwd(), inFile)
        if os.path.isfile(file_name):
            return shutil.copy(file_name, outDir)
        else:
            return f"File {inFile} does not exist."


copyFileDir('tasks_01.py', '/Users/alyona')


# Напишите декоратор для превращения функции print в генератор html-тегов
# Декоратор должен принимать список тегов italic, bold, underline

def str_to_html(tags):

    def decorator(func):  # decorator(get_text)
        tag_base = {
            "italic": f"<i>%text%</i>",
            "bold": f"<b>%text%</b>",
            "underline": f"<u>%text%</u>",
        }

        def wrapper(text):
            # my code here
            tags_splitted = {k: v.split('%') for k, v in tag_base.items()}
            new_text = tags_splitted['italic'][0]\
                + tags_splitted['bold'][0] + text\
                + tags_splitted['bold'][-1] + tags_splitted['italic'][-1]
            return new_text
        return wrapper
    return decorator


@str_to_html(["italic", "bold"])
def get_text(text):
    return text


get_text(text='Hello coronavirus')

# Напишите функцию, которая возвращает список файлов из директории.
# Напишите декоратор для этой функции, который прочитает все файлы с
# раширением .log из найденных
path = '/Users/alyona/HILLEL/Advanced_Python'


def log_reading(func):
    def wrapper(*args):
        # my code here
        return func()
    return wrapper


@log_reading
def get_files():
    # my code here
    file_list = list()
    for dirpath, dirnames, filenames in os.walk(path):
        current_path = dirpath
        directories = dirnames
        files = filenames
        for file in files:
            if file.endswith('.log'):
                file_list.append(file)            
    return file_list


get_files()
