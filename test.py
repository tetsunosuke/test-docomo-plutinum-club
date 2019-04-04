from selenium import webdriver
import chromedriver_binary
import config
import time

options = webdriver.ChromeOptions()
#options.add_argument('--headless')
driver = webdriver.Chrome(options=options)  # 今は chrome_options= ではなく options=

url = "https://dpoint.jp/auth/cgi/mltdomanidlogin?rl=https%3A%2F%2Fdpoint.jp%2Fctrw%2Fweb%2Fcoupon%2Fplatinum_coup.html"
driver.get(url)
driver.find_element_by_name("authid").send_keys(config.mail)
driver.find_element_by_name("subForm").click()
# 画面遷移
driver.find_element_by_name("authpass").send_keys(config.pwd)
driver.find_element_by_name("subForm").click()

for i in range(4,7):
    driver.get("https://dpoint.jp/ctrw/web/coupon/platinum_coup.html")
    time.sleep(5)
    btns = driver.find_elements_by_link_text("応募する")

    # 最初の応募ボタン = 1
    print(btns)
    btn = btns[i]
    btn.click()
    btns = driver.find_elements_by_tag_name("button")
    btns[0].click()
    time.sleep(1)
    try:
        driver.find_element_by_id("menb").click()
    except:
        driver.find_element_by_id("memb").click()

    driver.find_element_by_id("js-mail-text").send_keys("tetsunosuke.ito@gmail.com")
    driver.find_element_by_id("js-mail-confirm").send_keys("tetsunosuke.ito@gmail.com")
    try:
        driver.find_element_by_id("confirmPcSp_0").click()
    except:
        driver.find_element_by_id("selectParkPCSp_0").click()
        continue

    driver.find_element_by_id("redirectMail_0").click()


