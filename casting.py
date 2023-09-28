# キャスティング casting

# strings '1'
# int 1
# float 1.0
# boolean True, False
# list [1, 2, 3, 4, 5]
# tuple (1, 2, 3)
# dictionary {'a': 1, 'b': 2, 'c': 3}
# set {1, 2, 3, 4, 5}

# 型変換
# str(), int(), float(), list(), bool(), tuple(), set()
print(type(str(1)))
print(type(int('1')))
print(1 + int('1'))
print(str(1) + '1')
print(float(1))
print(list('12345'))
print(bool(1))
print(bool(0))
print(tuple([1, 2, 3, 4, 5]))
print(len(set([1, 2, 3, 1, 2, 3])))
