#!/usr/bin/env python3


def solve(N):
    '''Create a list which contains N lists,
    each list contains N numbers from 0->N-1.

    E.g with N = 10:

    matrix = [
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
      ...
      ...
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ]

    Then returns a string looks like below

      0********0
      *1******1*
      **2****2**
      ***3**3***
      ****44****
      ****55****
      ***6**6***
      **7****7**
      *8******8*
      9********9
    '''

    result = []
    m = 0
    n = 10
    ss = ''

    for i in range(N):
        for j in range(N):
            if j == i or j == N - 1 - i:
                result.append(str(i))
            else:
                result.append('*')
    result = ''.join(result)
    for k in range(10):
        ss += result[m:n] + '\n'
        m += 10
        n += 10
    result = ss.strip()
    return result
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp

def main():
    print(solve(10))


if __name__ == "__main__":
    main()
