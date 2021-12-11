import operator
fenshu = {"张飞":78+75,
          "李大刀":92+67,
          "李墨白":84+88,
          "王老虎":50+50,
          "雷小米":99+98}
a = sorted(fenshu.items(),key=operator.itemgetter(1))
print(a)
