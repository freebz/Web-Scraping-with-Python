from selenium import webdriver
service_args = [ '--proxy=localhost:9150', '--proy-type=socks5', ]
driver = webdriver.PhantomJS(executable_path='[path to PhantomJS]',
                             service_args=service_args)

driver.get("http://icanhazip.com")
print(driver.page_source)
driver.close()
