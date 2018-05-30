from morse import string_to_morse

def returnMorse(str):
    return "".join(string_to_morse(list(str)))

print(returnMorse("SOS"))
print(returnMorse("TRINKET"))