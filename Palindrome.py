pstr = raw_input("please input string to check if palindrome: ")
if pstr == pstr[::-1]:
    print "yes"
else:
    print "no"

for i in range(len(pstr)):
    if pstr[i] == pstr[len(pstr)-1-i]:
        continue
    else:
        print 'not palindrom'
        break

loopc = 0

while loopc < len(pstr):
    if pstr[loopc] == pstr[len(pstr)-loopc-1]:
        if loopc == len(pstr)-1:
            print 'p'
            break
    else:
        print 'np'
        break
    loopc+=1