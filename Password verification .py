import hashlib
import secrets
import string
 

N = 7
res = ''.join(secrets.choice(string.ascii_uppercase + string.digits)
              for i in range(N))


print ("\n\t SIGN UP")

class signup : 
    " Class for Sign-up "

    username = input("\n Enter Username :")
    password = input("\n Enter Password :")

    saltedpassword = password + str(res) 

    result = hashlib.sha256(saltedpassword.encode())
    hash = result.hexdigest()


print ("\n\t LOGIN")

class login :
    " Class for Login "

    username = input("\n Enter Username :") 

    if  username == signup.username :

        password=input("\n Enter Password :")

        saltedpassword = password + str(res)

        result = hashlib.sha256(saltedpassword.encode())
        hash = result.hexdigest()
            
        if hash == signup.hash :

            print ( "\n Account Logged in ")

        else :

            print ( "\n ACCESS DENIED !")

            
    else :

        print ("\n No Account with such username !")