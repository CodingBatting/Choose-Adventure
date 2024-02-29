
print("Welcome to Knight's adventure! You will set on the quest to save the Princess from evildoers!")
print("Travel into the castle, facing obstacles along the way, and always think before you go!")
name = input("First, What is your name?")
print("Ah, so your name is", name)

stance = input("Are you ready? (yes/no)")

if stance.lower().strip() == "yes":
    print("Great! You have entered the entrance of the castle. Strangely, the entrace is left opened, as if they were expecting you")
    print("You entered the castle cautiously. You found an obvious pit trap laiding in the open. Do you jump or use the rope and hook?")
    choice = input("jump or rope and hook?")
    if choice.lower().strip() == "rope and hook":
        print("As you throw your rope and hook, the hook fall into the second pit trap. You were somehow glad you didn't make the decision to jump")
        print("You retrieved your rope and hook and throw it again. it landed at the other side, you tied the other end of the rope onto another hook on your side")
        print("You cross the double fall by swinging your arms like a monkey. you travel deeper into the castle")
        print("There is a bridge. it look old and about to be broken.")
        choice = input("would you like to cross?")
        if(choice.lower().strip() == "no"):
            print("You noticed that there are stairs. oops. you climb up the stairs")
            print("you find a locked door. what are you going to do")
            choice = input("charge in/pick lock?")
            if(choice.lower().strip() == "pick lock"):
                print("you managed to unlocked the door, effectively disabling the trap")
                print("The princess was sitting at her bed. When she saw you, she jump at your direction")
                print("effectively embracing her in your arms. You found it strange that there is no evildoars around")
                print("regardless, you carried the princess out of the castle and live happily ever after....or is it?")
        else:
            print("The bridge broke and you fell to the abyss. Game Over")
    else:
        print("You fell into the second pit trap and died. Oops.... Game Over")
else:
    print("Come Back when you are ready.")