# 12.2.3 타이밍이 가장 중요합니다.

# 12.3 널리 쓰이는 폼 보안 기능

# 12.3.1 숨긴 필드 값

# 12.3.2 허니팟 피하기

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.PhantomJS()
driver.get("http://pythonscraping.com/pages/itsatrap.html")
links = driver.find_elements_by_tag_name("a")
for link in links:
    if not link.is_displayed():
        print("The link "+link.get_attribute("href")+" is a trap")

fields = driver.find_elements_by_tag_name("input")
for field in fields:
    if not field.is_displayed():
        print("Do not change value of "+field.get_attribute("name"))


# 12.4 사람처럼 보이기 위한 체크리스트
