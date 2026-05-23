import random
l = ['rock', 'paper', 'scissor']
while(True):
    print('''1. Play
2. Exit''')
    ch = int(input("Enter 1 or 2: "))
    if(ch == 2):
        print("Exiting from game...")
        break
    elif(ch == 1):
        uscore = 0
        cscore = 0
        for i in range(1, 6):
            print('''\n1. rock
2. paper
3. scissor''')
            uch = int(input("Enter 1, 2 or 3: "))
            cch = random.choice(l)
            print(f"Computer chooses {cch}")
            if((uch == 1 and cch == 'rock') or (uch == 2 and cch == 'paper') or (uch == 3 and cch == 'scissor')):
                print("Its a draw!")
                uscore += 1
                cscore += 1
            elif((uch == 1 and cch == 'scissor') or (uch == 2 and cch == 'rock') or (uch == 3 and cch == 'paper')):
                print("You won :)")
                uscore += 2
            elif(uch != 1 and uch != 2 and uch != 3):
                print("Enter valid input!")
            else:
                print("Computer won :(")
                cscore += 2
        if(uscore == cscore):
            print("Match Draw!")
        elif(uscore > cscore):
            print(f"You won by {uscore-cscore} points!!")
        else:
            print(f"Computer won by {cscore-uscore} points!!")
    else:
        print("Enter valid input!")