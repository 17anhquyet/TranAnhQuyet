def process(t):
    hour=t//3600
    minute=(t%3600)//60
    second=t%3600%60
    return hour,minute,second
    
def main():
    t=int(input("Nhap so giay :"))
    h,m,s=process(t)
    print("{0:<7} {1:>4}".format("Gio",h))
    print("{0:<7} {1:>4}".format("Phut",m))
    print("{0:<7} {1:>4}".format("Giay",s))

if __name__=="__main__":
    main()