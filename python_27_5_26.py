## Case change loop
 
while True:

    name = input('Enter your name : ')
    num = int(input("Enter a number between 1 - 4 : "))

    if num > 4 or num <= 0:
        print("Invalid Number!")

    elif num == 1:
        print(name.upper())

    elif num == 2:
        print(name.lower())

    elif num == 3:
        print(name.capitalize())

    elif num == 4:
        print(name.swapcase())

    if input("Stop? (y/n): ") == 'y':
        break
    
## Calculator

while True:
    op = input('Which operation do you want(+, -, *, /, **, //, %) : ')
    n1 = float(input("Enter first operand : "))
    n2 = float(input("Enter second operand : "))
    if op == '+':
        print(n1 + n2)
    elif op == '-':
        print(n1 - n2)
    elif op == '*':
        print(n1 * n2)
    elif op == '/':
        print(n1 / n2)
    elif op == '//':
        print(n1 // n2)
    elif op == '%':
        print(n1 % n2)
    elif op == '**':
        print(n1 ** n2)
    else:
        print("Invalid Operation!!")
    if input("Stop? (y/n):") == 'y':
        break;
        
## List operation

m = ['Arya', 24, 55.5, 30+2j, True, 'Yes']


# Lenght of list
print(len(m))

#Append
m.append(8.93)
print(m)

# pop
m.pop()
print(m)

# pop(index)
m.pop(3)
print(m)

# Add element in the last / append
m.append(2002)
print(m)

# Add value in a particular index
m.insert(3, 'Paranoid')
print(m)

# Update
m[4] = False
print(m)

# Extend
n = ['Shreya', 25, 2001, True, 'Yes']

m.extend(n)
print(m)

m.append(n)
print(m)

# reverse
m.reverse()
print(m)

# count
m.count("Shreya") # counting Shreya only 1 time bcz counting in main level and not counting in nested level for nested level counting we need to count in loop

# sort()
m.sort()  # TypeError: '<' not supported between instances of 'int' and 'str'

a = [12, 1, 89, 33, 76]
a.sort()
print(a) # [1, 12, 33, 76, 89]

print(a.sort()) # None


## Arithmetic operation in list

a1 = [2, 3, 5, 6]
a2 = [1, 2, 3, 4]

print(a1 + a2) # [2, 3, 5, 6, 1, 2, 3, 4]
print(a1 - a2) # TypeError
print(a1 * a2) # TypeError
print(a1 / a2) # TypeError

# multiplication in list 
print(a1 * 2)


####==============================================================================
### Arithmetic operation in list

a1 = [2, 3, 5, 6]
a2 = [1, 2, 3, 4]

# Addition
print([x + y for x, y in zip(a1, a2)])

# Subtraction
print([x - y for x, y in zip(a1, a2)])

# Multiplication
print([x * y for x, y in zip(a1, a2)])

# Division
print([x / y for x, y in zip(a1, a2)])

####==============================================================================












