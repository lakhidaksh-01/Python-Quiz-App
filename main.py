# Python Quiz App program
while True:
 Questions = (
    "Which planet is known as the Red Planet?",
    "Who developed the theory of relativity?",
    "What is the capital of Japan?",
    "Which element has the chemical symbol ‘O’?",
    "What is the largest ocean on Earth?",
    "Which programming language is known for its snake logo?",
    "What does ‘HTTP’ stand for?",
    "Who painted the Mona Lisa?",
    "What is the hardest natural substance on Earth?",
    "Which gas do plants absorb from the atmosphere?"
 )

 Options = (
    ("A. Earth", "B. Mars", "C. Jupiter", "D. Venus"),
    ("A. Isaac Newton", "B. Albert Einstein", "C. Nikola Tesla", "D. Stephen Hawking"),
    ("A. Beijing", "B. Seoul", "C. Tokyo", "D. Bangkok"),
    ("A. Oxygen", "B. Gold", "C. Silver", "D. Carbon"),
    ("A. Atlantic Ocean", "B. Indian Ocean", "C. Pacific Ocean", "D. Arctic Ocean"),
    ("A. Java", "B. Python", "C. C++", "D. Ruby"),
    ("A. HyperText Transfer Protocol", "B. High Transmission Text Protocol", "C. Hyper Transfer Text Process", "D. Hybrid Transfer Protocol"),
    ("A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Claude Monet"),
    ("A. Gold", "B. Diamond", "C. Iron", "D. Quartz"),
    ("A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen")
 )

 Answers = ("B", "B", "C", "A", "C", "B", "A", "C", "B", "C")
 score=0
 quesNum=0
 guesses=[]

 for question in Questions:
    print("---------------------")
    print(question)
    for option in Options[quesNum]:
        print(option)
    
    guess=input("Enter (A,b,C,D): ").upper()
    guesses.append(guess)

    if guess == Answers[quesNum]:
        score+=1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"Correct answer is {Answers[quesNum]}")

    quesNum=quesNum+1




 print("---------------------")
 print("       RESULT        ")
 print("---------------------")

 print("Correct Answers: ")
 for answer in Answers:
    print(answer,end=" ")
 print("")

 print("Your Guesses: ")
 for guess in guesses:
    print(guess,end=" ")
 print("")

 print(f"Your score is : {score}/{len(Questions)}")


 retry = input("Do you want to play again? (yes/no): ").lower()
 if retry != "yes":
    print("Thanks for playing!")
    break