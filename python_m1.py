print ('hello, world')


### 2. PEP8


## 2.1 Indentation - wciecia

# 4 spaces per indent

#if score <= 100:
# print('Zwyciestwo!') 

#if x > 5:
    print('Hello')
    x=6

# breaking line with paranthesis () or backshash /

    long_string = (
            'This is a very long string'
            'that spans multiple lanes.'
)
    
wyslane = wyslij_wiadomosc(e_mail_odbiorcy, temat,
                           wiadomosc)

def calculate_total(price, quantity, discount):
    return (price*quantity
            -discount)


## 2.2 Empty lines - puste linie


#Separate with two empty lanes - two empty lanes before and after


def top_level_function():
    return 'Hello'


class MyClass:
    def __init__(self):
        pass


def another_top_level_function():
    return 'World'

# Inside a class separate defs with one empty line

def top_level_function():
    return 'hello'


class MyClass:
    def __init__(self):
        pass

    def another_top_level_function():
        return 'World'
    
    def farewell(self):
        print('Goodbye, {self.name}')
              
#Cwiczenie

def get_user():
    return {'name': 'Alice', 'age': 25}


class User:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(f'Hi, {self.name}')


user = User('Bob')
user.greet()

## 2.3 Import organization - orgainzacja importow

# one import per line
import os
import sys

from subprocess import Popen, PIPE

import numpy as np
import requests

from datetime import datetime

pip install isort

