import time
import csv
import random
import winsound

name = input("What is your name? ")

print("Hi, " + name, "Time to play hangman game!")

print()

time.sleep(1)

print("Start Loading...")
print()
time.sleep(0.5)

words = []
with open('./resource/word_list.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for c in reader:
        words.append(c)

random.shuffle(words)
q = random.choice(words)

word = q[0].strip()
# print(word)

guesses = ''

turns = 10

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=' ')
        else:
            print("_",  end=' ')
            failed += 1

    if failed == 0:
        winsound.PlaySound('./sound/good.wav', winsound.SND_FILENAME)
        print()
        print()
        print('Congraturation! Your guess is correct.')

        break
    print()

    print()
    print('Hint: {}\n'.format(q[1].strip()))
    guess = input("Guess a character: ")
    guesses += guess

    if guess not in word:
        turns -= 1
        winsound.PlaySound('./sound/bad.wav', winsound.SND_FILENAME)
        print("Ooops! Wrong")
        print("You have", turns, 'more gueeses!')

    if turns == 0:
        print("You hangman game failed. Bye!")
