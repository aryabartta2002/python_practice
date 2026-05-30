
# 1. Count words in a sentence

st = input("Enter string:")

count = 0

for i in st.split():
    count += 1
    
print(count)

# 2. Find frequency of each character

seen = '' # for not repeate the charecter

st = input("Enter string:").lower()  # a p p l e

for i in st:
    if i not in seen:
        print(i, ":", st.count(i))
        seen += i

## Note: The loop is not counting the characters, it is deciding
##       should I print the frquency for this character or not?

# 3.Convert first character of every word into uppercase

l = input("Enter string:")
print(l.capitalize())

# 4. Remove duplicate characters from string

st = input("Enter string:")
seen = ''

for i in st:
    if i not in seen:
        seen += i
print(seen)

# 5. Find longest word in sentence

st = input("Enter string:")

longest =''

for i in st.split():
    if len(i) > len(longest):
        longest = i

print('Longest word:', longest)

# 6. Find lowest word in sentence



# lowest = ''    -----> in result nothing will come bcz '' is the lowest one

lowest = st.split()[0]

st = input('Enter string:')

for i in st.split():
    if len(i) < len(lowest):
        lowest = i
        
print('Lowest word:', lowest)



#List Questions


# 7. Remove duplicates from list

lst = list(map(int, input("Enter Numbers for list:").split()))

new_lst = []

for i in lst:
    if i not in new_lst:
        new_lst.append(i)
        
print(new_lst)

# 8. Find largest number without max()

lst = list(map(int, input('Enter num:').split()))
# At a time enter your desire list value

mAx = lst[0]

for i in lst:
    if i > mAx:
        mAx = i
        
print('Largest num:', mAx)
    


# 7. Find smallest number without min()

lst = []

n = int(input('Enter how many values you need in list:'))
# At a time do not enter your desire list value

for i in range(n):
    x = int(input("Enter number:"))
    lst.append(x)
    
    
sm = lst[0]

for i in lst:
    if i < sm:
        sm = i

print('Smalest num:', sm)

# 9. Find second largest number

lst = list(map(int, input('Enter num:').split()))

lst.sort(reverse = True)

print('Second largest', lst[1])

# 10. Count even and odd numbers in list

lst = list(map(int, input('Enter num:').split()))
e, o = 0, 0

for i in lst:
    if i % 2 == 0:
        e += 1
    else:
        o += 1
        
print('Even number:', e)
print('Odd number:', o)

# 11. Sum all elements of list without sum()

lst = list(map(int, input("Enter numbers:").split()))

sum = 0

for i in lst:
    sum += i

print('Sum:',sum)


# 12. Merge two lists without +

l1 = [1, 2, 3]
l2 = [4, 5, 6]

for i in l2:
    l1.append(i)
    
print('Merge:', l1)

# 13. Reverse list without slicing

lst = list(map(int, input("Enter numbers: ").split()))
rev = []

for i in range(len(lst)-1, -1, -1):
    rev.append(lst[i])

print("Reversed list:", rev)


# 14. Find common elements in two lists

l1 = list(map(int, input("Enter numbers: ").split()))
l2 = list(map(int, input("Enter numbers: ").split()))

common = []

for i in l2:
    if i in l1:
        common.append(i)
        
print("Common element:", common)


# 15. Separate positive and negative numbers

pos = []
neg = []
z = []

lst = list(map(int, input('Enter positive and negative numbers:').split()))

for i in lst:
    if i > 0:
        pos.append(i)
    elif i < 0:
        neg.append(i)
    else:
        z.append(i)
        
print('Positive:',pos)
print('Negative:',neg)
print("Zeros:",z)

