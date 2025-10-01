#EC 1st for loops

nums = [4,654,136,84,651,86,42,1,564,3,4894]

for num in nums:
    num /= 2
    if num > 100:
        print(f"{num} i only half of {num*2}. It is a large number")
    else:
        print(num)

print("the loop is over!")

for num in range(1,11,2):
    print(num)