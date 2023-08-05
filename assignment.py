# 変数へ代入：assignment

hello = "Hello"
world = "World!!"
print(hello + " " + world)

# pythonの命名はsnake_case
# 文字、数字、_
# Case sensitive

print("hello" + "world")
# ハードコーディングは推奨されていない

print("------------------------")
# format機能
print("hello{}".format("world"))

print("{}{}".format(hello, world))

name = "John"
print("Hey, {}!! How are you doing?".format(name))

balance = 100
print("balance: {}".format(balance))

print("------------------------")
# fstring
print(f"{hello} {world}")

print(f"Hey, {name}!! How are you doing?")
print(f"balance: {balance}")