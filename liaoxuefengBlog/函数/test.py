import math

# 定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程的解

def function(a, b, c):
    delta = (b ** 2 - 4 * a * c)
    if delta < 0:
        return 
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
    return x1, x2

print(function(2, 3, 1))
        

    

        