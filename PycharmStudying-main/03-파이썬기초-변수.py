x = 10  # 정수 할당
y = 3.14  # 실수 할당
name = "Alice"  # 문자열 할당
is_valid = True  # 불리언 (참/거짓) 값 할당


a = 5
b = a  # b에 a의 값을 복사
print(b)  # 5 출력

num = 42  # 정수 (int)
pi = 3.14159  # 실수 (float)
text = "Python"  # 문자열 (str)
is_happy = True  # 불리언 (bool)
arr = [1, 2, 3]  # 리스트 (list)
person = {"name": "Bob", "age": 25}  # 딕셔너리 (dict)

print(type(num))  # <class 'int'>
print(type(text))  # <class 'str'>
print(type(arr))  # <class 'list'>


a, b, c = 1, 2, 3
print(a, b, c)  # 1 2 3


a, b = 10, 20
a, b = b, a  # 값 교환
print(a, b)  # 20 10

#🎯 7. 변수 활용 예제 (코딩 테스트 스타일)
#📌 7-1. 두 개의 숫자 입력받아 변수에 저장 후 합 출력
a, b = map(int, input().split())
print(a + b)


n = int(input())  # 숫자 개수 입력
arr = list(map(int, input().split()))  # 리스트 입력
total = sum(arr)  # 리스트의 합 계산
print(total)
