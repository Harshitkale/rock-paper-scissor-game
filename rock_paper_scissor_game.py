import random
print("-----------ROCK-PAPER-SCISSOR-GAME-------------\n")
#while loop make the code to run itself again and again
while True:
    print("************************************************************************************************************\n")
    #enter proper choice that is required
    person=input("Choice rock,paper,scissor: ").lower()
    #print("") for spacing
    print(" ")
    # print("************************************************************************************************************")
# if the enter value is different from the required input it will give warning and tell user to reenter the value
    if person != 'rock' and person != 'paper' and person !='scissor':
        print("************************************************************************************************************")
        print("Plz choice from rock/paper/scissor!!!\n")
        print("************************************************************************************************************")
        continue
    print("************************************************************************************************************")
#it use random module to give random output
    choices=('rock','paper','scissor')
    computer=random.choice(choices)
    print("BOT ==>",computer)
    #check condition for win or loose
    if person == computer:
        print("result ==>tie😒!!")
    elif person == 'rock' and computer == 'scissor':
        print("result ==>you win🎉🎉!!")
    elif person == 'paper' and computer == 'rock':
        print("result ==>you win🎉🎉!!")
    elif person == 'scissor' and computer == 'paper':
        print("result==>you win🎉🎉!!")
    elif computer == 'rock' and person == 'scissor':
        print("result==>you loose😣!!")
    elif computer == 'paper' and person == 'rock':
        print("result ==>you loose😣!!")
    elif computer == 'scissor' and person == 'paper':
        print("result ==>you loose😣!!")
