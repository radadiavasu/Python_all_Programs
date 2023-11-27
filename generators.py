def numbers():
    nums = []
    i = 0
    
    while i < 10:
        nums.append(i)
        # yield i # this "yield" is a generator to store a object memory.
        i += 1
    return nums
print(numbers())

# for i in range(1,11):
#     print(i)