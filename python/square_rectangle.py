length = float(input("Введите длину прямоугольника:"))
width = float(input("Введите ширину прямоугольника:"))
def square_rectangle(length,width):
    s = length*width
    return s
square = square_rectangle(length,width)
print("Длина прямоугольника: " + str(length))
print("Ширину прямоугольника: " + str(width))
print("При этом площадь прямоугольника: " + str(square))
