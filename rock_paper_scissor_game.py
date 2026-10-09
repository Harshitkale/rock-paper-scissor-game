import random
print("-----------ROCK-PAPER-SCISSOR-GAME-------------\n")

while True:
    print("************************************************************************************************************\n")
    person=input("choice rock,paper,scissor: ").lower()
    print(" ")
    # print("************************************************************************************************************")

    if person != 'rock' and person != 'paper' and person !='scissor':
        print("************************************************************************************************************")
        print("plz choice from rock/paper/scissor")
        print("************************************************************************************************************")
        continue
    print("************************************************************************************************************")

    choices=('rock','paper','scissor')
    computer=random.choice(choices)
    print("BOT ==>",computer)
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
