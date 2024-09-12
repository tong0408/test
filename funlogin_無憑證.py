import time
from xml.dom.minidom import Element

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#輸入帳號密碼
user='T223075335'
pwd='a123456'

# 會自行下載版本對應的 ChromeDriver，並生成一個 chrome driver object，用作操控 Browser
driver = webdriver.Chrome(service=Service())

# 使 Browser Window 最大化
driver.maximize_window()

# 導向 fun心投
driver.get("https://funwebtest.concords.com.tw/index/1")
time.sleep(3)

#點選文字為登入按鈕
login = driver.find_element(By.PARTIAL_LINK_TEXT, '登入')
login.click()
time.sleep(3)

#找到輸入帳號密碼的地方填入
logintext = driver.find_element(By.CSS_SELECTOR, 'input[placeholder]')
logintext.send_keys(user)

loginpwd = driver.find_element(By.CSS_SELECTOR,"[placeholder='請輸入您的密碼']")
loginpwd.send_keys(pwd)
time.sleep(3)

#按下登入鍵
loginbutton = driver.find_element(By.CSS_SELECTOR, '.m-cnt-main div>div>div>div>div>button')
print(loginbutton)
loginbutton.click()
time.sleep(5)


# 關閉當前操作的 Window
#driver.close()
#time.sleep(3)

# 關閉整個 Browser
# 小提醒: 操作結束後，必須加這個，使之自動關閉 Browser，不然會愈開愈多
#driver.quit()