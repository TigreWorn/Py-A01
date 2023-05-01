#unique 12 digit pass
import random as r
import string as s
def passw():
  low=s.ascii_lowercase
  upr=s.ascii_uppercase
  digit=s.digits
  symbols=s.punctuation
  allc= low+upr+digit+symbols
  if len(allc)<8:
    len(allc)==8
  passw=''.join(r.sample(allc,12))
  return passw
print(passw())
