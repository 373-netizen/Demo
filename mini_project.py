import random
print(f"Player")
print(f"Computer")
options=("Rock","Paper","Scissors")

def determine_winner(player,computer):
    if player==computer:
        return "It's a tie!"
    elif (player =="Rock"and computer == "Paper") or \
         (player =="Paper"and computer == "Scissors") or \
         (player =="Scissors"and computer == "Rock") :
         return"Computer wins!"
    else:    
         return"Player wins!"
player = None
while player not in options:
    player = input("Enter a choice(Rock,Paper,Scissors):").capitalize()
    if player not in options:
        print("Invalid choice,Try again")

computer = random.choice(options)
print(f"Player:{player}")
print(f"Computer:{computer}")
print(determine_winner(player,computer))
