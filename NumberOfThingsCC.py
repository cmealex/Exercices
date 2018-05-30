def noOfThings(myl):
    if myl[0] == 1:
        return "There is " + str(myl[0]) + " " + myl[1]
    else:
        return "There are " + str(myl[0]) + " " +myl[1] + "s"

print(noOfThings([1, "lion"]))
print(noOfThings([5, "lion"]))