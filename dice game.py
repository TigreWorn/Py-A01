import random
num_dice = 2
num_eyes = 6
score = 0
dice_to_keep = []
for i in range(num_dice):
    roll = random.randint(1, num_eyes)
    print("Dice", i+1, "rolled a", roll)
    score += roll
print("Your score is", score)
while True:
    keep = input("Which dice do you want to keep? (separate with commas) ")
    keep_list = keep.split(",")
    valid_input = True
    for die in keep_list:
        if not die.isdigit() or int(die) < 1 or int(die) > num_dice:
            valid_input = False
            break
    if valid_input:
        for die in keep_list:
            if int(die) not in dice_to_keep:
                dice_to_keep.append(int(die))
        break
    else:
        print("Invalid input. Please try again.")
for i in range(num_dice):
    if i+1 not in dice_to_keep:
        roll = random.randint(1, num_eyes)
        print("Dice", i+1, "rolled a", roll)
        score += roll
print("Your final score is", score)
