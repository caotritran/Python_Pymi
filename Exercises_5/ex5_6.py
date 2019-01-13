#!/usr/bin/env python3

term1 = {'math': 3, 'python': 5, 'data': 2}
term2 = {'math': 7, 'python': 9, 'SQL': 8, 'HTML': 6}
data = [term1, term2]


def solve(term1, term2):
    '''Trả về result là dict chứa bảng điểm của các môn học sau hai học kỳ.
    Biết điểm số được chọn là điểm số ở lần học sau cùng.
    '''

    result = {}
    hk1 = term1
    hk2 = term2

    # Xoá dòng raise và Viết code vào đây set result làm kết quả
    for key1, value1 in term1.items():
        for key2, value2 in term2.items():
            if key1 == key2:
                if value1 >= value2:
                    result[key1] = value1
                else:
                    result[key1] = value2

    for key, value in result.items():
        hk1.pop(key)
        hk2.pop(key)

    result.update(hk1)
    result.update(hk2)

    return result


def main():
    # Một học viên có bảng điểm học kỳ 1 trong term1
    # Học kỳ 2, học thêm/lại có bảng điểm trong term2

    print(solve(*data))


if __name__ == "__main__":
    main()
