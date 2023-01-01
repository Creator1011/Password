import random


def generate(length: int, special_char: str = ""):
    num = "1234567890"
    upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
    lower = "qwertyuiopasdfghjklzxcvbnm"
    pwli = []
    if special_char != "":
        for x in range(0, int(length / 4)):
            pwli.append(special_char[random.randint(0, len(special_char) - 1)])
    for x in range(0, int(length / 4)):
        pwli.append(num[random.randint(0, 9)])
    for x in range(0, int(length / 4)):
        pwli.append(upper[random.randint(0, 25)])
    for x in range(0, length - len(pwli)):
        pwli.append(lower[random.randint(0, 25)])
    random.shuffle(pwli)
    password = ""
    for x in pwli:
        password += x
    return password


def generate_num(length: int):
    password = ""
    for i in range(0, length):
        password += str(random.randint(0, length))
    return password


print(generate(8, "`~!@#$%^&*()-=[]\\;\',./_+{}|:<>?\""))
