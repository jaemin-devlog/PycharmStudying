# 기본 출력
print("Hello, World!")  # Hello, World!
print(1, 2, 3)  # 1 2 3

# sep : 구분
print(1, 2, 3, sep=", ")
print("a", "b", "c", sep="")
print("year", "month", "day", sep=" / ")

# end : 줄바꿈
print("Hello", end=" ")
print("World!")

# sys.stdout.write()
import sys

sys.stdout.write("Hello World!\n")

# f-string
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old")

# list, dictionary
arr = [1, 2, 3, 4, 5]
print(*arr)
print(" ".join(map(str, arr)))

#sys.stdin.readline() + print()
#input보다 sys.stdin.readline()이 속도가 더 빠름

n = int(sys.stdin.readline())
print(n)

s = sys.stdin.readline().strip()
print(s)

