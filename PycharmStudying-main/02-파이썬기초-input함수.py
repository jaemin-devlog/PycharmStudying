# #기본 입력 input()
# name = input("이름을 입력하시오 : ")
# print(name)
#
# #input()은 항상 문자열(str)로 입력을 받음.
# #숫자를 입력받고 싶다면 int(), float()로 변환해야함
# num = int(input("정수 입력 : "))
# print(num * 2)
#
# num = float(input("실수 입력 : "))
# print(num)

#빠른 입력
#sys.stdin.readline()
#input은 속도가 느려서, 반복문에서 여러 줄 입력 받을 때
#sys.stdin.readline()을 쓰는게 효과적
#sys.stdin.readline()은 개행문자(\n)까지 포함하여 입력됨.
#strip()을 사용하여 개행문자를 제거하는 것이 일반적
# import sys
# data = sys.stdin.readline().strip() #개행 문자 제거
# print(data)
#
#
# #여러 개의 값 입력받기(공백 구분)
# #split()을 사용하면 공백을 기준으로 여러 개의 값을 나눠서 입력받을 수 있음
# #map(int, input().split())을
# a, b = map(int, input("a, b를 입력 : ").split())
# print(a,b)
#
# a, b = map(int, input("a, b = ").split())
# print(f"{a} {b} -> a = {a}, b = {b}")

#list로 여러 개의 값 입력 받기
# arr = list(map(int, input().split()))
# print(*arr, f"arr -> = {arr}")

#여러 줄 입력받기
#for문을 이용한 입력방법
# n = int(input("몇개를 입력하시겠습니까? ")) #입력 받을 줄 수
# arr = [input("입력 : ").strip() for _ in range(n)]
# print(arr)

#sys.stdin.readline()을 이용한 빠른 여러 줄 입력
# import sys
# n = int(sys.stdin.readline())
# arr = [sys.stdin.readline().strip() for _ in range(n)]
# print(arr)

#고정 개수의 숫자 입력받기 (공백 기준)
# a, b, c = map(int, input().split())
# print(a,b,c)
#
# # N개의 숫자 입력받기 ->리스트로 저장
# n = int(input("입력받을 개수 입력 : "))
# arr = list(map(int, input().split()))
# print(arr)

#문자열 여러 개 입력받기
words = input("문자열 입력").split()
print(words)