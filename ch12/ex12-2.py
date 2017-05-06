# 12.2.2 쿠키 처리

from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get("http://pythonscraping.com")
driver.implicitly_wait(1)
print(driver.get_cookies())
