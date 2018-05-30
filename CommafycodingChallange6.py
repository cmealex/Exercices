myl = ["triknet", "learning", "fun"]

def commafy(my_list):
    return ", ".join(my_list[:-1]) + " and " + my_list[-1]

print(commafy(myl))

