import random

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def present_question(self, question):
        print(question['question'])
        for idx, option in enumerate(question['options'], start=1):
            print(f"{idx}. {option}")

    def evaluate_response(self, question, response):
        correct_answer = question['answer']
        if response == correct_answer:
            self.score += 1
            print("Correct!\n")
        else:
            print(f"Incorrect. The correct answer is: {correct_answer}\n")

    def play(self):
        print("Welcome to the Quiz Game!")
        print("Rules:")
        print("a. Answer each question by typing the number of your choice.")
        print("b. At the end of the quiz, your score will be displayed.\n")

        while self.questions:
            current_question = self.questions.pop(0)
            self.present_question(current_question)
            user_response = input("Your answer: ")

            try:
                user_response = int(user_response)
                if 1 <= user_response <= len(current_question['options']):
                    self.evaluate_response(current_question, user_response)
                else:
                    print("Invalid choice. Try again.\n")
                    self.questions.append(current_question)
            except ValueError:
                print("Invalid input. Try again.\n")
                self.questions.append(current_question)

        print("Quiz Finished!")
        print(f"Your final score is: {self.score}/{len(questions)}")

def play_again():
    play_again = input("Do you want to play again? (yes/no): ").lower()
    return play_again == 'yes'

# Sample questions (replace with your own)
questions = [
    {
        'question':'What is the pH value of the human body?',
        'options':['9.2 to 9.8','7.0 to 7.8','6.1 to 6.3','5.4 to 5.6'],
        'answer':2
    },
    {
        'question': 'Pustaz grasslands are situated at?',
        'options':['South Africa','China','Hungary','USA'],
        'answer': 3
    }
]

while True:
    random.shuffle(questions)
    quiz_game = QuizGame(questions)
    quiz_game.play()
    
    if not play_again():
        break

print("Thank you for playing! Goodbye.")
