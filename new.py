import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import win32com.client as win32
import logging
from datetime import datetime
import datetime
                        
executable_path = 'C:/NotBackedUp/ChromeDriver/chromedriver.exe'
capabilities = { 'chromeOptions':  { 'useAutomationExtension': False}}
driver = webdriver.Chrome(executable_path,desired_capabilities = capabilities)


driver.get("https:\\Google.com")
time.sleep(20)

driver.get("https://www.udemy.com/java-tutorial/learn/v4/t/lecture/131596?start=0")
time.sleep(20)
