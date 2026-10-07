from questions import questions, answers

from score import getMark

userAnswers = []

for question in questions:
    print(question)
    answer = input("Answer: ")
    userAnswers.append(answer)

print(f"Congrats! Your final score is {getMark(userAnswers)}")