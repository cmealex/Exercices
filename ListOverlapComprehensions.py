import random
# len1 = random.randint(1, 9)
# len2 = random.randint(1, 9)
#
# list1 = [random.randint(1, 100) for i in range(len1)]
# print list1
# list2= [random.randint(1, 100) for i in range(len2)]
# print list2
###########
# a = random.sample(xrange(50), random.randint(3,10))
# print a
##########
list1 = [1,1,2,5,8,13,21,34,55,89]
len1 = len(list1)
list2 = [1,2,3,4,5,6,7,8,9,10,11,12]
len2 = len(list2)

common_elems = []
if len1 > len2:
    for i in list2:
        if i in list1 and i not in common_elems:
            common_elems.append(i)
else:
    for i in list1:
        if i in list2 and i not in common_elems:
            common_elems.append(i)
print common_elems

#better version:? Actually not :)
c = [num for num in list1 if num in list2]
print c