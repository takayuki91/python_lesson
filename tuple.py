# tuple(タプル)：変更できないリスト

date_of_birth = (1990, 2, 3)
# date_of_birth = [1990, 2, 3]
# date_of_birth[0] = 2000
# date_of_birth[0] = 2000 これはできない
print(date_of_birth)

year, month, date = date_of_birth
print(year)
print(month)
print(date)
