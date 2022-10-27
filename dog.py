
class dog:
    legs=4
    species="dog"
    sound="gau"
    def __init__(self,list):
        self.name =list[0]
        self.color=list[1]
        self.origin=list[2]
        self.age=list[3]
    def showDogProfile(self):
        print(f"{self.name} la mot chu cho long {self.color} co nguon goc tu {self.origin} va hien tai {self.age} tuoi")
    def judgeAge(self):
        if int(self.age) >=2:
            return True

def main():
    arr=input("Enter :").split()
    boss=dog(arr)
    boss.showDogProfile()
    print("Old man" if boss.judgeAge()== True else "So young")

if __name__=="__main__":
    main()