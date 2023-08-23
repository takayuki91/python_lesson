fruits = ['apple', 'peach', 'grapes', 'banana']

print('apple' in fruits)
print('lemon' in fruits)
print('lemon' not in fruits)

favorite = input("好きなフルーツは何ですか？")

if favorite in fruits:
    print("{}ですね、差し上げますよ".format(favorite))
    fruits.remove(favorite)
else:
    print("{}ですね、仕入れますよ".format(favorite))
    fruits.append(favorite)

print("今あるフルーツはこちらです！{}".format(fruits))