#EC 1st Multiplication table

nums = [1,2,3,4,5,6,7,8,9,10,11,12]
columns = [1,2,3,4,5,6,7,8,9,10,11,12]
column_value = []

for num in nums:
    for column in columns:
        column_value.append(column*num)
    print(*column_value)
    column_value.clear()
