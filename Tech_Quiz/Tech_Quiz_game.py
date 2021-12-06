import json
import requests
import pprint as pp
import random
import html

# API from https://opentdb.com/api_config.php
url = "https://opentdb.com/api.php?amount=50&category=18"
endgame = ""
score_correct = 0 
score_incorrect = 0 

while endgame != "quit":
    r = requests.get(url)
    if (r.status_code != 200):
        endgame = input("There was issue retrieving the question from API ! Please try again or Quit the game by typing 'quit' ")
    else:
        valid_answer = False    
        answer_num = 1
        data = json.loads(r.text)
        question = data["results"][0]["question"]
        answers = data["results"][0]["incorrect_answers"]
        correct_answers = data["results"][0]["correct_answer"]
        answers.append(correct_answers)
        # Shuffle the Answers
        random.shuffle(answers)

        # Translate the HTML Code Tags using html.unescape
        print(html.unescape(question) + "\n")
        
        for answer in answers:
            print(f"{str(answer_num)} - {html.unescape(answer)}")
            answer_num += 1
        
        # Invalid input Check
        while valid_answer == False:
            user_answer = input("\nType the number of the correct answer: ")
            
            try:
                user_answer = int(user_answer)
                if user_answer > len(answers) or user_answer <= 0:
                    print("Invalid Answer")
                else:
                    valid_answer = True
            except:
                print("Invalid answer. Use only numbers.")
                
        # Number Assignment to options
        user_answer = answers[int(user_answer)-1]
        # Answers Validation
        if (user_answer == correct_answers):
            print("Correct Answer buddy XD")
            score_correct += 1
            
        else:
            print("Oppps Wrong Answer !!")
            print(f"The Correct answer is {correct_answers}")
            score_incorrect += 1
        print("#########################################")
        print(f"Your Score is {score_correct}")
        print(f"You have {score_incorrect} incorrect answers")
        print("#########################################")
    endgame = input("Press Enter to Jump into Next Question or type 'quit' to exit: ").lower()

print("\nThank You For Playing XD")
    
        
