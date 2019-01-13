#!/usr/bin/env python3


def solve(numbers):
    '''Tìm phần tử lớn nhất của list số nguyên `numbers`
    Không sử dụng function `max`, `sorted`
    '''
    assert isinstance(numbers, list)
    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    num_max = numbers[0]
    for number in range(1, len(numbers)):
        if numbers[number] > num_max:
            num_max = numbers[number]
    result = num_max
    return result


def main():
    print(solve([-1, 5, 9, 6, 2, 1]))


if __name__ == "__main__":
    main()
