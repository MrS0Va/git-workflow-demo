def add(a, b):
    print(f"Adding {a} and {b}")
    return a + b

def subtract(a, b):
    return a -b

def multiply(a, b):
    #Возвращает произведение двух чисел
    return a * b

def divide(a, b):

    if b == 0:
        raise ValueError("На ноль делить нельзя!")
    return a / b
if __name__ == "__main__":

    print("Тестирование калькулятора:")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
    print(f"4 * 3 = {multiply(4, 3)}")
    try:
        print(f"10 / 2 = {divide(10, 2)}")
        print(f"5 / 0 = {divide(5, 0)}")
    except ValueError as e:
        print(f"Error: {e}")