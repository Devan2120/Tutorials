# check = 5
# for i in range(check):
#     for j in range(check - i - 1):
#         print(' ', end = " ")
#     for k in range(i + 1):
#         print('*', end = " ")
#     print()

# string1 = input("Enter a string: ")
# digits = 0
# char = 0
# for i in string1:
#     if i.isalpha():
#         char += 1
#     elif i.isdigit():
#         digits += 1
# print(f"Letter = {char} \nNumbers = {digits}")

# nos = list(int(i) for i in input("Enter the binary nos:").split(","))
# def to_decimal(no):
#     no = str(no)
#     dec = 0
#     for i in range(len(no) - 1, -1, -1):
#         dec += int(no[i]) * 2**i
#     return dec

# for no in nos:
#     if to_decimal(no) % 5 == 0:
#         print(no)

# a = int(input("Enter the value of a:"))
# b = int(input("Enter the range:"))
# sum = 0
# for i in range(b):
#     no = ""
#     for j in range(i + 1):
#         no += str(a)
#     sum += int(no)

# print(sum)

# nos = list(int(i) for i in input("Enter the binary nos:").split(","))
# max = nos[0]
# for no in nos:
#     if max < no:
#         max = no
# print(max)

# def fact(no):
#     if no == 0:
#         return 1
#     else:
#         return(no * fact(no - 1))
# print(fact(5))

##leetcode probs
# #q1
# nums = list(int(i) for i in input("Enter the nos:").split())
# tar = int(input("Enter the target"))
# for i in range(len(nums)):
#     for j in range(i,len(nums)):
#         if nums[i] + nums[j] == tar:
#             print([i,j])

# #q2         
# l1 = list(int(i) for i in input("Enter the no:").split())
# l2 = list(int(i) for i in input("Enter the no:").split())
# l1.reverse()
# l2.reverse()
# sum = int("".join(str(i) for i in l1[::-1])) + int("".join(str(i) for i in l2[::-1]))
# print(list(int(i) for i in str(sum))[::-1])

#q3
# roman = input("Enter the Roman numerals:")
# ref = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
# sum = 0
# for i in range(len(roman)):
#     if i != len(roman) - 1:
#         if ref[roman[i]] >= ref[roman[i+1]]:
#             sum += ref[roman[i]]
#         else:
#             sum -= ref[roman[i]] 
#     else:
#         sum += ref[roman[i]]
# print(sum)     

# #q4
# s = input("Enter a string:")
# sub_strings = [s[i : j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]
# print(max(len(set(list(i))) for i in sub_strings if len(set(list(i))) == len(i)))

##q5
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

# #q6
# s = input("Enter a string:")
# sub_strings = [s[i : j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]
# ans = s[0]
# for i in sub_strings:
#     if i[::-1] == i[:] and len(i) > len(ans):
#         ans = i
# print(ans)

# #q7
# num = input("Enter a no:")
# if num[:] == num[::-1]:
#     print(True)
# else:
#     print(False)

# #q8
# no = input("Enter a no:")
# if int(no) < 0:
#     rev_no = '-' + no[-1:0:-1]
# if int(rev_no) <= 231 and int(rev_no) >= -231:
#     print(rev_no)
# else:
#     print(0)

# #q9
# def convert(s, rows):
#     out = ""
#     for i in range(rows):
#         if i in (0,rows - 1):
#             out += "".join(s[i::2*(rows - 1)])
#         else:
#             j = i
#             out += s[i]
#             while j < len(s):
#                 j += 2*(rows - i -1)
#                 if j < len(s):
#                     out += s[j]
#                 else:
#                     break
#                 j += 2*i
#                 if j < len(s):
#                     out += s[j]
#                 else:
#                     break        
                
#     return out

# print(convert("PAYPALISHIRING", 3))

# #q10
# strs = list([i for i in input("Enter:").split()])
# pre = strs[0]
# for i in strs:
#     for j in range(min(len(pre),len(i))):
#         if pre[j] != i[j]:
#             pre = i[:j]
#             break

# print(pre)

# #q11
# s = list(input("Enter:"))
# ans = True
# dic = {')':'(', '}':'{', ']':'['}
# for i in range(len(s)):
#     if s[i] in (')','}', ']'):
#         if s[i - 1] != dic[s[i]]:
#             ans = False
#             break
# print(ans)

# #q12
# lst1 = list(i for i in input("Enter:").split())
# lst2 = list(i for i in input("Enter:").split())
# print(sorted(lst1 + lst2))

#q13
# nums = list(int(i) for i in input("Enter:").split())
# k = 0
# for i in range(len(nums)):
#     while nums.count(nums[i]) > 1:
#         nums.pop(nums[i + 1:].index(nums[i]))
#         nums.append('_')
#         k += 1
# print(len(nums) - k)
# print(nums)

#q14
# nums = list(int(i) for i in input("Enter:").split())
# num = list(set(nums))
# print(len(num))
# for i in range(len(nums) - len(num)):
#     num.append('_')                     #can be anything

# print(num)

# #q15
# nums = list(int(i) for i in input("Enter:").split())
# val = int(input('Enter val:'))
# k = nums.count(val)
# print(len(nums) - k)
# for i in range(nums.count(val)):
#     nums.remove(val)
#     nums.append('_')
# print(nums)


