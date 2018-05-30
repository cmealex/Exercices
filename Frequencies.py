import operator

myl = [1,1,2,3,2,4,2]

freq = {}
for i in myl:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)
for key, value in sorted(freq.items(), key=operator.itemgetter(1)):
    print(key, value)

freq2 = {}
for i in myl:
    freq2[i] = myl.count(i)
print(freq2)

print(max(freq2.items(), key=operator.itemgetter(1))[1])


def keywithmaxval(d):
    """ a) create a list of the dict's keys and values;
        b) return the key with the max value"""
    v = list(d.values())
    k = list(d.keys())
    return k[v.index(max(v))], max(v)

print(keywithmaxval(freq2))