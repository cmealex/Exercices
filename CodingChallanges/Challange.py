from math import sqrt
from typing import Counter

'''
https://www.w3resource.com/python-exercises/challenges/1/index.php
'''

# def perfectSquare(n):
#     if sqrt(n)==2:
#         print("True")
# perfectSquare(5)

# #for every case if power of x
# def checkIfPow(n, power):
#     a=n
#     while n>=0:
#         if n%power==0 and isinstance(n, int):
#             # print(n)
#             n = int(n/power)
#             if n==1:
#                 print("{} is power of: {}".format(a, power))
#                 break
#         else:
#             break
# checkIfPow(9,3)

# def is_Power_of_x(n, x):
#     while (n % x == 0):
#         # print(n)
#         n /= x
#     return n == 1
#
# print(is_Power_of_x(18,2))
# print(is_Power_of_x(81,3))
# print(is_Power_of_x(21,3))
# print(is_Power_of_x(4,2))
# print(is_Power_of_x(9,3))
# print(is_Power_of_x(4,4))

# def missingNo(myl):
#     mysum = sum(myl)
#     full_sum = sum(range(myl[0],myl[-1]+1))
#     print(full_sum- mysum)
# missingNo([10,11,12,14,15,16,17])

# def findMissingNumbers(myl):
#     miss = []
#     normal_list = list(range(myl[0], myl[-1] + 1))
#     # a = set(normal_list)
#     # b = set(myl)
#     # print(a,b)
#     # print(a.difference(b))
#     # print(normal_list)
#     for i in normal_list:
#         # print(i)
#         if i not in myl:
#             miss.append(i)
#     print(miss)
# findMissingNumbers([1,2,3,4,6,7,10])

# def find3NoArraySum3Is0(myl):
#     result = []
#     for i in range(len(myl)):
#         for j in range(i+1, len(myl)):
#             for k in range(j+1, len(myl)):
#                 if myl[i] + myl[j] + myl[k] ==0:
#                     c = [myl[i],myl[j], myl[k]]
#                     c.sort()
#                     if c not in result:
#                         result.append(c)
#     print(result)
# find3NoArraySum3Is0( [-1,0,1,2,-1,-4])
# find3NoArraySum3Is0( [-25,-10,-7,-3,2,4,8,10])

# def find3NoArraySum3Is0(myl, x):
#     result = []
#     for i in range(len(myl)):
#         for j in range(i+1, len(myl)):
#             for k in range(j+1, len(myl)):
#                 if myl[i] + myl[j] + myl[k] ==x:
#                     c = [myl[i],myl[j], myl[k]]
#                     c.sort()
#                     if c not in result:
#                         result.append(c)
#     print(result)
# find3NoArraySum3Is0([1, 0, -1, 0, -2, 2], 1)

# def occurOnce(myll):
#     dic = {}
#     for i in myll:
#         count = 1
#         if i in dic:
#             count+=1
#             dic[i]=count
#         else:
#             dic[i] = 1
#     # print(dic)
#     for k,v in dic.items():
#         if v == 1:
#             print(k)
# occurOnce([5, 3, 4, 3, 4])
# occurOnce( [5, 3, 4, 3, 5, 5, 3])
# occurOnce([1, 1, 1, 2, 2, 2, 3])
# occurOnce([1, 2, 1, 3, 2, 5])

# def addDigitsUntilSingleDigit(n):
#     while len(str(n))!=1:
#         one_digit = 0
#         for i in str(n):
#             one_digit+=int(i)
#         if len(str(one_digit))>1:
#             n=one_digit
#         else:
#             print(one_digit)
#             break
# addDigitsUntilSingleDigit(59)

# def additiveSecq(myl):
#     for i in range(len(myl)-2):
#         if myl[i]+myl[i+1] == myl[i+2]:
#             # print(myl[i], myl[i+1], myl[i+2])
#             continue
#         else:
#             return False
#     return True
# print(additiveSecq([6, 6, 12, 18, 30]))
# print(additiveSecq([5, 1, 1, 2, 3]))
# print(additiveSecq([2, 3, 5, 8, 13]))

# def reverseDigitsOfInteger(n):
#     return str(n)[::-1]
# print(reverseDigitsOfInteger(234))

