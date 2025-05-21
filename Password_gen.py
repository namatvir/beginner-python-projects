import random

def password_gen(leng: int)->str:

    """
    Create a random password of length: leng
    """
    
    storage='1234567890-=qwertyuiop[]asdfghjkl;zxcvbnm,./!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?'
    password=[]
    for i in range(leng):
        password.append(random.choice(storage))

    return ''.join(password)

def user_test(user_password: str, generated_password: str):


    """
    Test newly created password of inputted user_password
    """
    
    if user_password == generated_password:
        return "welcome"
        
    else:
        return "incorrect password"


length = int(input("length of password:"))

stored_pass = password_gen(length)

print("your password is:", stored_pass)

print(user_test(input("enter password:"),stored_pass))

#Key takeaway: original error was generating new passwords and comparing those new ones within user_test
#Change: store generated password the compare user input with stored password
