a=1
b=1
c=1

print("Fibo no, Golden Ration" )
while c < 1000000:
    print(c,",", c/a)
    c=a+b
    a=b
    b=c
