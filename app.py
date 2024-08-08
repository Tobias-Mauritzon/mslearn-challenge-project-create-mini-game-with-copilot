#hello world

print("hello world")
score = {'wins' : 0,
         'losses' : 0,
         'ties' : 0}
print("enter rock, paper or scissors")

while score["wins"] < 3 :
    
    inputS = input()
    aiMove = 'paper'

    allowedMoves = ['rock', 'paper', 'scissors']
    badMove = False
    
    if(inputS == 'exit'):
        break
    if(inputS == None or not isinstance(inputS, str)):
        print("bad move")
        badMove = True

    inputS = inputS.lower()

    if(inputS not in allowedMoves):
        print("allowed moves are rock, paper or scissors")
        badMove = True

    if(not badMove):
        if(inputS == aiMove):
            print("you tied")
            score["ties"] +=1
        elif(inputS == "rock" and aiMove == "scissors"):
            print("you won")
            score["wins"] +=1
        elif(inputS == "paper" and aiMove == "rock"):
            print("you won")
            score["wins"] +=1
        elif(inputS == "scissors" and aiMove == "paper"):
            print("you won")
            score["wins"] +=1
        else:
            print("you lose")
            score["losses"] +=1

    print(score)