a=int(input())
b=float(input())
c=a/b**2
if c<18:
    print("0") 
elif c>=18 and c<25:
    print("1")
elif c>=25 and c<30:
    print("2")
elif c>=30 and c<40:
    print("3")
elif c>=40:
    print("4")
