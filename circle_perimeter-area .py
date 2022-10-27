from cmath import pi


def data():
    r=float(input("Nhap ban kinh hinh tron :"))
    return r

def perimeter(r):
    return 2*r*pi

def area(r):
    return r**2*pi

def main():
    try:
        r=data()
        print(f"Chu vi hinh tron : {perimeter(r)}")
        print(f"Dien tich hinh tron : {area(r)}")
    except:
        print("Du lieu nhap bi sai")
        
if __name__ == "__main__":
    main()
    