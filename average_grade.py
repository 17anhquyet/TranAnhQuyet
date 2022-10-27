
def data():
    m=float(input("Nhap diem toan:"))
    p=float(input("Nhap diem ly  :"))
    c=float(input("Nhap diem hoa :"))
    return m,p,c

def main():
    grades=data()
    s=0
    for grade in grades:
        s+=grade
    print("Diem trung binh :{0:>10.2f}".format(s/len(grades)))
    
if __name__=="__main__":
    main()