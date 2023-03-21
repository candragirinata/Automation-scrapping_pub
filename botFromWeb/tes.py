from time import sleep
from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get('https://www.instagram.com/apple/')

# action = ActionChains(driver)
#
# driver.execute_script("window.scrollTo(0, 263)")
#
# a= driver.find_element_by_xpath("//div[@class='u7YqG']")
# # a = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[3]/article/div/div/div[1]/div[1]/a/div[2]")
#
# action.move_to_element(a).perform()
# # driver.find_element_by_css_selector(".Ln-UN").click() ## tidak berfungsi karena tidak menggunakan clickable
#
#
# ui.WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".Ln-UN"))).click()

angkaKiriman = list()
nPosts = driver.find_elements_by_xpath("//span[@class='g47SY ']")

for nPost in nPosts:
    angkaKiriman.append(nPost.text)

# a = append.angkaKiriman[0]
print(angkaKiriman[0])
a = 0
# if (angkaKiriman[0] <> 0):
if (int(angkaKiriman[0]) > 645):
    print("oke")

# while True:
#     print("ok")
#     while True:
#
#
#     if (angkaKiriman[0] == 0):
#      print("lewat")


# print("[for nPost in nPosts]" )

sleep(10)
driver.quit()
