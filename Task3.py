import secrets
import string

try:
    length=int(input("Enter length of the password:"))

except ValueError:
    print("ValueError:Input must be a number")
    
chara= string.ascii_letters+string.digits+"#$&"

password=""

for i in range(length):
    password+=secrets.choice(chara)

print("Generated Password:",password)