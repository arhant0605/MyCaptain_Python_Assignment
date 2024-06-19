def answer_to_the_universal_question()
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    if answer == '42' or answer.lower() == 'forty two' or answer.lower() == 'forty-two':
        print("Yes")
    else:
        print("No")

answer_to_the_universal_question()
