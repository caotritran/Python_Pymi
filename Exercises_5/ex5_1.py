#!/usr/bin/env python3


data = {
    'xanh lá': '#3cba54',
    'vàng': '#f4c20d',
    'đỏ': '#db3236',
    'xanh da trời': '#4885ed',
}


def solve(colors):
    '''Ghi ra file index.html code HTML để tạo ra logo của Google với màu sắc
    chính xác.
    Biết cách để tạo chữ G màu xanh da trời dùng code HTML sau::

      <span style="color:#4885ed">G</span>

    Return list chứa các tuple, mỗi tuple  chứa chữ cái trong 'Google' và màu
    của nó.
    Gợi ý: dùng `zip`

        In [1]: list(zip(['xanh', 'do'], ['XXX', 'YYY']))
        Out[1]: [('xanh', 'XXX'), ('do', 'YYY')]
    '''
    result = []

    # Xoá dòng raise và Viết code vào đây set result làm kết quả
    with open('index.html', 'wt') as f:
        f.write('<span style="color:{}">G</span>\n'
                .format(data['xanh da trời']))
        f.write('<span style="color:{}">O</span>\n'
                .format(data['đỏ']))
        f.write('<span style="color:{}">O</span>\n'
                .format(data['vàng']))
        f.write('<span style="color:{}">G</span>\n'
                .format(data['xanh da trời']))
        f.write('<span style="color:{}">L</span>\n'
                .format(data['xanh lá']))
        f.write('<span style="color:{}">E</span>'
                .format(data['đỏ']))

    result = list(zip(['G', 'o', 'o', 'g', 'l', 'e'], [data['xanh da trời'],
                                                       data['đỏ'],data['vàng'], data['xanh da trời'],
                                                       data['xanh lá'], data['đỏ']]))
    return result

def main():
    '''Biết mã hex của các màu trong Google logo là:
    '''
    colors = data
    print(solve(colors))


if __name__ == "__main__":
    main()