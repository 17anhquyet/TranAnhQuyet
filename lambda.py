def process(f,x):
    return f(x)

def soChan(x):
    return x%2==0

k=int(input("Enter :"))
print("So Chan" if process(lambda x:soChan,k)==True else "So Le") 
#print("So chan" if process(lambda x:(x%2==0),k) else "So Le")
