import random as r
def rps(pc):
  compc=r.choice(["rock","paper","scissors"])
  if (pc==compc):
    return "draw"
  elif (pc=="rock"):
    if (compc=="paper"):
      return "comp won"
    else:
      return "player won"
  elif (pc=="paper"):
    if (compc=="scissors"):
      return "comp won"
    else:
      return "player won"
  elif (pc=="scissors"):
    if (compc=='rock'):
      return 'comp won'
    else:
      return 'player won'
compc=0
while True:
  pc=input('Choose rock, paper, or scissors: ').lower()
  if pc not in ["rock","paper","scissors"]:
    print('Invalid input')
    continue
  compc = r.choice(['rock', 'paper', 'scissors'])
  print('Computer chose:', compc)
  print(rps(pc))
  play_again = input('wanna play again? (y/n): ').lower()
  if play_again != 'y':
    break
