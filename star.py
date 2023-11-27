num = int(input("Enter the number of rows: "))
for i in range(1,num+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
    
# 1.
nums = 5
for i in range(1, (nums+1)):
        print("*" * (i))
                
# Output
# *
# **
# ***
# ****
# *****

# 2.
nums = 5
for i in range(1, (nums+1)):
        print(" " * (nums - i) + "*" * i)
        
# Output
#     *
#    **
#   ***
#  ****
# *****

# 3.
nums = 5
for i in range(nums, 0, -1):
        print(" " * (nums - i) + "*" * i)
        
# Output
# *****
#  ****
#   ***
#    **
#     *