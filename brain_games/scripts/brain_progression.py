#!/usr/bin/env python3
import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print("Hello, " + name)
    num_of_iter = 3
    print("What number is missing in the progression?")
    while num_of_iter:
        progression = random.randint(1, 15)
        fst_num_in_lst = random.randint(1, 100)
        last_num_in_lst = fst_num_in_lst + progression * 10
        lst = list(range(fst_num_in_lst, last_num_in_lst, progression))
        index = random.randint(0, 9)
        correct_answer = str(lst[index])
        lst[index] = '..'
        print(' '.join(str(i) for i in lst))
        user_answer = input('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"""'{user_answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'""")
            print(f'Let\'s try again, {name}')
            break
        num_of_iter -= 1
    if num_of_iter == 0:
        print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()
