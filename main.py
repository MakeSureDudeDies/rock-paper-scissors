print("Welcome to rock, paper, scissors, pick one of the three") 

def YouLost():
  print("\nYou Lost.")

picked = input("Let's start\n")
if picked == "scissors":
  print("rock")
  YouLost()
elif picked == "rock":
  print("paper")
  YouLost()
elif picked == "paper":
  print("scissors")
  YouLost()
else:
  print("Wrong input! type in lowercase.")
# lol ez get rekt
