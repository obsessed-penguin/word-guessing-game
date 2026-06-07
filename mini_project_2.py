from random import choice

print("System activation.........")


def starts():
    while True:
        answer = input("Do you want to play 'Word Guessing Game'? ")

        if answer.lower() in ["yes", "i want to", "exactly", "sure", "maybe", "yeah"]:
            print("Let's start!\n")
            return game()
        
        elif answer.lower() in ["no", "nope", "not at all", "never", "nono"]:
            print("We will definitely play next time!\n")
            break

        else:
            print("Unfortunately, your request could not be processed. You might have made a mistake. Please enter the text correctly!\n")
            

def game():
    while True:
        try_count = 1
        words_pool = ["apple", "actor", "adult", "agent", "alarm", "album", "angel", "anger", "arrow", "audio", "address", "academy", "account", "airline", "airport", "animals", "apricot", "artwork", "average", "avocado", "algorithm", "advantage", "adventure", "ambulance", "anonymous", "apartment", "applause", "architect", "astronaut", "attention"]
        word = choice(words_pool)
    
        print("The program has thought of a word that starts with the letter A.", "Try to guess it!", sep="\n")
  
        while True:
            info = input().lower()
            
            if info in ["idk", "idontknow", "i dont know", "i don't know"]:
                print("I beat you this time!", f"The secret word is: {word}")
                break

            elif info == word:
                print("You guessed the answer correctly!", f"It took you {try_count} shots to get it.", sep="\n")
                break

            else:
                print("Wrong word! Try again!")

            try_count += 1

                        
        if (input("Type 'yes' if you want to restart the round or start a new game: ")).lower().strip() in  ["yes", "i want to", "exactly", "sure", "maybe", "yeah"]:
            continue
        else:
            print("It was a pleasure playing with you!", "See you next time!\n", sep="\n")
            break
        

starts()