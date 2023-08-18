
fruits = ['apple', 'peach', 'melon', 'grapes']
hetro_list = ['string', 1, 3.4, True, fruits]
#
# print(hetro_list)
# print(fruits[0])
# print(fruits[-3])
# print(hetro_list[-1][-1])
# print("hello world"[3])

# Listのメソッド
print(fruits)
fruits.append('banana')
print(fruits)

fruits.insert(3, 'lemon')
print(fruits)

fruits.remove('peach')
print(fruits)

fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)

print(len(fruits))
print(len("hello world"))