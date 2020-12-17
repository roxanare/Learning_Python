x = [1, 2, 3]

x = [1, 'sasa', [1, 2, 3]]

x = [[1, 2], [4, 5]]

print(len(x))
print(type(x))

x = [1, 2, 3, 4]

#  print(x - 1) throw exception

print(x[1:3])

print(x[1:-1])

print(x[:])

x = [-1, 0, 1, 2, 3, 4, 5, 6, 7]
x[1:-1] = ['x','x'] # [] will replace with nothing

print(x)

# x.append
# del x[1]

# x.insert

# del x[]

x = [-1, 0, 1, 2, 3, 4, 5, 6, 7]

x.remove(3)

print(x)
x.reverse()

print(x)

x.sort()
print(x)

z = [None, 1] * 4
print(z)

print(min(x))
print(max(x))

x = [-1, 0, 1, 2, 3, 'ddd',6, 5, 6, 7]
print(x.index('ddd'))


#### how to hard reference in code instead of writing string constants
# asas = 'asaa'

# df[asasa]

print(x.count(6))

# list comprehension 

# [  <expression to be evaluate as item>    for   i   in   <list>   if   <predicate>     ]

d = [i for i in range(1, 11) if i%2==0]
print(d)
