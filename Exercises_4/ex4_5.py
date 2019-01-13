#!/usr/bin/env python3


def solve(numbers):
    '''Tính tổng và tích của dãy số `numbers`

    Return một tuple (sum, product)
    Không sử dụng hàm `sum`
    '''
    result = ()
    tong = 0
    tich = 1

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    for i in numbers:
        tong += i
        tich *= i
    result = (tong, tich)

    return result


def main():
    # Cho list numbers chứa các số chẵn từ -10 đến 10, trừ số 0.
    numbers = range(-10, 11, 2)  # step=2
    numbers = list(numbers)
    numbers.remove(0)

    result = solve(numbers)
    print(result)
    assert result == (0, -14745600)


if __name__ == "__main__":
    main()
