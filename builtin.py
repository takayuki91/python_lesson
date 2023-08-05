# built in function

# type() データ型を表す
hello_type = type("Hello")
print(hello_type)
print(type("hello"))
print(type(1))

print("---------------------")
# id()　idを表す
hello_id = id("Hello")
print(hello_id)
hello = "Hello"
hello2 = "hello"
print(id(hello))
print(id(hello2))
w = "world"
print(id(w))
print(id("world"))

# オブジェクト