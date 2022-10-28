def emailProcess(email):
    email_username=email[0:email.index("@")]
    email_domain=email[email.index("@")+1:]
    return [email_username,email_domain]

def printEnd(email_username, email_domain):
    print(f"User name:  {email_username}")
    print(f"Domain   :  {email_domain}")

def main():
    email=input("Nhap email address :")
    email_username, email_domain = emailProcess(email)
    printEnd(email_username,email_domain)

if __name__ == "__main__": 
    main()
