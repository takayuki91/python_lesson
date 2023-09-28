# mutable(変更可能)とimmutable（変更不可能）

# mutable・・・list, dict, set
# fruits = ['apple', 'lemon', 'peach']
# print(f"fruitsのIDは{id(fruits)}")
# fruits.append('lemon')
# print(f"fruitsのIDは{id(fruits)}")

# immutable・・・int, float, str, bool, tuple
# fruit = 'apple'
# print(f"fruitのIDは{id(fruit)}")
# fruit += ', lemon'
# print(f"fruitのIDは{id(fruit)}")

# text = ""
# for i in range(1, 11):
#     if i == 1:
#         text += str(i)
#         print(id(text))
#     else:
#         text += '-' + str(i)
#         print(id(text))
# print(text)

# text_list = []
# for i in range(1, 11):
#     text_list.append(str(i))
#     print(id(text_list))
# text = "-".join(text_list)
# print(text)