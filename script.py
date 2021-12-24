# import os
# from selenium import webdriver
# # from selenium.webdriver.firefox import service
# # from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By

# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options

# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# # os.environ['PATH'] += r"C:\SeleniumDrivers\geekodriver.exe"
# s = Service(r"C:\SeleniumDrivers\chromedriver.exe")
# driver = webdriver.Chrome(service=s, options=options)

# driver.get("http://192.168.228.41/med2des/")
# input_login = driver.find_element(By.XPATH, "//td[@class='td_edit_control']/input[@class='input-ctrl']")
# input_login.clear()
# input_login.send_keys('dev') 

# input_password = driver.find_element(By.XPATH, "//input[@type='password']")
# input_password.send_keys('def') 
# login_button = driver.find_element(By.XPATH, "//td[@class='btnc btnc-caption minwidth']")
# login_button.click()
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//td[@class='btnc btnc-caption minwidth']"))).click()
# driver.execute_script("openWindow('PatientSearch/patient_search');")
# # WebDriverWait(driver, 1).until(EC.text_to_be_present_in_element((By.XPATH, "//td[@class='btnc btnc-caption minwidth']")))


# try:
#     WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.ID, 'IdOfMyElementWait')))
# except:
#     driver.quit()
# from random import radnrange

# print(f"BotLastName{randrange(10000)}")

"Tasks for university"

#1
# def fibbonacci():
#     a,b = 1, 1
#     while True:
#         yield a
#         a, b = b, a+b

# c = fibbonacci()
# k = int(input('Введите диапазон: '))
# for i in range(k):
#     print(next(c))

#2
def fibbonacci():
    a,b = 1, 1
    while True:
        yield a
        a, b = b, a+b

c = fibbonacci()
k = int(input('Введите диапазон: '))
for i in range(k-1):
    print(next(c))

#3