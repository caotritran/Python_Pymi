#!/usr/bin/env python3

import string


def solve(words):
    '''Trả về list chứa điểm tương ứng của các từ trong `words`

    Nếu a b c d (không phân biệt chữ hoa thường) .... lần lượt bằng 1 2 3 4 ...
    thì từ ``attitude`` có giá trị bằng 100.
    (http://www.familug.org/2015/05/golang-tinh-tu-cung-9gag.html)

    Gợi ý::

      import string
      print(string.ascii_lowercase)
    '''
    result = []
    li = []
    tong = 0

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    for word in enumerate(string.ascii_lowercase, start=1):
        index, char = word
        li.append([index, char])

    for s in words:
        for w in s:
            w = w.lower()
            for i, c in li:
                if w == c:
                    tong += i
        result.append(tong)
        tong = 0

    return result


def main():
    words = ['numpy', 'django', 'saltstack', 'discipline',
             'Python', 'FAMILUG', 'pymi']

    print(solve(words))


if __name__ == "__main__":
    main()
