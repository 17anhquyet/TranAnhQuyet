# def process(f,x):
#     return f(x)

def factorial(n):
    return n*factorial(n-1) if n!=0 else 1

x=int(input("Enter :"))
print(f"Factorial of {x} = ",factorial(x))

# print(f"Factorial of {x} = ",process(factorial,x))