#otp
import random as r
import string as s
l=int(input("Enter:\n4 for numeric otp: \n6 for alphanumeric otp: \n"))
def otp():
  if (l==4):
    return str(r.randint(1000, 9999))
  elif (l == 6):
    chars=(s.ascii_lowercase + s.ascii_uppercase + s.digits)
    return ''.join(r.sample(chars, k=6))
print(otp())
