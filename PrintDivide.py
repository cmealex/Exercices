for i in range(50):
    if i%3==0 and i%5==0:
        print(i, "35")
    elif i%5==0:
        print(i, "5")
    elif i%3==0:
        print(i, "3")
    else:
        print(i)