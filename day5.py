print("\n1. MY FIRST PROJECT::")
print(      "                                              "                                           "+=CALCULATOR+=")
a=float(input('ENTER NUM1='))
b=float(input('ENTER NUM2='))
print('SELECT CHOICE 1.add\n2.sub\n3.mul\n4.div')
op=int(input('enter choice'))
if op ==1:
    print('solution=',a + b)
elif op ==2:
    print('solution=',a-b)
elif op ==3:
    print('solution=',a* b)
elif op ==4:
    print('solution=',a /b)
else:
    print('ERROR')

print('THANK YOU')