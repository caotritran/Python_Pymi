#!/usr/bin/env python3
import string

data = '''Dictionaries are sometimes found in other languages as “associative memories” or “associative arrays”. Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys, which can be any immutable type; strings and numbers can always be keys. Tuples can be used as keys if they contain only strings, numbers, or tuples; if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key. You can’t use lists as keys, since lists can be modified in place using index assignments, slice assignments.''' # NOQA
#data = '''hoc lap trinh python la hoc ngon ngu va cu phap lap trinh'''

# Chú ý: dấu “ không phải double quotes "

def solve(input_data):
    '''
    Đặt result bằng list chứa 10 tuple ứng với 10 từ xuất hiện nhiều nhất,
    mỗi tuple chứa từ và số lần xuất hiện tương ứng.
    (Nếu có nhiều từ cùng xuất hiện với số lần như nhau thì trả về từ nào
    cũng được).
    '''
    result = []
    dict = {}
    # Xoá dòng raise và Viết code vào đây set result làm kết quả
    input_data = input_data.lower()
    data_1 = string.ascii_lowercase

    data_2 = ''
    for char in input_data:
        if char in data_1 or char == ' ':
            data_2 += char

    for word1 in data_2.split():
        count = 0
        for word2 in input_data.split():
            if word1 == word2:
                count += 1
        dict[word1] = count
    #print(dict)
    ##sap xep list giam dan
    for key in sorted(dict, key=dict.get, reverse=True):
        result.append((key, dict[key]))

    result = result[:10]

    #print(li)



    return result


def main():
    # Đây là một cách làm khác với kiểu dữ liệu có sẵn
    # trong thư viện collections của Python
    #from collections import Counter
    # Regex (re) là một công cụ xử lý string khác so với các method của
    # `str`, linh hoạt nhưng phức tạp, khó đọc, dễ sai.
    #import re
    #cleaned = re.sub(r'“|”|\.|,', ' ', data)
    #c = Counter(cleaned.split())
    #top = c.most_common(5)

    result = solve(data)
    #assert result[:5] == top, (result[:5], top)

    # In ra 10 từ xuất hiện nhiều nhất kèm số lần xuất hiện
    # Viết code in ra màn hình sau dòng này
    print(result)


if __name__ == "__main__":
    main()