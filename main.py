# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from game import MarketMaker


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mm = MarketMaker()
    mm.load_questions()
    mm.play()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

"""
Load question bank,

shuffle the questions

present question to user

while num_guess < 5 and user out of range:
    either buy or sell depending on direction of interest
    keep count of the max true loss and net user and agent position
    
    return position of user, return true value of question

ask would you like a new question
continue

shift question asked into new dict for known questions and keep count of the number of times asked
"""