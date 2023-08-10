from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time as t
# 뷰티풀수프 임포트
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

service = webdriver.ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service ,options=options)

driver.get('https://www.aladin.co.kr')

t.sleep(2)

# 베스트셀러 탭 클릭
driver.find_element(By.XPATH, '//*[@id="Wa_header1_headerTop"]/div[2]/div[3]/ul[1]/li[3]/a').click()

t.sleep(2)

# selenium으로 현재 페이지의 html 소스 코드를 전부 불러오기
src = driver.page_source
# print(src)

# 뷰티풀수프 객체 생성
# 뷰티풀수프 객체를 생성하면서, 셀레니움이 가지고 온 html 소스코드를
# 제공하고, 해동 소스코드를 html 문법으로 변환하라는 주문.
soup = BeautifulSoup(src, 'html.parser')