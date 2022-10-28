from sub_module import emailProcess, printEnd

def main():
    emails = ["linhphuong97dl@gmail.com","17anhquyet@gmail.com"]
    for email in emails :
        u,d = emailProcess(email)
        printEnd(u,d)

if __name__ == "__main__":
    main()