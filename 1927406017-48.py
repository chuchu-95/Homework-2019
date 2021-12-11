def appearance(a, n=0):
    a = a.lower()
    point = a[n]
    return a.count(point)

print(appearance("This is a test example"))

