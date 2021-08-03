import random
a = int (input('Birinchi random uchun birinchi sonni kiriting:'))
b = int (input('Birinchi random uchun ikkinchi sonni kiriting:'))
list_1 = [a,b]
ab_min=min(list_1)
ab_max=max(list_1)
c = int (input('Ikkinchi random uchun birinchi sonni kiriting:'))
d = int (input('Ikkinchi random uchun ikkinchi sonni kiriting:'))
list_2 = [c,d]
cd_min=min(list_2)
cd_max=max(list_2)
i=0
while i<3:
    rand1 = random.randint(ab_min,ab_max)
    rand2 = random.randint(cd_min, cd_max)
    print('Birinchi random natijasi:', rand1)
    print('Ikkinchi random natijasi:', rand2)
    def rand (rand1,rand2):
        sum = rand1+rand2
        print(sum)
    rand(rand1,rand2)
    i=i+1