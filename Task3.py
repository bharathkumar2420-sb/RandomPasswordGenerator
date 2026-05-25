import secrets
import string

try:
    length=int(input("Enter length of the password:"))
    
    chara= string.ascii_letters+string.digits+"#$&"

    password=[]

    for i in range(length):
        password.append(secrets.choice(chara))

    final_password="".join(password)

    print("Generated Password:",final_password)

except ValueError:
    print("ValueError:Input must be a number")
