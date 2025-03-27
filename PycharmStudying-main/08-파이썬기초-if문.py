score = int(input("점수 입력 >> "))

if score < 0 or score > 100:
    print("유효한 점수를 입력하세요.")
elif score >= 90:
    print("학점 : A")
elif 80 <= score < 90:
    print("학점 : B")
elif 70 <= score < 80:
    print("학점 : C")
elif 60 <= score < 70:
    print("학점 : D")
else:
    print("학점 : F")
