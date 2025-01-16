# words = ["pay","attention","practice","attend"]; pref = "at" # output: 2
# words = ["leetcode","win","loops","success"]; pref = "code" # output: 0
# words = ["lewsmb","lewrydnve","lewqqm","lewec","lewn","lewb","lewedb"]; pref = "lew" # output: 7

# n = len(pref)
# for i in words:
#     if pref == i[0:1]:
#         print(len(i[0:1]))
#     else:
#         print(0)
# print(len(i[0:2]))


# 1. Using built in modules

# count = 0
# for i in words:
#     if i.startswith(pref):
#         count += 1
# print(count)


# 2. With slicing technique.

# count= 0
# a = len(pref)
# for i in words:
#     if i[:a] in i:
#         count += 1
# print(count)


####################################

# words1 = ["amazon","apple","facebook","google","leetcode"]; words2 = ["e","o"]
# words1 = ["amazon","apple","facebook","google","leetcode"]; words2 = ["e","oo"]
# words1 = ["amazon","apple","facebook","google","leetcode"]; words2 = ["lo","eo"]
# words1 = ["amazon","apple","facebook","google","leetcode"]; words2 = ["lo","eo"]
# words1 = ["amazon","apple","facebook","google","leetcode"]; words2 = ["l","e"]


# store = []

# for i in words1:
#     if (all(s in i for s in words2)):
#     # if all(all(k in i for k in s)for s in words2):
#         store.append(i)
# print(store)


# -----------------------------------------
# Find first, second or third largest value
# -----------------------------------------

# First

# n = [10, 20, 30, 40, 45, 99]

# first = float('-inf')

# for i in n:
#     if i > first:
#         first = i
# print(first)


# Second

# n = [20, 10, 70, 50, 45, 99]
# first = min(n)
# second = 0

# for i in n: 
#     if i > first:
#         second = first
#         first = i
# print(second)


# Third

# n = [20, 10, 70, 50, 45, 99]

# first = second = third = float('-inf')

# for i in n:
#     if i > first:
#         third = second
#         second = first
#         first = i

#     elif i > second and i != first:
#         third = second
#         second = i

#     elif i > third and i != second:
#         third = i
# print(third)


# -------------
# Counting freq.
# -------------

# With using built in method.

# from collections import Counter

# s = [1,1,2,3,4,5,5,5,5,6,7,8,9,8,9]

# d = dict(Counter(s))


# With using dict.

# s = [1,1,2,3,4,5,5,5,5,6,7,8,9,8,9]

# d = {}

# for i in s:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)


# With using list

# s = [1,1,2,3,4,5,5,5,5,6,7,8,9,8,9]

# for i in s:
#     d[i] = d.get(i, 0) + 1
# print(d)


# ----------------------
# Simple To-Do in Python.
# ----------------------

# class TODO:
#     def __init__(self):
#         self.datas = []

#     def add_tasks(self, data):
#         self.datas.append(data)

#     def remove_taskes(self, data):
#         if data in self.datas:
#             self.datas.remove(data)

#     def view_tasks(self):
#         return self.datas

# obj = TODO()
# obj.add_tasks("First task")
# obj.add_tasks("Second task")
# obj.remove_taskes("Second task")
# print(obj.view_tasks())


# -----------------------
# Checking for Palindrome
# -----------------------

# s = "ama"

# l = []

# if s == s[::-1]:
#     l.append(s)
#     print(l)
# else:
#     print("Given string is not palindrome")


# -----------------------------------------
# Extract specific column with dict of list
# -----------------------------------------

# dicts = [{'name': 'Alice', 'age': 25},
# {'name': 'Bob', 'age': 20}, 
# {'name': 'Charlie', 'age': 23}]

# s = [s['name'] for s in dicts] # Name
# x = [s['age'] for s in dicts] # Age

# print(s, x)


# ---------
# Fibonacci
# ---------

# First

# n = 10

# a,b = 0,1
# while a < n:
#     print(a, end=" ")
#     a,b = b, a+b


# Second

# n = 10
# a,b = 0,1

# print(a,b, end=" ")
# for _ in range(2, n):
#     c = a+b
#     a = b
#     b = c
#     print(c, end=" ")
# print()

# Third

# nooooo = [0, 1]
# def fibo(n):
#     if n < 0:
#         print("Values must be greater than 0")
#     elif n < len(nooooo):
#         return nooooo
#     else:
#         nooooo.append(fibo(n - 1) + fibo(n - 2))
#         # return n
    
# print(fibo(10))


# Fourth

# n = int(input("Enter number: "))

# temp = n

# p = [0, 1]

# for i in range(1, temp+1):
#     p.append(p[-1] + p[-2])
# print(p)


# ----------------
# Factorial number
# ----------------

# Using Recursion

# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fact(n-1)
# print(fact(5)) # 1! * 2! * 3! * 4! * 5! = 120


# Using Dynamic Programming(Memorization)

# fact_num = {}

# def fact(n):
#     if n in fact_num:
#         return fact_num[n]
#     elif n == 0 or n == 1:
#         fact_num[n] = 1
#     else:
#         fact_num[n] = n * fact(n-1)
#     return fact_num[n]

# print(fact(5))


# ----------------------------
# Add Digits with target value
# ----------------------------

# n = [10,20,30,40,50,60]

# target = 60

# for i in range(len(n)):
#     for j in range(len(n)):
#         if n[i] + n[j] == target:
#             print(f"{n[i]} + {n[j]} = {n[i]+n[j]}")


# --------------------
# Prime number or not.
# --------------------
"""A number is divisible of 1 and only with itself is prime number."""
# n = 12

# if n <= 1:
#     print(False)

# for i in range(2, n):
#     if n % i == 0:
#         print(False)
# print(True)


# ----------------
# Leap year or not
# ----------------

# n = 2025

# if n % 400 == 0:
#     print(True)
# elif n % 100 == 0:
#     print(False)
# elif n % 4 == 0:
#     print(True)
# else:
#     print(False)


# In one line.

# n = 1900

# print((n % 4 == 0 and n % 100 != 0) or n % 400 == 0)


# ----------------
# Armstrong number
# ----------------

# n = 153

# p = str(n)
# l = len(p)

# # ans = sum(int(d)**l for d in p)
# ans = sum(pow(int(d), l) for d in p) # With pow()

# print(ans == n)


