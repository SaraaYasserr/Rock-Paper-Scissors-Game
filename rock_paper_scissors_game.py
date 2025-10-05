import random 

while True:
 choices=["rock","paper","scissors"]
 computer=random.choice(choices)
 player=None


 while player  not in choices:
     player=input("Enter rock,paper or scissors ").lower()

 if player ==computer:
    print("computer "+computer)
    print("player "+player)
    print("Tie")

 elif player=="rock":
    if computer=="paper":
        print("computer "+computer)
        print("player "+player)
        print("You lose")

    if computer=="scissors":
        print("computer "+computer)
        print("player "+player)
        print("You Win")

 elif player=="paper":
    if computer=="rock":
        print("computer "+computer)
        print("player "+player)
        print("You lose")

    if computer=="scissors":
        print("computer "+computer)
        print("player "+player)
        print("You lose")

 elif player=="scissors":
    if computer=="paper":
        print("computer "+computer)
        print("player "+player)
        print("You Win")

    if computer=="rock":
        print("computer "+computer)
        print("player "+player)
        print("You lose")

 again=input("Do You Want to play again(Yes/No)").lower()
 if again!="yes":break 
print("Good Bye")