#
# def arithmeticProgresison(myl):
#     diff = myl[0] - myl[1]
#     for i in range(len(myl)-1):
#         if not myl[i]-myl[i+1] == diff:
#             return False
#     return True
# print(arithmeticProgresison([5, 7, 9, 11]))
# print(arithmeticProgresison([5, 8, 9, 11]))

# def geometricProgresison(myl):
#     mult = myl[1]/myl[0]
#     for i in range(len(myl)-1):
#         if not myl[i+1]/myl[i] == mult:
#             return False
#     return True
# print(geometricProgresison([2, 6, 18, 54]))
# print(geometricProgresison([10, 5, 2.5, 1.25]))
# print(geometricProgresison([5, 8, 9, 11]))

# def reverseDigitsOfIntegerPlusSum(n,m):
#     a = int(str(n)[::-1])
#     b = int(str(m)[::-1])
#     return int(str(a+b)[::-1])
# print(reverseDigitsOfIntegerPlusSum(13,14))
# print(reverseDigitsOfIntegerPlusSum(130,1))
# print(reverseDigitsOfIntegerPlusSum(305,794))

# def get1(n):
#     output = []
#     while n!=1:
#         output.append(n)
#         if n%2==0:
#             n/=2
#         else:
#             n=3*n+1
#     output.append(1)
#     print(output)
# get1(12)
#
# def checkUglyNo(num):
#     if num == 0:
#         return False
#     for i in [2, 3, 5]:
#         while num % i == 0:
#             num /= i
#     return num == 1
# print(checkUglyNo(12))
# print(checkUglyNo(13))

# def checkHammingNo(num):
#     if num == 0:
#         return False
#     for i in [2, 3, 5]:
#         while num % i == 0:
#             num /= i
#     return num == 1
# print(checkHammingNo(12))
# print(checkHammingNo(15))

# def getHammingNo(num):
#     output = []
#     for i in range(1,num+1):
#         if checkHammingNo(i):
#             output.append(i)
#     return output
# print(getHammingNo(28))

# def anagram(str1, str2):
#     if sorted(str1) == sorted(str2):
#         print("anagram")
#     else:
#         print("no")
# anagram("anagram", "nagaram")
# anagram("anagram", "anagaram")

# def pushZerosEnd(myl):
#     l = len(myl)
#     for i in range(l):
#         if i==0:
#             myl.remove(i)
#             myl.append(i)
#
#     print(myl)
# pushZerosEnd( [0,2,3,4,6,7,10])

# def majorityElem(myl):
#     x = Counter(myl).most_common()
#     if x[0][1]>=(len(myl)/2):
#         print(x[0][0], " is the most commin")
#     else:
#         print("no majority")
# majorityElem([1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 6])
# majorityElem([1,2,3,4,3,3,2,4,5,6,1,2,3,4,6,1,2,3,4,6,6])

# def lengthOfLastWord(str1):
#     return len(str1.split(" ")[-1])
# print(lengthOfLastWord("Python Exercises"))
# print(lengthOfLastWord("Python"))
# print(lengthOfLastWord(""))
# print(lengthOfLastWord(" "))

# def oddOcc(myl):
#     x = Counter(myl).most_common()
#     # print(x)
#     for i in x:
#         # print(i)
#         if i[1]%2!=0:
#             print(i[0])
# oddOcc([ 4, 5, 4, 5, 2, 2, 3, 3, 2, 4, 4 ])

# def countDuplicates(myl):
#     x = Counter(myl).most_common()
#     # print(x)
#     c = 0
#     for i in x:
#         # print(i[1])
#         if i[1]>1:
#             c+=1
#     print(c)
# countDuplicates([ 1,3,1,4,5,6,3,2 ])

def mergeStrings(a,b):
    minim = min(len(a), len(b))
    mergedString = ""
    for i in range(minim):
        mergedString+=a[i]+b[i]
    if len(a)>len(b):
        mergedString+=a[len(a)-len(b)+1:]
    elif len(a)<len(b):
        mergedString += b[len(b) - len(a) + 1:]
    return mergedString
print(mergeStrings("abc","def"))
print(mergeStrings("ab","zsd"))

