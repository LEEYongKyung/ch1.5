# 기본 인수값


def incr(a, step=1):
    return a + step


print(incr(10, step=2))
print(incr(10, 2))
print(incr(10))

# 오류
# def decr(step=1, a):
#    return a-step


# 키워드 인수
def area(width, height):
    return width*height


print(area(10, 20))
print(area(width=10, height=20))
print(area(height=20, width=10))
print(area(10, height=20))
# 오류
# print(area(10, width=20))
# print(area(height=10, 20))


# 가변 인수
