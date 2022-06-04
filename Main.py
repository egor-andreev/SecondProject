def decorator_func(function_name):
    def inner_decorator(num1, num2): #1
        print("decoration!!! in progress")
        c = function_name(num1, num2) #2
        return c #5
    return inner_decorator

@decorator_func
def calculator_sum(a, b):#3
    c = a+b
    print(c)
    return c #4

p = calculator_sum(5, 3)
#6
print(p)
#returns result of calculation. Последовательность передачи аргументов в комментариях