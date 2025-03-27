import subprocess
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

WIFI_NAME = "HANSEO"  # 연결할 Wi-Fi 이름
USER_ID = "jjm1088"
USER_PASSWORD = "sm476970!"


# 1️⃣ Wi-Fi 연결 상태 확인 함수
def is_wifi_connected():
    result = subprocess.run(
        "netsh wlan show interfaces",
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="ignore"  # 인코딩 오류 발생 시 무시
    )
    output = result.stdout or ""  # NoneType 방지
    return "상태                   : 연결됨" in output


# 2️⃣ Wi-Fi 연결 시도 함수
def connect_to_wifi():
    print(f"Wi-Fi '{WIFI_NAME}' 연결 시도 중...")
    subprocess.run(f'netsh wlan connect name="{WIFI_NAME}"', shell=True)
    time.sleep(5)  # Wi-Fi 연결될 시간을 줌
    return is_wifi_connected()


# 3️⃣ 로그인 자동화 함수
def auto_login():
    print("Wi-Fi 로그인 페이지 접속...")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.get("http://220.82.2.250/upload/custom/web/index.html?cmd=login")

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user")))

        user_id = driver.find_element(By.ID, "user")
        user_password = driver.find_element(By.ID, "password")

        user_id.send_keys(USER_ID)
        user_password.send_keys(USER_PASSWORD)

        login_button = driver.find_element(By.NAME, "Login")
        login_button.click()

        print("HANSEO Wi-Fi 로그인 완료!")
    except Exception as e:
        print(f"로그인 중 오류 발생: {e}")
    finally:
        driver.quit()


# ✅ 실행 순서
if not is_wifi_connected():
    if connect_to_wifi():
        print("HANSEO Wi-Fi 연결 성공!")
        auto_login()
    else:
        print("Wi-Fi 연결 실패: 프로그램 종료")
else:
    print("Wi-Fi 이미 연결됨. 로그인 진행")
    auto_login()
