# is演算子：同じオブジェクトかどうかを判定
a = 1
b = 1
c = 3
d = a
e = 2 - 1

print(id(a))
print(id(b))
print(id(1))
print(a is b)
print(a is not c)

print(d is a)
print(d is b)

print(a is e)

hello = "hello"
hello2 = "h" + "e" + "l" + "l" + "o"
print(hello, hello2)
print(hello is hello2)
hello = "konnichiwa"
print(hello is hello2)

# Noneかどうかの判定
nothing = None
print(nothing)
print(id(nothing))
print(nothing is None)

