# 인수없이 반환하기

def nothing():
    return

n = nothing()
print(n)

# return문이 없어도 됨
def print_menu():
    print('1. Python')
    print('2. Java')
#    return
    print('3. C')
    print('4. C++')
    print('5. C#')

print_menu()

# 1개의 값을 반환할 때,
def max_value(a, b):
    if a > b:
        return a
    else:
        return b

print(max_value(10, 20))

# 여러 개의 값을 반환할 때
def func():
    return 10, 'hello', {1, 2, 3}, (1, 2, 3)

t = func()
print(t, type(t))

n, s, e, t = func()
print(n, s, e, t)