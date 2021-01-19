# Write your code here
import random
print("H A N G M A N")

while True:
    command = input("Type \"play\" to play the game, \"exit\" to quit: ")
    
    if command == 'play':
        
        answer = random.choice(['python', 'java', 'kotlin', 'javascript'])
        dash = '-' * len(answer)

        mistakes = 0
        newdash = list(dash)
        already_played = ''

        while True:
            guesses = ''.join(newdash)
            print('\n' + guesses)

            guess = input("Input a letter: ")
            guess_answer = guess in answer
            guess_played = guess in already_played
            
            
            if len(guess) == 1:
                if guess.isupper() or not guess.isalpha():
                    print("Please enter a lowercase English letter")
                    continue
                
            if len(guess) > 1:
                print("You should input a single letter")
                continue
                
            if guess_played:
                print("You've already guessed this letter")
                continue

            already_played += guess
            
            if guess_answer:
                for idx, letter in enumerate(answer):
                    if guess == letter:
                        newdash[idx] = letter
            
            if not guess_answer and mistakes < 7 and not guess_played:
                print("That letter doesn't appear in the word")
                mistakes += 1
                continue
                

            if answer == ''.join(newdash):
                print('\n' + ''.join(newdash))
                print("You guessed the word!\nYou survived!")
                break

            if (not guess_answer or guess_played) and mistakes == 7:
                mistakes += 1
                
                if not guess_answer:
                    print("That letter doesn't appear in the word")
                if guess_played:
                    print("No improvements")
                if mistakes == 8:
                    print("You lost!")
                    break
    else:
        break