import random, sys


words_five_letters = []


def load_words(filename):
    with open(filename, "r") as file:
        return [line.strip() for line in file if len(line.strip()) == 5]


def man():
    print("""
          ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
          Wordle But Python (CLI) works similarly to the known version, but notable changes are the usage of a CLI (Command Line Interface) and 
          the option to choose your own word to guess. 
          
          The word you are guessing is the solution word. The guess you submit is the guess word. If you get a letter right and it is in the correct position,
          you will get a g, or green, indicating it is correct. A y, or yellow, indicates that the letter is correct but not in the right position. 
          If the letter is blank, that means that the letter does not occur in the solution. Try a different one.
          
          There are only six (6) tries. Good luck.
          ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
          """)

    return
          

def wordle_check(solution_word, guess_word):
    print("pass w_c")

#runs if the user chooses "START" on the "main menu"
def wordle_setup():
    solution_word = None 

    while solution_word is None:
        gamemode_choice = input("Random word (RANDOM) or choose your own? (CHOOSE) >>>").strip().lower()
        if gamemode_choice == "random" or gamemode_choice == "rand" or gamemode_choice == "r":
            solution_word = random.choice(words_five_letters)

        elif gamemode_choice == "choose" or gamemode_choice == "c":
            length_choice = None

            while length_choice is None:
                length_choice = input("Classic word length (5 chars long) or free word length? [CLASSIC][FREE] >>>").strip().lower()
                if length_choice == "classic" or length_choice == "c":
                    print("-Classic Selected-")
                    free_length = False

                elif length_choice == "free" or length_choice == "f":
                    print("-Free Selected-")
                    free_length = True
                
                else:
                    print("Invalid input. [CLASSIC][FREE]")
                    length_choice = None
            
            valid_word = None

            while valid_word is None:
                solution_word = input("Enter wordle solution word: >>>")
                if free_length == False:
                    if len(solution_word) != 5 or not solution_word.isalpha():
                        print("Invalid word. Maybe you used a non-alphabet character, or the length is not 5 characters long.")
                    else:
                        valid_word = True

                elif free_length == True:
                    if not solution_word.isalpha():
                        print("Invalid word. Maybe you used a non-alphabet character?.")
                    else:
                        valid_word = True
        else:
            print("Invalid input. [Try RANDOM] or [CHOOSE] to continue. >>>")

        print(f"\n-solution word selected-")
        #print(f"solution word: {solution_word}")
        return solution_word

          
def main_game(sol_wd):
    guess_count = 0
    game_status = None
    
    while game_status == None:
        guess = input("\nenter guess: >>>")

        length_1 = len(sol_wd)
        length_2 = len(guess)

        if length_1 != length_2:
            print(f"Invalid word length. Solution length is {length_1} ")

        else:
            guess_count += 1
            output_list = []

            for i in range(0,length_1):
                if guess[i] == sol_wd[i]:
                    output_list.append("g")
                elif guess[i] in sol_wd:
                    output_list.append("y")
                else:
                    output_list.append("_")

            print("   ")
            print(f"{output_list}   {guess_count}")

            if guess == sol_wd and guess_count <= 6:
                print("Correct!")
                game_status = "win\n"
                print(game_status)
            
            if guess_count == 6:
                print("\nOut of guesses!")
                print(f"Correct word was: {sol_wd}")
                game_status = "lose\n"
                #print(game_status)


def exit_program():
    sys.exit("Exiting program...")


def main_menu():
    while True:
        user_input = input("Type START to play, MAN to see how to play, EXIT to quit >>>").strip().lower()
        #print(user_input)

        if user_input == "man":
            man()

        elif user_input in ["exit", "quit"]:
            exit_program()

        elif user_input == "start":
            solution_word = wordle_setup()
            if solution_word != None:
                main_game(solution_word)

        else:
            print("Command not recognized. Capitalization does not matter, but spelling does.")


if __name__ == "__main__":
    words_five_letters = load_words("five_letter_words.txt")
    print("""
-----------------------------------------
Wordle But Python (CLI) by Isaac De Silva
-----------------------------------------
   """)

    main_menu()
