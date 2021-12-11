def reverse(n):
    li = n.split(" ")
    n = " "
    re = n.join(li[::-1])
    return re


print(reverse("What a wonderful day!"))
