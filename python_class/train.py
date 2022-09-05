
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.programmercarl.com/')

#driver.find_element(By.LINK_TEXT,'贴吧').click()
#driver.find_element(By.XPATH, '//input[@id="kw"]').send_keys('蔡徐坤')

# driver.find_element(By.LINK_TEXT,'地图').click()
driver.find_element(By.XPATH,'//span[text()="求职"]').click()
driver.find_element(By.XPATH,'//a[contains(text(),"专业技能")]').click()
driver.find_element(By.XPATH,'//a[text()="知识星球"]').click()
#page_size = driver.find_element(By.XPATH,'//div[@class="showbody"]//h1').size
#print(page_text)
#print(page_size)
# driver.get('https://www.huya.com/')
# time.sleep(2)
# driver.back()
# time.sleep(2)
# driver.forward()
# time.sleep(2)
driver.maximize_window()
# driver.quit()