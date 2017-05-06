# 13.3 셀레니움을 사용한 테스트

from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get("http://en.wikipedia.org/wiki/Monty_Python")
assert "Monty Python" in driver.title
driver.close()
