#!/usr/bin/env python3

import os
import json


data = os.path.join(os.path.dirname(__file__), 'salt_contributors.json')


def data_key(datapath):
    '''Trả về list chứa các dictionary chứa data về các contributor bao gồm
    các key: login, html_url và contributions.
    Nếu html_url nào bị thiếu, tạo html_url mới bằng
    "https://github.com/" + login tương ứng.
    '''
    # Sửa function cho phù hợp, trả về kết quả yêu cầu.

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    lst = []
    with open(datapath, 'rt') as f:
        dt = f.read()
    md = json.loads(dt)
    for i in md:
        lst.append({'login': i['login'],
                    'html_url': "https://github.com/" + i['login'],
                    'contributions': i['contributions']})
    return lst


def solve(input_data):
    result = data_key(input_data)

    return result


def main():
    '''Truy cập đường dẫn
    https://api.github.com/repos/saltstack/salt/contributors?page=3 Lưu lại
    thành file salt_contributors.json.
    Sử dụng JSON để chuyển dữ liệu thành dữ liệu trong Python.
    File đã được lưu sẵn trong thư mục này - link để đây để học viên biết
    dữ liệu lấy từ đâu.
    '''
    datafile = data
    li = []
    for d in solve(datafile):
        '''print("User: {} - URL {} - {}".format(d['user'], d['html_url'], d['contributions']))'''
        li.append({"User: {} - URL {} - {}".format(d['login'], d['html_url'], d['contributions'])})
    print(li)


if __name__ == "__main__":
    main()
