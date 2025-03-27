import random

answer = random.randint(1, 200)

while True:
    ChoiceNum = int(input("정답을 입력하세요 >> "))

    if ChoiceNum > answer:
        print(f"{ChoiceNum}보다 Down!")
    elif ChoiceNum < answer:
        print(f"{ChoiceNum}보다 Up!")
    else:
        print("정답입니다!")
        break
