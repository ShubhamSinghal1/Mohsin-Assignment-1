"""2)Reverse typing (one more solutionn is present in this script)"""

var = input("please enter the text: ")
length = len(var)
num = -1
while num >= -length:
    print(var[num],end = "")
    num -= 1
