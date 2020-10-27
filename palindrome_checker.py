from deque import Deque
import re


def palindrome_checker(word):
    word = "".join(re.findall(r"\w", word.lower()))
    pal_deque = Deque()

    # adds words through the rear
    # add_rear(pushes items forward) -->[r, a, d, a, r]<-- add_front(pushes items backwards)
    # [r]
    # [a, r]
    # [d, a, r]
    # [a, d, a, r]
    # [r, a, d, a, r]
    for w in word:
        pal_deque.add_rear(w)

    still_equal = True
    while pal_deque.size() > 1 and True:
        rear = pal_deque.remove_rear()
        # print(f'rear->{rear}')
        front = pal_deque.remove_front()
        # print(f'front->{front}')

        if rear != front:
            still_equal = False

    return still_equal


mul_palindromes = ["Hours", "My gym", "Go hang a salami - I'm a lasagna hog", "Eva, can I see bees in a cave?", "house"
                   "No lemon, no melon", "I did, did I?", "Don't nod", "Step on no pets", "Red rum, sir, is murder"]
for words in mul_palindromes:
    print(f"{words} is palindrome = '{palindrome_checker(words)}'")


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
