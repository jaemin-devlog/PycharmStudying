# 리스트의 요소를 하나씩 출력하는 for문
fruits = ["사과", "바나나", "체리"]
for fruit in fruits:
    print(fruit)

# 문자열의 문자 하나씩 출력하는 for문
text = "Python"
for char in text:
    print(char)

# 튜플의 요소를 하나씩 출력하는 for문
numbers = (1, 2, 3, 4, 5)
for num in numbers:
    print(num)

# 딕셔너리의 키와 값을 출력하는 for문
scores = {"철수": 90, "영희": 85, "민수": 80}
for name, score in scores.items():
    print(f"{name}의 점수: {score}")

# 리스트 내부의 리스트를 순회하는 중첩 for문
matrix = [[1, 2], [3, 4], [5, 6]]
for row in matrix:
    for value in row:
        print(value)





