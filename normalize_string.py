# 문자열 데이터를 분석하기 전에 처리함수 만들기
# 1. 공백제거
# 2. 필요없는 문장 부호 제거
# 3. 대소문자 정리하기 title 처리
import re

states = ['Alabama', ' Georgia!#?!', 'Georgia ', 'georgia', 'FlOrIda', 'south carolina   ', 'West virginia?']

def clean_strings(strings):
    results = []
    for s in strings:
        s = s.strip()
        s = re.sub('[!#?]', '', s)
        s = s.title()
        results.append(s)

    return results


result = clean_strings(states)
print(result)


def clean_strings2(strings, *funcs):
    results = []
    for s in strings:
        for func in funcs:
            s = func(s)

        results.append(s)

    return results


# def remove_specialchar(s):
#    return re.sub('[!#?]', '', s)
# print((lambda s: re.sub('[!#?]', '', s))("abc#4!!!!!def"))
# print((lambda s: re.sub('[!#?]', '', s) )("abc"))
# result = (lambda a, b: a*b)(10, 20)
# a, b -> a * b

result = clean_strings2(states, str.strip, str.title, lambda s: re.sub('[!#?]', '', s))
print(result)