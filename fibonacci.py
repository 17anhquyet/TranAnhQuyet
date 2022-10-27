def fibon(n):
    if n==1 :
        return 1
    elif n==2 :
        return 1
    else:
        return fibon(n-1)+fibon(n-2)

while True:
    n=int(input("Enter :"))
    if n>2: break
print("List of fibon :",end="")
for i in range(1,n+1):
    print(fibon(i),end=" ")
