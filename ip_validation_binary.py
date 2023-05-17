def decimalToBinary(n):
    return bin(n).replace("0b", "")


def binaryToDecimal(n):
    return int(n, 2)


print("Enter 0 for Binary Mode and 1 for Decimal Mode: ", end="")
mode = int(input())
print("Enter IP: ", end="")
str1 = str(input())
t1 = []
t2 = []
t3 = []
t4 = []
flag = 0

if mode == 0:
    if (len(str1) != 32):
        flag = 1
        print("Invlaid IP: Incorrect Length!")

    t1 = str1[0:8]
    t2 = str1[8:16]
    t3 = str1[16:24]
    t4 = str1[24:32]

if mode == 1:
    str1 = str1.split(".")

    s1 = str(str1[0])
    s2 = str(str1[1])
    s3 = str(str1[2])
    s4 = str(str1[3])

    t1 = int(str1[0])
    t2 = int(str1[1])
    t3 = int(str1[2])
    t4 = int(str1[3])

    ss1 = str(int(str1[0]))
    ss2 = str(int(str1[1]))
    ss3 = str(int(str1[2]))
    ss4 = str(int(str1[3]))

    if (s1 != ss1 or s2 != ss2 or s3 != ss3 or s4 != ss4):
        flag = 2
        print("Entered input is of incorrect format!")
    elif (t1 > 0 and t2 > 0 and t2 > 0 and t3 > 0 and t4 > 0):
        if (t1 < 256 and t2 < 256 and t3 < 256 and t4 < 256):
            flag = 0
        else:
            flag = 1
            print("Invalid IP: Decimal Value out of Range!")
    else:
        flag = -1
        print("Invalid IP: Decimal Value is Negative!")


if (flag == 0 and mode == 0):
    print("Valid IP Address")
    if t1[0] == "0":
        print("Clasa A")
    elif t1[0:2] == "10":
        print("Class B")
    elif t1[0:3] == "110":
        print("Class C")
    elif t1[0:4] == "1110":
        print("Class D")
    elif t1[0:5] == "11110":
        print("Class E")


if (flag == 0 and mode == 1):
    print("Valid IP Address")
    b1 = decimalToBinary(t1)
    b1 = b1.zfill(8)
    b2 = decimalToBinary(t2)
    b2 = b2.zfill(8)
    b3 = decimalToBinary(t3)
    b3 = b3.zfill(8)
    b4 = decimalToBinary(t4)
    b4 = b4.zfill(8)
    bi = b1 + b2 + b3 + b4

    print(bi)
    a = t1
    if (a >= 0 and a <= 127):
        print("Class A")
    if (a >= 128 and a <= 191):
        print("Class B")
    if (a >= 192 and a <= 223):
        print("Class C")
    if (a >= 224 and a <= 255):
        print("Class D")