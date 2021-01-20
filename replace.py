def replace_num(x, d1, d2):
    result = 0
    multiply = 1
    while x > 0:
        y = x % 10
        if y == d1:
            result += (d2 * multiply)
        else:           
            result += (y * multiply)
        multiply *= 10
        if x != 0: 
            x = (x - y) // 10
        else:
            pass
        return result
print(replace_num(2889, 8, 5))
