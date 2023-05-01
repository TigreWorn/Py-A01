#guess game
import random as r
comp=r.randint(1,10)
user=int(input("guess number: "))
if user==comp:
    print(f"you guess is right: \n comp-->{comp} \n user-->{user}")
else:
    print(f"you guess is wrong: \n comp-->{comp} \n user-->{user}")
