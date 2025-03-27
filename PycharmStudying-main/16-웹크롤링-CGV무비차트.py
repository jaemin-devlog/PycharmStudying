import requests
from bs4 import BeautifulSoup

#서버로부터 HTML 코드 받아오기
code = requests.get("https://m.moviechart.co.kr/")
#print(code.text)

#HTML 코드 예쁘게 정리하기
soup = BeautifulSoup(code.text, features="html.parser")
#print(soup)

#내가 원하는 요소 가져오기
#<p class="main_slide_movie_title">극장판 진격의 거인 완결편 더 라스트 어택</p>
#title = soup.select_one("p[class='main_slide_movie_title']")
#print(title.text)
print("\t*** 영화 예매율 순위 ***")
title = soup.select("p.main_slide_movie_title")
num = 1
for i in title:
    print(f"{num}위 : {i.text}")
    num+=1

#[CSS 선택자]
# 1. 속성명이 class : "."
# 2. 속성명이 id : "#"
# 3. ~의 자손 : "> "
# 4. ~의 후손 :