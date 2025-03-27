# list
name = ["철수", "짱구", "영구"]
print(name[0])
print(name[2])

print(name + ["영희", "민수"])
print(name[0] * 3)

# list 관련 함수
name.append("영희") #원소 추가
print(name)
name.remove("철수") #원소 제거
print(name)
name[0] = "헐크"    #원소 수정
print(name)
#원소의 개수
print(len(name))
#원소 정렬
name.sort(reverse=True) # reverse=True : 내림차순 정렬
print(name)

#python 출력
foo = [1,2,3, ["foo","hello", ["world","python"]]]
print(foo[3][2][1])
