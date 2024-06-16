import random
while True:
  choices=["rock","paper","scissors"]
 
  computer = random.choice(choices)
  player = None
  while player not in choices:
    player = input("choose from rock, paper or scissors: ").lower()                                           

    
  if player== computer:
        print("player:"+player)
        print("computer:"+computer)
        print("it's a tie")
    
  elif player == "rock":
        if computer == "paper":
          print("player: "+player)
          print("computer: "+computer)
          print("you've lost")
        if computer == "scissors":
          print("player: "+player)
          print("computer: "+computer)
          print("you've won")
          
  elif player == "paper":
        if computer == "rock":
          print("player: "+player)
          print("computer: "+computer)
          print("you've won")
        if computer == "scissors":
          print("player: "+player)
          print("computer: "+computer)
          print("you've lost")
          
  elif player == "scissors":
        if computer == "rock":
          print("player: "+player)
          print("computer: "+computer)
          print("you've lost")
        if computer == "paper":
           print("player: "+player)
           print("computer: "+computer)
           print("you've won")
  answer= input ("do you still want to play yes/no: ").lower() 
  if answer != "yes":
       break
print("bye")
         