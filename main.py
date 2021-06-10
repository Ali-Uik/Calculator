
what = input("Qaysi amalni bajaramiz:+,-,*,/")

a = float(input("Birinchi sonni kiriting:"))
b = float(input("Ikkinchi sonni kiriting:"))

if what == "+":
	c=a+b
	print("Yig'indi " +str(c)+"ga teng")
elif what == "-":
	c=a-b
	print("Ayirma " +str(c)+"ga teng")
elif what == "*":
	c=a*b
	print("Ko'paytma " +str(c)+"ga teng")
elif what == "/":
	c=a/b
	print("Bo'linma " +str(c)+"ga teng")
else: 
	print("Siz bajarilishi kerak bo'lgan amalni tanlamadingiz")

what2= input("Yana qaysi amalni bajaramiz:+,-,*,/")
d = float(input("Uchinchi sonni kiriting:"))
if what2 == "+":
	e=c+d
	print("Yig'indi " +str(e)+"ga teng")
elif what2 == "-":
	e=c-d
	print("Ayirma " +str(e)+"ga teng")
elif what2 == "*":
	e=c*d
	print("Ko'paytma " +str(e)+"ga teng")
elif what2 == "/":
	e=c/d
	print("Bo'linma " +str(e)+"ga teng")
else: 
	print("Siz bajarilishi kerak bo'lgan amalni tanlamadingiz")
input()     