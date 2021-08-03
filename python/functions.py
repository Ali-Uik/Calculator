'''
def function1():
    print("Hello1")
    print("Hello2")
print("Hello from outside")
function1()

def function2(x):
    return 2*x 
a = function2(5)
print (a)
print (function2(4))

def sum_of_two_numbers(x,y):
    return x+y 
e = sum_of_two_numbers(4,5)
print(e)
def function5(some_argument):
    print("some_argument")
    print("Ali")
function5(5)
def function6():
    return 5
z = function6()

def function7(x):
    print(x)
    print("Ali")
    return 3*x
a = function7(10)
print (a)
'''
name1 = "Tom"
height1 = 1.90
weight1 = 80

name2 = "Kate"
height2 = 1.70
weight2 = 60

name3 = "Bob"
height3 = 2
weight3 = 150

def bmi_calculator(name,height,weight):
    bmi = weight/(height**2)
    print ("ИНдекс массы тела: " + str(bmi))
    if bmi < 25:
        return name + " не имеет лишнего веса"
    else:
        return name + " имеет лишний вес"
bmi1 = bmi_calculator(name1,height1,weight1)
bmi2 = bmi_calculator(name2,height2,weight2)
bmi3 = bmi_calculator(name3,height3,weight3)
print(bmi1)
print(bmi2)
print(bmi3)