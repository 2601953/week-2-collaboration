import questions

def getMark(answers):
    total = 0
    try:
        for i in range(0, len(questions.answers)):
            if answers[i] == questions.answers[i]:
                total += 1
        return total
    except:
        print("invalid array size")
        return -1