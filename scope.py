# scope test

# (L)GB
def func(a):
    x = 2
    return a * x
print(func(10))

# L(G)B
x = 2
def func2(a):
    return a * x
print(func2(10))


def func3(a):
    global y
    y = 2
    return a * y

print(func3(10))
print(y)

# 내장 영역(Built-In Scope)
print(dir('__builtins__'))
