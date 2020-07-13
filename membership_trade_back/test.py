from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome('./chromedriver')


driver.get('https://tmembership.tworld.co.kr:8000/web/html/coupon/CtgViewMainYesMovie.jsp?order=1')
driver.find_elements_by_id('userId')[0].send_keys('jsuwan961205@gmail.com')
driver.find_elements_by_id('password')[0].send_keys('wjdakftndhks1@')
driver.implicitly_wait(2)
driver.find_elements_by_id('authLogin')[0].click()
driver.implicitly_wait(2)
time.sleep(5)

try:
    title = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.slideNavi > li.on > a"))
    )
    print(title.text)
except TimeoutError:
    print("타임아웃")
finally:
    print("끝!")
