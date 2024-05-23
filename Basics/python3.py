# ##tuple
# one = (1,)
# a = (1,2,34,67)
# b = (3,4,56)
# # c = list(b)
# # c[1] = 8
# b = tuple(c)
# print(tuple(zip(a,b)))
# d , *e, f= ("Mon","Tue","Wed","Thurs")
# print(d)
# print(e)
# print(f)

## set
# se = set((1, True))
# print(se)
# sets = set((1,a))
# print(sets)

#set methods
# sets.add(45)
# sets.update((54,23,68))
# sets.remove(68)
# sets.discard(23)
# sets.pop()
# print(sets)

# s1 = {1,2,3,4}
# s2 = {5,6,7,3,4}
# print(s1 | s2)
# s1.union(s2)
# print(s1)
# print(s1 & s2)
# print(s1.intersection(s2))
# print(s1 - s2)
# print(s1.difference(s2))
# print(s1^s2)
# print(s1.symmetric_difference(s2))

##dictionary
# dic = {}
# for i in range(21):
#     if i % 2 == 0:
#         dic[i] = i**3
#     else:
#         dic[i] = i
# print(dic)

# string1 = "I am in kozhikode, and today is a wonderful day"
# chars = set(list(string1))
# dict = {}
# for i in chars:
#     if i != " ":
#         dict[i] = string1.count(i)
# print(dict)

# string2 = "karaparamba"
# chars = set(list(string2))
# dic = {}
# for ch in chars:
#     counts = 0
#     for i in range(len(string2)):
#         if (ch == string2[i]):
#             counts +=1
#     dic[ch] = counts
# print (dic)

# even = {i:i**3 for i in range(20) if i % 2 == 0  }
# print(even)

# ##Q
# #count the no of vowels in the string -- user
# string1 = input("Enter a string:")
# vowels = ('a','e','i','o','u')
# vowel_count = {}
# for vowel in vowels:
#     counts = 0 
#     for i in range(len(string1)):
#         if (vowel == string1[i].lower()):
#             counts +=1
#     vowel_count[vowel] = counts
# print(vowel_count)

# #print first 20 nos of a fibonocci series -- while and for
# a1 = 0
# a2 = 1
# print(a1,a2, end = " ")
# for i in range(18):
#     out = a1 + a2
#     print(out, end = " ")
#     a1, a2 = a2, out
# print()
# b1, b2 = 0, 1
# print(b1, b2, end = " ")
# i = 0
# while i < 18:
#     out = b1 + b2
#     print(out, end = " ")
#     b1, b2 = b2, out
#     i += 1


# #print all factors of a given no by user
# no = int(input("Enter a no:"))
# factors = list()
# for i in range(1,no+1):
#     if no % i == 0:
#         factors.append(i)
# print(factors)

# #find length of a string without using len() fn
# st = input("Enter a string: ")
# counter = 0
# for i in st:
#     counter += 1
# print(f"Length of the string = {counter}")

# # print follwing pattern
# """
#  1
#  2 3
#  4 5 6
#  7 8 9 10
#  """
# check = 1
# for i in range(1,11):
#     print(i, end = " ")
#     if i == check * (check + 1)/2:
#         print()
#         check += 1

#  # find median fo two sorted array
# """[1,3] and [2] output = 2 exp: median of [1,2,3]
#     [1,2] and [3,4] output = 2.5 """

# a1 = list(int(i) for i in input("Enter the nos:").split())
# a2 = list(int(i) for i in input("Enter the nos:").split())
# a = a1 + a2
# a.sort()
# length = len(a)
# mid = length//2
# if length % 2 == 0:
#     median = (a[mid-1] + a[mid])/2
# else:
#     median = a[mid]
# print(median) 
