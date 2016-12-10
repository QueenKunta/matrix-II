#import header files
from cop import Cop
from morpheus import Morpheus
from Trinity import Trinity
from agentbrown import AgentBrown

def main():
    #ask user if they would like to play
    print("Would you like to help Trinity make a run for it?")
    player = input('Yea or Nah ')
    if player == 'Yes' or player == 'yes' or player == 'Y' or player == 'y' or player == 'Yea' or player == 'yea' or player == 'Ye' or player == 'ye':
        play()

    else:
        print("Bye!")
        
def play(): #scene
    #declare linkers
    aCop = Cop()
    bMorpheus = Morpheus()
    cTrinity = Trinity()
    dAgent = AgentBrown()
    
    bMorpheus.morpheus1()
    bMorpheus.morpheus3()
    bMorpheus.morpheus4()
    cTrinity.escape1()
    answer1=input("If you choose to wait press 1. \nIf you choose to shoot press 2. ")
    aCop.setQuantity(answer1)
    answer1 = aCop.verify()
    if (answer1==1):
        print("Good, you caught him off guard!")
    elif (answer1==2):
        print("The cops shoot you so much you die.")
        print("The End.")
        go_on()
        
    print("Meanwhile...")
    dAgent.bar()
    dAgent.cop_scene()
    print("Hey, I'm just doing my job. You give me juris-my diction crap, you can cram it up your ass.")
    dAgent.cop_scene2()
    print("I think we can handle one little girl....I sent two units. They're bringing her down now.")
    dAgent.cop_scene3()
    dAgent.cop_scene4()
    dAgent.alley()

    cTrinity.escape2()
    answer2=input("To kick them so good, press 1. \nTo stand there and get shot press 2. ")
    aCop.setQuantity(answer2)
    answer2 = aCop.verify()
    if (answer2==1):
        print("Good job! You've beat them all up!")
        print("You run out of the room and find an exit...")
    elif(answer2==2):
        print("You died by being shot.")
        go_on()
    dAgent.trinityspotted()
    print("\n")

    cTrinity.escape3()
    answer3=input("Press 1 to take a short break. \nPress 2 to keep climbing. ")
    aCop.setQuantity(answer3)
    answer3 = aCop.verify()
    if(answer3==1):
        print("You died because he shot you so many times.")
        print("The End.")
        go_on()
    elif (answer3==2):
        print("Good job! He didn't get a chance to shoot you!")
        print("You are alive!")       

    cTrinity.escape4()
    answer4=input("Press 1 to jump. \nPress 2 to jump. ")
    aCop.setQuantity(answer4)
    answer4 = aCop.verify()
    if (answer4==1):
        print("You've jumped over and made it! You keep running!")
    elif(answer4==2):
        print("You've jumped but didn't make it! You got shot so many times you died.")
        print("The End.")
        go_on()

    cTrinity.escape5()
    answer5=input("Let's leave this to your instincts.... \nPress 1. \nPress 2. ")
    aCop.setQuantity(answer5)
    answer5 = aCop.verify()
    if (answer5==1):
        print("You died, because he shot you so many times you died.")
        print("The End.")
        go_on()
    elif(answer5==2):
        print("Good job you survived!")        

    cTrinity.escape6()
    answer6=input("Press 1 to jump. \nPress 2 to jump. ")
    aCop.setQuantity(answer6)
    answer6 = aCop.verify()
    if (answer6==1):
        print("Good job, I don't know how you made it but you did.")
    elif(answer6==2):
        print("You fell so hard, you died... sorry m8.")
        print("The End.")
        go_on()

    cTrinity.escape7()
    answer7=input("Press 1 to jump into a window. \nPress 2 to keep running. ")
    aCop.setQuantity(answer7)
    answer7 = aCop.verify()
    if(answer7==1):
        print("Good job you somehow jumped into a random window fam")
    elif(answer7==2):
        print("You died dude. Just stop. Uninstall program. Thanks.")
        print("The End.")
        go_on()

    cTrinity.escape8()
    answer8=input("Press 1 to hold your fire. \nPress 2 to shoot your gun. ")
    aCop.setQuantity(answer8)
    answer8 = aCop.verify()
    if(answer8==1):
        print("Good job you didn't shoot your gun! They don't know where you are yet!")
    elif(answer8==2):
        print("They found you and shot you and you died.")
        print("The End.")
        go_on()

    cTrinity.escape9()
    answer9=input("Press 1 to run and find another phone booth. \nPress 2 to take a risk and run for the phone. ")
    aCop.setQuantity(answer9)
    answer9 = aCop.verify()
    if(answer9==1):
        print("You got shot so many times you died.")
        print("The End.")
        go_on()
    elif(answer9==2):
        print("You ran so hard and picked up the phone!")
        print("You've made it!")

    go_on() #ask user if they would like to play again

def go_on():
    print("Thanks for playing! Would you like to play again?")
    user = input('Yea or Nah ')
    if user == 'Yes' or user == 'yes' or user == 'Y' or user == 'y' or user == 'Yea' or user == 'yea' or user == 'Ye' or user == 'ye':
        print('You said yes!')
        play()

    else:
        print('Bye!')
        main()
main()
