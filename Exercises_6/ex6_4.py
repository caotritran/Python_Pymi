#!/usr/bin/env python3


def sumall(input_data):
    '''Viết function ``sumall`` tính tổng của tất cả các argument (int, float,
    hoặc string) được gọi. Thay input_data bằng code phù hợp.
    '''
    sum_arg = 0
    for i in range(len(input_data)):
        sum_arg += float(input_data[i])
    return sum_arg


def solve():
    input_data1 = [1, 2, 3, 4.5, 5, ' 6 ']
    input_data2 = [1, 2, 3, 4.5, 5, 9, ' 6 ']
    result = sumall(input_data1)
    result2 = sumall(input_data2)

    return result, result2


def main():
    print(solve())


if __name__ == "__main__":
    main()
