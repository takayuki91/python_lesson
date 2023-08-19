
even = [2, 4, 6, 8, 10, 12]

print(even[1:4])
# 基本は[開始:未満]

print(even[0:4])
print(even[:4])
# 0 は省略可

print(even[3:5])
print(even[3:-1])

print(even[3:])

print(even[:])

text = "hello world"
print(text[3:])

# [開始:未満:step]
print(text[2:10:2])
# 2〜10未満を2stepで
print(text[::-1])
# 全部を逆順