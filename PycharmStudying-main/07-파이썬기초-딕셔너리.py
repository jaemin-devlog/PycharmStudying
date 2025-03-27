fruit = {"사과" : 1000, "포도" : 2000, "오렌지" : 3000}
print(fruit["사과"])

#딕셔너리 원소 추가
fruit["바나나"] = 4000
print(fruit)

#딕셔너리 원소 수정
fruit["사과"] = 5000
print(fruit)

#딕셔너리 원소 삭제
del(fruit["사과"])
print(fruit)

# 딕셔너리 관련 함수
print(fruit.items())
print(fruit.keys())
print(fruit.values())
