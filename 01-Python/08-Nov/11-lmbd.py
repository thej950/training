max_num = lambda a, b, c: a if a > b and a > c else (b if b > c else c)
print(max_num(10, 25, 15))
