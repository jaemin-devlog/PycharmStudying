foo = "Hello"
print("Hello" + "world")
print("Hello" * 3)
foo1 = 'Hello'
print(foo)
print(foo1)
print("개가 멍멈 짓는다.")
print('개가 "멍멍" 짓는다.')
foo = """개가
멍멍
짓는다."""
print(foo)
foo = "Hello World"
#문자열 길이
print(len(foo))
#글자 바꾸기
print(foo.replace("Hello","Python"))
#양쪽 공백 지우기
print("      Hello World          ".strip())
#공백 단위로 나누기
print("Hello World hello python".split())
print("Hello,World,hello,python".split(","))
#문자열 속 글자 세기
print(foo.count("l"))
#대문자로 변환하기
print(foo.upper())
#소문자로 변환하기
print(foo.lower())
#in, not in
print("hello" in "hello world")
print("fdsfsdf" not in "hello world")