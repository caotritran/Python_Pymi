#!/usr/bin/env python3

NUMBER_OF_LINES = 30000000
#NUMBER_OF_LINES = 10


def solve(output_path):
    '''Tạo ra 1 file chứa 30 triệu dòng, các dòng lẻ chứa 30 số 1,
    các dòng chẵn chứa giá trị 2 * số dòng hiện tại.

    Sau khi tạo xong file, return result là list chứa 10 dòng cuối theo thứ tự
    dòng xuất hiện trước đứng trước.

    Chú ý: 30 triệu dòng.
    '''
    result = []
    # Xoá dòng raise và Viết code vào đây set result làm kết quả
    with open('file.txt', 'wt') as f:
        for NUM in range(1, NUMBER_OF_LINES+1):
            if NUM % 2 == 0:
                f.write('{}\n'.format(NUM * 2))
            else:
                f.write('{}\n'.format('1' * 30))
    with open('file.txt', 'rt') as f:
        data = f.readlines()
        result = list(data[-10:])
    import os
    # Xoá file sau khi đã xong vì file này rất lớn
    try:
        os.remove(output_path)
    except OSError as e:
        print(e)

    return result


def main():
    import tempfile
    # tên _ hàm ý rằng ta sẽ không dùng giá trị của nó - convention
    _, output_path = tempfile.mkstemp()
    print('File to write: {0}'.format(output_path))
    for line in solve(output_path):
        print(line.rstrip())


if __name__ == "__main__":
    main()