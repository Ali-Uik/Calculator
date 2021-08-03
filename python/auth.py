import datetime
currentdate=datetime.datetime.now()
a = input ('Ismingizni kiriting:')
b = input ('Yoshingizni yoki tug\'ilgan yilingizni kiriting:')
print (type(b))

if(b>150):
    year=int(currentdate.year)
    age=year-b
    if(age>20):
        print ('Assalomu aleykun '+a+'. Servisimizga hush kelibsiz!')
    else:
        print(a+' bizning servisimizdan foydalanishga sizning yoshingiz yetmaydi!')
elif(20<b and b<150):
    print ('Assalomu aleykun '+a+'. Servisimizga hush kelibsiz!')
else:
    print(a+' bizning servisimizdan foydalanishga sizning yoshingiz yetmaydi!')
