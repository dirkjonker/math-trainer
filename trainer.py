#!/usr/bin/env python3

import random
import time


def get_random_numbers(max_num=100):
    a = random.randint(2, max_num)
    b = random.randint(2, max_num)
    return a, b


def random_sum():
    a, b = get_random_numbers()
    e = f'{a} + {b}'
    return e, a + b


def random_mult():
    a, b = get_random_numbers(10)
    e = f'{a} * {b}'
    return e, a * b


functions = (random_sum, random_mult)


def guess():
    """Ask a math question

    On a good answer, returns the number of wrong guesses
    """
    equation, solution = random.choice(functions)()
    wrong = 0
    while True:
        guess = input(f'{equation} = ')
        if not guess.isnumeric():
            print('please enter a number')
            continue
        if int(guess) == solution:
            break
        wrong += 1
        print('wrong!')
    print('right!')
    return wrong


start = time.time()
solved = 0
bad_guesses = 0

while True:
    try:
        bad_guesses += guess()
        solved += 1
    except KeyboardInterrupt:
        end = time.time()
        d = end - start
        print(f'\nequations solved: {solved} ({d / solved:.1f}s per solve)')
        print(f'bad guesses:', bad_guesses)
        break
