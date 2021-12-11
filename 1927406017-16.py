def median(lst):
    lst.sort()
    if len(lst) % 2 == 0:
        med = lst[int(len(lst)/2-1)]
    else:
        med = lst[int((len(lst)-1)/2)]
    return med


print(median([2, 98, 76, 3, 5]))
