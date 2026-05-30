
## 1. fetching name from E-mail using String

while True:
    name = ''
    e_mail = input("Enter E-mail : ")
    for i in e_mail:
        if i == '@':
            break
        else:
            name += i
    print("Name: ", name)
    if input("Stop? (y/n) : ") == 'y':
        break
    
## 2.  fetching name from E-mail using List


while True:
    name = []
    e_mail = input("Enter E-mail : ")
    for i in e_mail:
        if i == '@':
            break
        else:
            name.append(i)
    
    print("Name :", ''.join(name))
   
    if input("Stop? (y/n) : ") == 'y':
        break
    
# 3. Extract domain from email

while True:
    s = input('Enter email: ')
    domain = s.split('@')[1]
    print('Domain:',domain)
    
    if input('Stop? (y/n):').lower() == 'y':
        break
    
    
# 4. Count vowels in a string

count = 0
st = input("Enter string:")
for i in st:
    if i in ['a', 'e', 'i', 'o', 'u']:
        count += 1
print("Total vowel:", count)
        


# 5. Count uppercase and lowercase letters

l, u = 0, 0
i = input('Enter string:')
for j in i:
    if j.isupper():
        u += 1
    elif j.islower():
        l += 1
    else:
        pass
print("Upper:", u)
print("Lower:", l)

# 6. Reverse a string without slicing

st = input("Enter string: ")
rev = ''
for i in st:
    rev = i + rev

print("Reversed string:", rev)


# 7. Remove spaces from string

st = input("Enter string:")

print(st.replace(" ", ''))
        

# 8. Count digits in a string

count = 0
st = input("Enter string:")

for i in st:
    if i.isnumeric():
        count += 1
print("Count number:", count)

# 9. Replace vowels with *

new_lst = ''
st = input ('Enter string:').lower()
for i in st:
    if i in 'aeiou':
        new_lst += '*'
    else:
        new_lst += i
print(new_lst)


# 10. Find duplicate characters in a string

dup =''

st = input("Enter string:").lower()

for i in st:
    if st.count(i) > 1 and i not in dup:
        print(i, end = ' ')
        dup = dup + i
