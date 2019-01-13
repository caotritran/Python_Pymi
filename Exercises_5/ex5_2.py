#!/usr/bin/env python3
import copy

'''
Tips: dùng stdlib copy.deepcopy

In [14]: import copy

In [15]: d = [{'name': 'Dung', 'languages': ['C', 'Python']}]

In [16]: dnew = copy.deepcopy(d)

In [18]: dnew[0]['languages'].append('Elixir')

In [19]: dnew
Out[19]: [{'languages': ['C', 'Python', 'Elixir'], 'name': 'Dung'}]

In [20]: d
Out[20]: [{'languages': ['C', 'Python'], 'name': 'Dung'}]
'''

data = [
    {"name": "Hoang",
     "phone": "0988888888",
     "languages": ["Python", "C", "SQL", "HTML", "CSS", "JavaScript",
                   "Golang"],
     },
    {"name": "Duy", "girl_friend": "Maria"},
    {"name": "Dai", "girl_friend": "Angela"},
    {"name": "Tu"},
]


def solve(last_year_data):
    '''
    Trả về list thông tin các học viên sau khi đã update sau 1 năm.
    Không thay đổi thông tin năm cũ.

    Biết các học viên đều học được các ngôn ngữ lập trình
    trong "languages" của học viên "Hoang".
    Sau đó "Hoang" học thêm được ngôn ngữ "Elixir", các học
    viên khác không biết ngôn ngữ này.
    "Tu" có bạn gái tên là "Do Anh".
    "Duy" chia thay bạn gái, không còn bạn gái nữa.
    '''
    result = []

    # Xoá dòng raise và Viết code vào đây set result làm kết quả
    result = copy.deepcopy(last_year_data)
    result[0]['languages'].append('Elixir')
    for language in range(1, len(result)):
        result[language]['languages'] = ["Python", "C", "SQL", "HTML",
                                         "CSS", "JavaScript", "Golang"]
    result[3]['girl_friend'] = 'Do Anh'
    result[1].pop('girl_friend')

    return result


def main():
    # Cho list chứa các dictionary chứa thông tin của các học viên:
    students = data
    # In ra màn hình tên học viên kèm tên bạn gái (nếu có)
    print([students[0]['name']], [students[1]['name'],
                                  students[1]['girl_friend']], [students[2]['name'],
                                                                students[2]['girl_friend']], [students[3]['name']])
    result = solve(students)  # NOQA
    # In ra các thông tin đã thay đổi so với năm trước của mỗi học viên.
    print(result)


if __name__ == "__main__":
    main()
