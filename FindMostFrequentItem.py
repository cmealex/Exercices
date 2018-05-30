from collections import Counter

test = "we hope to one day become the wolrds leader in free is now not now"

words = test.split()
print(words)

counter = Counter(words)
top_three = counter.most_common(3)
print(top_three)

myl = [1,1,2,3,2,4,2]
counter1 = Counter(myl)
comm = counter1.most_common()
print(comm)