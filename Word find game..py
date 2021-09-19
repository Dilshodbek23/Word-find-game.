from uzwords import words
from function import get_word
from display import display
uz_word = get_word()
all_enterned_letters = ""
count = 0
print(f"My word consists of {len(uz_word)} letters. Can you find it?")
while True:
    enterned_letter = input("Enter letter\n>>>")
    count += 1
    if enterned_letter in all_enterned_letters:
        print("You entered this letter earlier. Please enter a another letter.")
    if enterned_letter in uz_word:
        print(f"Letter {enterned_letter.upper()} is correct")
        all_enterned_letters += enterned_letter
        check = display(all_enterned_letters, uz_word)
        if "-" not in check:
            print(f"Congratulations! You found the word {uz_word} after {count} tries.")
            break
    else:
        print("There is no such letter.")
        all_enterned_letters += enterned_letter
    print(check)
    print("All the letters you entered are: ", all_enterned_letters)
    print()


print("Game over")
