#!/usr/bin/env python3
import random
import string

def solve(N):
    '''Creates a string which contains N random ASCII letters.

    To create 1 letter, use::

      import random
      import string
      random.choice(string.ascii_letters)

    Must: use list comprehension
    Tips: list comprehension always create new list
    '''
    result = []

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    result = [random.choice(string.ascii_letters) for char in range(0, N)]

    return result


def main():
    print(solve(16))


if __name__ == "__main__":
    main()
