from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

def selenium_scroll_option():
    SCROLL_PAUSE_SEC = 3

    # 스크롤 높이 가져옴
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # 끝까지 스크롤 다운
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # 1초 대기
        time.sleep(SCROLL_PAUSE_SEC)

        # 스크롤 다운 후 스크롤 높이 다시 가져옴
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break
        last_height = new_height

chrome_options = webdriver.ChromeOptions()
base_url = "https://www.google.co.kr/imghp?hl=ko"
word = ['cup', 'tumbler', "vacuum"]
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(base_url)
browser = driver.find_element(By.NAME, "q")
browser.send_keys(word)
browser.send_keys(Keys.RETURN)

selenium_scroll_option() # 스크롤하여 이미지를 많이 확보

images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")

count = 1
cnt = 1
for w in word:
    for i in images:
        i.click()
        time.sleep(5)
        if cnt % 25 == 0:
            cnt += 1
        imgurl = driver.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div[' + str(cnt) + ']/a[1]/div[1]/img').get_attribute("src")
        path = "C:\\Users\\ksk03\\PycharmProjects\\Habig_data_collect\\data\\" + w + "\\"
        urllib.request.urlretrieve(imgurl, path + w + str(count) + ".jpg")
        count += 1
        cnt += 1
        if count > 50:
            break