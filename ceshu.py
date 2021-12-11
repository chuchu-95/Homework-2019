# print(len("he67\\\n1"))
# lst1 = [123]
# lst2 = lst1
# if id(lst1) == id(lst2):
#     print("Yes")
# else:
#     print("No")
#
#
# def change(dict1):
#     dict1.clear()
# dict1 = {}.fromkeys([i for i in "aa"],0)
# change(dict1)
# print(dict1)
#
# def change2(x,y):
#     x,y = y,x
# num1 = 3
# num2 = 5
# change2(num1,num2)
# print(num1,num2)


# l = []
# for i in range(5):
#     if i % 2 == 1:
#         l.append(i*i)
# print(sum(l))
#
# lst = [[0]*10]*10
# print(lst)
# print(lst[1][0])
# lst[1][0]=5
# print(lst[3][0])


# def isPrime(x):
#     import math
#     if 0 not in [x % i for i in range(2, int(math.sqrt(x))+1)]:
#         return True
#     else:
#         return False
#
# def palindrome(x):
#     x_re = int(str(x)[::-1])
#     return x_re
#
# def isNotPalin(x):
#     return True if x != palindrome(x) else False
#
# def isInversePrime(x):
#     if isPrime(x) and isPrime(palindrome(x)) and isNotPalin(x):
#         return True
#     else:
#         return False
#
# def printInversePrime(x):
#     count, i = 0, 10
#     while count <= x:
#         if isInversePrime(i):
#             print('{:>5d}'.format(i), end=' ')
#             count += 1
#             if count % 8 == 0 and count > 0:
#                 print()
#         i += 1
#
# def main():
#     print(isInversePrime(17))
#     print(isInversePrime(19))
#     printInversePrime(30)
#
# main()
# def statistics(s, n=0):
#     s = s.lower()
#     cha = s[n]
#     return s.count(cha)
#
# def main():
#     print(statistics('This is a test example'))
#
# main()

# class Solution:
#     def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
#         u,l = [],[]
#         w =len(grid)
#         for i in range(w):
#             m = max(grid[i][j] for j in range(w)) #求出每一行的最大值
#             n = max(grid[j][i] for j in range(w)) #求出每一列的最大值
#             l.append(m)
#             u.append(n)
#         sum = 0
#         for i in range(w):
#             for k in range(w):
#                 if u[k] > l [i]:
#                     sum = sum + l[i]
#                 else :
#                     sum =sum + u[k]
#         t = 0
#         for i in range(w):
#             for k in range(w):
#                 t = t + grid[i][k]
#         s = sum - t
#         return s

def buddyStrings(A, B):
    pairs = []
    for a, b in zip(A, B):  # A、B不相等的情况
        if a != b:
            pairs.append([a, b])
        if len(pairs) > 2: return False
    return len(pairs) == 2 and pairs[0] == pairs[1][::-1]



print(buddyStrings('ab','ba'))



