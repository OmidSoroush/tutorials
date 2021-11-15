def square(x):
    for i in x:
        yield (i * i)

squares = square([2, 3, 4, 5])

print(squares)

print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))

for i in squares:
    print(i)

lst = [2, 3, 4, 5]

gen_exp = (x**2 for x in lst)



print(min(x**2 for x in lst))
print(sum(x**2 for x in lst))