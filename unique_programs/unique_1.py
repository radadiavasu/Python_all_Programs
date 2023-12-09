# (1)
if __name__ == '__main__':
    text = "Hi my name is Vasu"
    
    
    info = {
        "word": (word := text.split()),
        "characters": (chrs := len(''.join(word))),
        "avg_char_per_word": round(chrs / len(word),2)
    }
    
    print(info)
    
# (2)

if __name__ == '__main__':
    name = 'Vasu'
    empty_name = ''
    
    if tempo_name := empty_name or name:
        print(tempo_name)
    

# (3) Calculate even & odd with acending decending without using sort() method.

answers = [1,2,3,4,5]
odd_ans = [ans for ans in answers if ans % 2 != 0]
even_ans = [ans for ans in answers if ans % 2 == 0]

acending_ans = sorted(odd_ans, reverse=False)
decending_ans = sorted(even_ans, reverse=False)

print("Odd Values: ", odd_ans)
print("Even Values: ", even_ans)
print("Odd Acending Values: ", acending_ans)
print("Even Decending Values: ", decending_ans)


# (4) Two ways to remove duplicate elements in the list

# 4.1

list_1 = [1,1,2,2,3,3,4,5,5]

list_2 = set(list_1)

list_3 = list(list_2)

print(list_3)


# 4.2 With using for loops

content = ["a", "b", "a", "c", "b"]

ans = []

for item in content:
    if item not in ans:
        ans.append(item)
        
print(ans)

# 4.3 With using list comprehensions

myset = [1,2,3,3,4,4,5,5]
set_2 = []

set_2 = [x for x in myset if x not in set_2 and not set_2.append(x)]
print(set_2)

# Factorial Number
user = int(input("Enter the value: "))

def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)

if user < 0 ^ user==0:
    print("Enter the value more than 0 and not negative.")
else:
    print("The faactorail number of", user, "is", factorial(user))
    
# Remove strings from list.
def remove_strings(lst):
    result = []
    
    for element in lst:
        if isinstance(element, int) and element >= 0:
            result.append(element)
    return result
    
print(remove_strings([1,2,"vasu",4,5]))