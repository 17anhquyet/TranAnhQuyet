def process(f,x):
    return f(x)
# def BMI(h,w):
#     return w/(h*h)

def checkBMI(check):
    if check<18.5: return "Thin"
    elif check<25: return "Normal"
    elif check<30: return "A little Fat"
    elif check<35: return "Fat:Level 1"
    elif check<40: return "Fat:Level 2"
    else:return "Fat:Level 3"

def main():
    h,w=eval(input("Height,Weight enter:"))
    # print(f"Result: {checkBMI(BMI(h,w))}")
    print(f"Result: {process(lambda x: checkBMI(x),w/(h*h))}")

if __name__=="__main__":
    main()