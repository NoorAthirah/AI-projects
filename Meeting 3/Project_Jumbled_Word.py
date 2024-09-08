import random
  
score = 0
player_name = input("Please enter your name: ") 

while True:
        
    words = ["python", "computer", "programming",
             "condition", "else", "break", "input",
             "print", "while", "for"] 
    pick = random.choice(words)

    random_word = random.sample(pick, len(pick)) 
    jumbled = "".join(random_word)
    print("Jumbled word is :", jumbled)

    answer = input("what is in your mind? ")

#                                   1
#----------------------------------------------------------------
    if answer == pick:
        score += 1
        print("Your score is :", score)
#----------------------------------------------------------------
#                                   2
#----------------------------------------------------------------
        if score == 10:
            print("Congratulation ",player_name , "you win!")
            print("Your score is :", score)
            break 
#----------------------------------------------------------------
#                                   3
#----------------------------------------------------------------
    else:
        print("Better luck next time... correct word is :", pick)    

        cont = input("press 'y' to continue and 'n' to quit : ") 
        if cont == "n":
            print(player_name, "Your score is :", score)
            print("Thanks for playing...")
            break 
#-----------------------------------------------------------------

"""random.sample() ensures that each character sampled 
from pick is unique within the sampled list. This is crucial 
because in a word jumble game, you don't want repeated characters
 in the jumbled word. For instance, if pick is "programming", using
   random.sample() ensures that each character in "programming" appears 
   exactly once in the jumbled output."""