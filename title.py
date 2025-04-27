from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service)


driver.get("https://www.google.com")

if driver.title == "Google" :
    print("verified")
else:
    print("Unverified")
driver.quit()