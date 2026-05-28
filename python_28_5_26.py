# 1. Write a program to count how many vowels are present in a string.

count = 0
s = input("Enter a string : ").lower()
for i in s:
    if i in ['a', 'e', 'i', 'o', 'u']:
        count += 1
print(count)

# 2. Write a program to reverse a list without using reverse().

a = input("Enter string : ")
print(a[::-1])

# 3. Write a program to find the largest element in a list.

ar = []
n = int(input("How many element do you want to enter : "))
for i in range(n):
    num = int(input('Enter elements:'))
    ar.append(num)
print(ar)
print("Largerst element is : ", max(ar))
    

# 4. Write a program to check whether a string is a palindrome or not.

st = input('Enter a string to check palindrom : ')
if st == st[::-1]:
    print("Pandrom!!!!!")
else:
    print("Not Palindrom!!")

# 5. Write a program to remove duplicate elements from a list.

r = list(map(int, input("Enter elements : ").split()))
new_list = []
for i in r:
    if i not in new_list:
        new_list.append(i)
print(new_list)

# OR

r = list(map(int, input("Enter elements : ").split()))    
s1 = set(r)                 ### set() is faster
print(s1)
