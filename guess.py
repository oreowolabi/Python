# Building a Guessing Game
# Basically, the player guesses the surnames of the President of 7 countries
#  Countries are: Nigeria, Rwanda, USA, Russia, France, China, and Turkey

# Create a list of words game players would choose from
# import random
#
# words = ["Macron", "Putin", "Biden", "Buhari", "Jinping", "Erdogan", "Kagame"]
#
# # randomly choose any of the listed words
# word = random.choice(words)
# # let's see the word
# # print(word)
# # erm, cause we don't want the user to know the word...
#
# # Let's add hints
# if word == "Macron":
#     print("Hint: President at 39")
# elif     word=="Biden":
#     print("Hint: Sleepy Joe")
# elif    word == "Erdogan":
#     print("Hint: Instanbul, not constantinople")
# elif     word == "Buhari":
#     print("Hint: Baba go slow, UK resident")
# elif     word == "Jinping":
#     print("Hint: Belt and Road")
# elif word == "Kagame":
#     print("small but mighty, even after a genocide")
# elif word == "Putin":
#     print("Foolishly invaded Ukraine")
#
#
#
# print("Guess the surname of the president of any of these countries - "
#       "Rwanda, China, France, USA, Russia, Nigeria, Turkey")
#
#
# guess = input("Enter a guess: ")
#
# def guess_counter(guess,word):
#     track = 0
#     while track != 3:
#         if guess != word:
#             track = guess.count(guess)
#             print("Congrats, the answer is " + word + "!")
#         else:
#            print("success!")

    # I was able to get inputs and note if it was right or wrong. I was able to allow multiple inputs but I couldnt get them to stop when right.


#  It's a new day, let's see get this working!
# start from scratch...
#
import random

words = ["Macron", "Putin", "Biden", "Buhari", "Jinping", "Erdogan", "Kagame"]

word = random.choice(words)
# print(word)



print(" Guess the surname of the president of any of these countries: \n "
      "Rwanda, China, France, USA, Russia, Nigeria & Turkey \n"
      " You have 3 tries. Good luck! ")

# Adding hints
if word == "Macron":
    print("Hint: President at 39")
elif     word=="Biden":
    print("Hint: Sleepy Joe")
elif    word == "Erdogan":
    print("Hint: Instanbul, not constantinople")
elif     word == "Buhari":
    print("Hint: Baba go slow, UK resident")
elif     word == "Jinping":
    print("Hint: Belt and Road")
elif word == "Kagame":
    print("small but mighty, even after a genocide")
elif word == "Putin":
    print("Foolishly invaded Ukraine")

guess = input("Enter a guess: ")

guesses_left = 3

#  The code below worked, so I'll just keep it here as reference...
# while guesses_left != 0:
#     if guess != word:
#         guesses_left = guesses_left - 1
#     if guess != word:
#         print("Wrong, Try again")
#         guess = input("Enter a guess: ")
#         print(str(guesses_left) + " guesses left")
#     elif guess == word:
#         print("You got it")


# Let's try it again
# if guess != word:
#       guesses_left = guesses_left - 1
# print(guesses_left)

while guesses_left != 1 and guess != word:
    if guess != word:
        guesses_left = guesses_left - 1
        print("Wrong, Try again.You have " + str(guesses_left) + " guesses left")
        guess = input("Enter a guess: ")
if guesses_left == 1:
    print(" Sorry, You are out of guesses. Try Again")
if guess == word:
    print("Congrats! You got it!")


# I think my game is ready!



