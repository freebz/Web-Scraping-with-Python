# 10.2 Ajax와 동적 HTML

# 10.2.1 셀레니움으로 파이썬에서 자바스크립트 실행

from selenium import webdriver
import time

driver = webdriver.PhantomJS()
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
time.sleep(3)
print(driver.find_element_by_id("content").text)
driver.close()
