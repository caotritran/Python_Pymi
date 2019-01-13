#!/usr/bin/env python3

'''
Input: một số nguyên trong range(1,13,1). # start=1, stop=13, step=1
Output: tên tương ứng của tháng đó bằng tiếng Anh, và số ngày trong tháng đó.
Tháng 2 tính 28 ngày.

Ví dụ:

- input_data: 2

- output: February 28
'''


def solve(input_data):
    '''Trả về 1 `tuple` chứa 2 phần tử, ví dụ:

        input_data: 2
        output: ("February", 28)

    :param input_data: tháng bất kì
    :rtype: tuple
    '''
    assert (input_data in range(1, 13, 1)), "Tháng không tồn tại"
    result = ("MONTH", "DATE")

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    if input_data == 1:
        result = ("January", 31)
    elif input_data == 2:
        result = ("February", 28)
    elif input_data == 3:
        result = ("March", 31)
    elif input_data == 4:
        result = ("April", 30)
    elif input_data == 5:
        result = ("May", 31)
    elif input_data == 6:
        result = ("June", 30)
    elif input_data == 7:
        result = ("July", 31)
    elif input_data == 8:
        result = ("August", 31)
    elif input_data == 9:
        result = ("September", 30)
    elif input_data == 10:
        result = ("October", 31)
    elif input_data == 11:
        result = ("November", 30)
    elif input_data == 12:
        result = ("December", 31)

    return result


def main():
    month, day = solve(2)
    print(month, day)


if __name__ == "__main__":
    main()
