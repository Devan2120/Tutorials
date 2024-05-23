## stringmethods

# # user input gmail (username@gmail.com), give username
# t = int(input("No of gmails"))
# for i in range(t):
#     mail = input()
#     index = mail.index('@')
#     username = mail[:index]
#     print(username)

# name = input("Enter your Name")
# place = input("Enter your Country")
# job = input("Enter your Job")

# print(f"Welcome, {name}, {job}, from {place}")

# str1 = 'HolLYwOod'
# str2 = ""
# for char in str1:
#     if char.islower():
#         str2 += char.upper()
#     else:
#         str2 += char.lower()

# print(str2)


# #print(lst[-2:-6:-1])
# # rev_lst = list()
# # for i in range(len(lst)):
# #     rev_lst.append(lst[-(i+1)])
# lst.reverse()
# print(lst)

# lst = [1,[2,3,4]]
# print(lst[1][1])

# lst[4] = 'str'
# print(lst)

# lst[1:5] = [['str']]
# print(lst)

# print(4 in lst)

## list fn
# lst = [1,7,44,67,-56,123,-45]
# char = ["We", "are", "HAPPy","TODAY", "now"]
# char.sort(reverse = True, key = str.lower)
# print(char)
# print(lst)
# print(lst)

## list comprehension
#a = [i for i in 'hollywood']
# a = [int(i) for i in input("Enter the  Nos: \n").split(",")]
# print(a)

# a = int(input("Enter the no of Numbers:"))
# t = list()
# for i in range(a):
#     t.append(int(input()))

# print(t)

# a = [i**2 if i % 2 == 0 else i for i in range(21) ]
# print(a)

# # sum of first n nos using while loop
# n = int(input("Enter the value of n: "))
# sum = 0
# i = n
# while i >0:
#     sum += i
#     i -= 1
# print(f"Sum of {n} nos = {sum}")

# # program to find factorial using while loop
# no = int(input("Enter the no: "))
# fact = 1
# i = n
# while i >1:
#     fact *= i
#     i -= 1
# print(f"Factorial of {no} = {fact}")

# # length of last word in a string
# st = input("Enter a string: ")
# word = st.split()[-1]
# print(f"Length of last word in- {st} = {len(word)}")

# # input = [1,2,3] output = [1,2,4] input = [1,2,9] output = [1,3,0]
# n1 = [1,2,3]
# n2 = [1,2,9]
def digits(n):
    n1 = str(n)
    n2 = [int(i) for i in n1]
    return n2
# N1 = digits(int("".join([str(i) for i in n1])) + 1)
# N2 = digits(int("".join([str(i) for i in n2])) + 1)
# print(f"input = {n1}, output = {N1}")
# print(f"input = {n2}, output = {N2}")


# # user input -- sum of digits
# num = int(input("Enter the Number: "))
# print(f"Sum of digits of {num} = {sum(digits(num))}")

# #user input -- leap year
# year = int(input("Enter the year: "))
# if year % 4 == 0:
#     print(f"{year} is a Leap year")
# else:
#     print(f"{year} is not a leap year")

# check if a no is armstrong or not
nu = int(input("Enter the number: "))
sum_digits = sum([i**(len(str(nu))) for i in digits(nu)])
if nu == sum_digits:
    print(f"{nu} is an armstrong no")
else:
    print(f"{nu} is not an armstrong no")

