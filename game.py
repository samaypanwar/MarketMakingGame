import json

class MarketMaker:

    def __init__(self, max_num_guesses: int = 5, error_percentage: float = 0.1):

        self.max_num_guesses = max_num_guesses
        self.error_percentage = error_percentage

    def load_questions(self):

        print("Loading Question Bank Questions...")
        with open("question_bank.json") as file:
            self.result = json.load(file)

    def play(self):

        if not self.result:
            raise ValueError("No Question Bank Questions Loaded Yet!")

        count = 0
        max_true_loss = 0
        user_position = 0
        is_liquid = False

        question = min(self.result, key = lambda x: x['Count'])
        question_idx = self.result.index(question)
        self.result[question_idx]['Count'] += 1

        print("Let us play the game!!")
        print("--------------------------------")
        print("Question: ", question.get('Question'))

        while count < self.max_num_guesses and not is_liquid:

            bid = float(input("Bid: "))
            ask = float(input("Ask: "))
            count += 1

            if bid > question.get('Answer'):
                print("I will sell to you @", bid)
                user_position += 1

            elif ask < question.get('Answer'):
                print("I will buy from you @", ask)
                user_position -= 1

            else:
                print("Your market is correct...", end="")

                if (ask - bid) / question.get('Answer') > self.error_percentage:
                    print("However your market is too wide")

                else:
                    print("Congratulations! you've made the market liquid")
                    is_liquid = True

        else:
            if not is_liquid:
                print("You have run out of guesses!")

            else:
                expected_user_position = int(input("Please state your position at the end of this game: "))

                while expected_user_position != user_position:
                    print("Wrong user position!, please try again")
                    expected_user_position = int(input("Please state your position at the end of this game: "))

                else:
                    print("Correct user position!")

        print("-------------------------------------------")
        print("We have come to the end of the game")
        print("Goodbye!")

        with open("question_bank.json") as file:

            json.dump(self.result, file)

















