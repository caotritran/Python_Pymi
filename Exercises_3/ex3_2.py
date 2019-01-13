#!/usr/bin/env python3

data = '''
Come to the
River
Of my
Soulful
Sentiments
Meandering silently
Yearning for release.
Hasten
Earnestly
As my love flows by
Rushing through the flood-gates
To your heart.
'''


# https://www.poetrysoup.com/poem/cross_my_heart_609765

def solve(text):
    '''Trả về tiêu đề bài thơ ghép từ các chữ cái đầu tiên của mỗi dòng.
    Chỉ viết hoa chữ cái đầu tiên.
    '''
    result = ''

    # Xoá dòng raise và Viết code vào đây set result làm kết quả
    result = text.strip().split('\n')
    s = ''
    for i in range(0, (len(result))):
        s = s + result[i][0]
    s = s.capitalize()
    result = s

    return result


def main():
    '''
    Cross my heart là một bài thơ thuộc thể loại "acrostic".
    Khi ghép các chữ cái HOẶC các từ đầu tiên lại với nhau thu được một
    thông điệp
    '''
    text = data
    print(solve(text))


if __name__ == "__main__":
    main()
