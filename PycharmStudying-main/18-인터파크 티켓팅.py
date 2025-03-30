import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import easyocr
import pickle

# 브라우저 설정
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# WebDriver 실행
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)

# 로그인 페이지로 이동
driver.get('https://tickets.interpark.com/')


def save_cookies():
    # 로그인 후 쿠키 저장
    time.sleep(5)  # 로그인 후 쿠키를 저장할 수 있도록 잠시 대기
    cookies = driver.get_cookies()  # 현재 세션의 쿠키를 가져오기

    # 쿠키 파일로 저장
    with open("cookies.pkl", "wb") as cookie_file:
        pickle.dump(cookies, cookie_file)

    print("쿠키가 저장되었습니다.")


def load_cookies():
    # 쿠키 파일 불러오기
    try:
        with open("cookies.pkl", "rb") as cookie_file:
            cookies = pickle.load(cookie_file)

        # 불러온 쿠키를 웹사이트에 추가
        for cookie in cookies:
            driver.add_cookie(cookie)

        print("쿠키가 불러와졌습니다.")
        driver.refresh()  # 페이지 새로 고침하여 로그인 상태 유지 확인
    except FileNotFoundError:
        print("쿠키 파일이 없습니다. 로그인 후 쿠키를 저장하세요.")


def login():
    print("[로그인 시작]")

    # 로그인 링크 클릭
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, '로그인'))).click()

    # 로그인 창 iframe으로 전환
    frame = wait.until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='leftLoginBox']/iframe[@title='login']"))
    )
    driver.switch_to.frame(frame)

    # 아이디, 비밀번호 입력
    userId = wait.until(EC.presence_of_element_located((By.NAME, 'username')))
    userId.send_keys('jjm1088')  # 아이디 입력

    userPwd = driver.find_element(By.NAME, 'password')
    userPwd.send_keys('sm476970')  # 비밀번호 입력
    userPwd.send_keys(Keys.ENTER)  # 로그인 시도

    print("[로그인 완료]")

    save_cookies()  # 로그인 후 쿠키 저장


# 쿠키가 있으면 불러오고, 없으면 로그인 진행
load_cookies()

# 만약 쿠키가 없으면 로그인 과정을 진행하도록 선택
if not driver.get_cookies():
    login()

# 로그인 후 이동할 페이지
driver.get('https://tickets.interpark.com/')

# 페이지 확인
print("페이지가 열렸습니다.")


# 티켓 검색
def search_ticket():
    print("[티켓 검색 시작]")

    search = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="__next"]/div/header/div/div[1]/div/div[1]/div[3]/div/input')))
    search.send_keys('싸이 올나잇')
    search.send_keys(Keys.ENTER)

    wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/main/div/div/div[1]/div[2]/a[1]/div[1]'))).click()
    print("[티켓 검색 완료]")


# 예매 페이지 이동
def go_to_booking():
    print("[예매 페이지 이동]")
    driver.switch_to.window(driver.window_handles[-1])
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="productSide"]/div/div[2]/a[1]'))).click()

    driver.switch_to.window(driver.window_handles[-1])
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//*[@id='ifrmSeat']")))
    print("[예매 페이지 도착]")


# 좌석 선택
def select_seat():
    print("[좌석 선택 시작]")
    driver.switch_to.default_content()
    driver.switch_to.frame(wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="ifrmSeat"]'))))

    while True:
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="GradeDetail"]/div/ul/li[1]/a'))).click()
            driver.switch_to.frame(wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="ifrmSeatDetail"]'))))

            seat = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Seats"]')))
            seat.click()
            print("[좌석 선택 완료]")
            payment()
            break
        except:
            print("[좌석 선택 실패, 다시 시도 중...]")
            driver.switch_to.default_content()
            driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="ifrmSeat"]'))
            wait.until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/form[1]/div/div[1]/div[3]/div/p/a/img'))).click()
            time.sleep(1)


# 결제 진행
def payment():
    print("[결제 진행]")
    driver.switch_to.default_content()
    driver.switch_to.frame(wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="ifrmSeat"]'))))
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="NextStepImage"]'))).click()

    driver.switch_to.default_content()
    driver.switch_to.frame(wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='ifrmBookStep']"))))

    select = Select(wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="PriceRow001"]/td[3]/select'))))
    select.select_by_index(1)
    driver.switch_to.default_content()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="SmallNextBtnImage"]'))).click()

    # 주문자 확인
    driver.switch_to.frame(wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='ifrmBookStep']"))))
    driver.find_element(By.XPATH, '//*[@id="YYMMDD"]').send_keys('생년월일')
    driver.switch_to.default_content()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="SmallNextBtnImage"]'))).click()

    # 결제 방식 선택
    driver.switch_to.frame(wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="ifrmBookStep"]'))))
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Payment_22004"]/td/input'))).click()

    select2 = Select(wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="BankCode"]'))))
    select2.select_by_index(1)
    driver.switch_to.default_content()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="SmallNextBtnImage"]'))).click()

    driver.switch_to.frame(wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="ifrmBookStep"]'))))
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkAll"]'))).click()
    driver.switch_to.default_content()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="LargeNextBtnImage"]'))).click()

    print("[결제 완료]")


# CAPTCHA 자동 입력
def solve_captcha():
    print("[CAPTCHA 해결 시작]")
    reader = easyocr.Reader(['en'])

    while True:
        try:
            capchaPng = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="imgCaptcha"]')))
            result = reader.readtext(capchaPng.screenshot_as_png, detail=0)
            capchaValue = result[0].replace(' ', '').replace('5', 'S').replace('0', 'O').replace('$', 'S')

            # CAPTCHA 입력
            driver.find_element(By.XPATH, '//*[@id="divRecaptcha"]/div[1]/div[3]').click()
            chapchaText = driver.find_element(By.XPATH, '//*[@id="txtCaptcha"]')
            chapchaText.send_keys(capchaValue)

            # 확인 버튼 클릭
            driver.find_element(By.XPATH, '//*[@id="divRecaptcha"]/div[1]/div[4]/a[2]').click()

            # CAPTCHA 해결 여부 확인
            if not wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="divRecaptcha"]'))).is_displayed():
                print("[CAPTCHA 해결 완료]")
                select_seat()
                break
            else:
                driver.find_element(By.XPATH, '//*[@id="divRecaptcha"]/div[1]/div[1]/a[1]').click()
        except:
            print("[CAPTCHA 해결 실패, 다시 시도 중...]")
