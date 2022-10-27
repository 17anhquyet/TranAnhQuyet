from math import sqrt

def process(a,b,c):
    if a==0:
        if b==0 and c==0:
            print("Countless of value")
        elif b==0 and c!=0:
            print("None of value")
        else:
            print(f"x = {-c/b:5.2f}")
    else:
        d=b**2-4*a*c
        if d<0 :
            print("None of value")
        elif d==0:
            print(f"x = {-b/(2*a):5.2f}")
        else:
            x1=(-b+sqrt(d))/(2*a)
            x2=(-b-sqrt(d))/(2*a)
            print(f"x1 = {x1:5.2f}")
            print(f"x2 = {x2:5.2f}")
def main():
    c=input("Enter a,b,c :").split()
    process(float(c[0]),float(c[1]),float(c[2]))
    
if __name__=="__main__":
    main()