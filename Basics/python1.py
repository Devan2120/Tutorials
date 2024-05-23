# print('Hello World')
# print(type(5))
# print(type(5.450))
# print(type('hello'))
# print(type(5 + 5.45j))
# print(type([1,2,3]))
# print(type({1,2,3}))
# print(type(False))
# print(type(None))
# print(type({"name":"akhil", "age": 30}))
# print(type((1,2,3)))

# x = (10,20,30,5,True, None, 'HJK ')

# print('HJK' in x)

# a = input('Enter Value 1')
# b = input('Enter Value 2')
# c = int(input('Enter Value 3'))

#print('Adiition:', a+b)
# print('Division:', a/b)
# if a%2 == 0:
#     print(a,"is Even")

## list of value -- seperate even and odd values as diff list
# even = list()
# odd = list()
# list1 = [1,2,3,4,5,6,7,8,9]
# for no in list1:
#     if no % 2 == 0:
#         even.append(no)
#     else:
#         odd.append(no)
# print('Even:',even)
# print('Odd:',odd)

## list of values -- sum of elements without using sum fn, and print
# def lsum(lst):
#     sum = 0
#     for no in lst:
#         sum += no
#     return sum
# print(lsum(list1))

# # user input 2 list -- join two list -- find sum
# lst1 = list(map(int, input('Enter Values of First List:').split(' ')))
# lst2 = list(map(int, input('Enter Values of Second List:').split(' ')))
# lst = lst1 + lst2
# print(lsum(lst))

# # reverese a string without using any known methods
# string1 = input("Enter a String:")
# rev_string1 = ""
# length = len(string1)
# for i in range(length):
#     rev_string1 += string1[-(i+1)]
# print(rev_string1)

# # program to find a number is prime or not, also print prime nos in a given range 
# no = int(input("Enter a Number:"))
# def check_prime(num):
#     is_prime = True
#     for i in range(2,num//2):
#         if num % i == 0:
#             is_prime = False
#             break
#     return is_prime
# if check_prime(no) == True:
#     print(no, "is a prime number")
# else:
#     print(no, 'is not a prime number')

# ran = int(input("Enter the range: "))
# prime = list()
# for nos in range(2,ran):
#     if check_prime(nos):
#         prime.append(nos)
# print(prime)

