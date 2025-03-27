while True:
    foo = input("여기에 문자열 입력 >>")
    if foo == "종료":
        break
    elif len(foo) ==0:
        print(f"글자수가 {len(foo)}입니다. 다시 입력하시오.")
        continue
    print(f"글자 수는 {len(foo)}")
