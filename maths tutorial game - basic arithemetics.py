#!/usr/bin/env python
# coding: utf-8

# In[6]:


from random import randrange as r

ari_type = input('What type of arithemetic operation would you like to solve? ')

def multiplication():
    question_number = int(input('How many questions would you like to answer? '))
    score = 0
    for question in range(question_number):
        value_a = r(0,100)
        value_b = r(0,100)
        result = value_a * value_b
        user_result = int(input(f' {value_a} X {value_b}'))
        if user_result == result:
            score += 1
    print(f'Thank you for playing! \nYou got {score} out of {question_number} {round(score/question_number*100)}%')

    
def addition():
    question_number = int(input('How many questions would you like to answer? '))
    score = 0
    for question in range(question_number):
        value_a = r(0,100)
        value_b = r(0,100)
        result = value_a + value_b
        user_result = int(input(f' {value_a} + {value_b}'))
        if user_result == result:
            score += 1
    print(f'Thank you for playing! \nYou got {score} out of {question_number} {round(score/question_number*100)}%')

def subtraction():
    question_number = int(input('How many questions would you like to answer? '))
    score = 0
    for question in range(question_number):
        value_a = r(0,100)
        value_b = r(0,100)
        result = value_a - value_b
        user_result = int(input(f' {value_a} - {value_b}'))
        if user_result == result:
            score += 1
    print(f'Thank you for playing! \nYou got {score} out of {question_number} {round(score/question_number*100)}%')

def division():
    question_number = int(input('How many questions would you like to answer? '))
    score = 0
    for question in range(question_number):
        value_a = r(0,100)
        value_b = r(0,100)
        result = value_a/value_b
        user_result = int(input(f' {value_a} / {value_b}'))
        if user_result == result:
            score += 1
    print(f'Thank you for playing! \nYou got {score} out of {question_number} {round(score/question_number*100)}%')
    
if (ari_type == 'Multiplication'):
    print('Muliplication Mode')
    multiplication()
elif (ari_type == 'Addition'):
    print('Addition Mode')
    addition()
elif (ari_type == 'Subtraction'):
    print('Subtraction Mode Activated')
    subtraction()
elif (ari_type == 'Division'):
    print('Division Mode Activated')
    division()
else: 
    print('Sorry, you can only perform Addition, Subtraction, Multiplication and Division with this machine. \nPlease try again!')


# 
