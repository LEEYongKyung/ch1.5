# call by reference 이지만
# 내부에서 변경하더라도 변경되지 않는다(immutable)
def f(i):
    i = 20
a = 10;
f(a)
print(a)

def f2(seq):
    seq[0] = 0

# list는 mutable 이므로 함수내에서 수정가능
a = [1, 2, 3]
f2(a)
print(a)

# tuple은 immutable 이므로 함수내에서 수정 불가능
# a = (1, 2, 3)
# f2(a)

