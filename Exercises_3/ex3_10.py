#!/usr/bin/env python3

data = (
    [1, 5, 2, 3, 4],
    [4, 5, 0, 4]
)


def solve(list1, list2):
    '''Find common elements of two given lists.

    Returns a list contains those elements.
    Require: use only lists, if/else and for loops.
    '''
    result = []
    li = []

    # Xoá dòng raise và Viết code vào đây set result làm kết quả
    for i in range(0, len(list1)):
        for x in range(0, len(list2)):
            if list1[i] == list2[x]:
                li.append(list1[i])

    n = li[0]
    for y in range(1, len(li)):
        if n != li[y]:
            n = li[y]
        else:
            li.remove(li[y])
    result = li
    return result


def main():
    L1, L2 = data
    print(solve(L1, L2))


if __name__ == "__main__":
    main()
