n=int(input("enter the number"))
if n%3==0 and n%5==0:
    print("fizzbuzz")
elif n%5==0:
    print("buzz")
elif n%3==0:
    print("fizz")
else:
    print(n)