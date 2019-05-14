# 함수정의

def dummy():
    pass

def my_function():
    print('Hello Wolrd')

def times(a, b):
    result = a * b
    return result

def none():
    return


dummy()
my_function()
print(times(10, 20))
print(none())

# 함수도 객체다
print(dummy, type(dummy))

f = my_function
f()

def my_function2(func):
    func()

my_function2(f)

print(f, my_function, sep=',')
