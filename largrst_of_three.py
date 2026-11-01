def largest_of_three(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
num1 = int(input("enter a number A: "))    
num2 = int(input("enter a number B: "))
num3 = int(input("enter a number C: "))
result=largest_of_three(num1,num2,num3)
print("largest number:",result)