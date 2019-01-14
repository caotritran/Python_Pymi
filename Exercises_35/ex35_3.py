#!/usr/bin/env python3


def solve(N):
    '''Creates a list which contains N first even integers. ``[2, 4 ...]``
    Must: use list comprehension
    Tips: list comprehension always create new list
    '''
    result = []
    nums = 0
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    for i in range(N):
        nums += 2
        result.append(nums)
    return result


def main():
    print(solve(6))


if __name__ == "__main__":
    main()
