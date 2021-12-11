str1 = input("please input a lowercase1: ")
str2 = input("please input a lowercase2: ")
l1 = list(str1)
l2 = list(str2)
l1.sort()
l2.sort()
m ="".join(l1)
n ="".join(l2)
if m == n:
    print("true")
else:
    print("false")
