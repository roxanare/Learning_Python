a = [1, 2, 3]
b = a.copy()
c = b

b[1] = 5
print(a, b, c)

a = 1
b = a
c = b
b = 5
print(a, b, c)

#a = D1
#b = D1.copy()   # <------------ always copy

#some new changes
