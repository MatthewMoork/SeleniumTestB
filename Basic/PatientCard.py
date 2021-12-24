from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from random import randrange

import Basic.constants as const
from Basic.WaitForText import wait_for_text_to_match as waitText

class PatientCard:
    def __init__(self):
        self.options=webdriver.ChromeOptions()
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver=webdriver.Chrome(service=Service(const.PATH), options=self.options)
        
    def take_first_page(self):
        driver=self.driver
        driver.implicitly_wait(30)
        driver.get(const.BASE_URL)

    def log_into_base(self):
        driver=self.driver
        wait = WebDriverWait(driver, 10)
        input_element_login = "//td[@class='td_edit_control']/input[@class='input-ctrl']"
        input_element_password = "//input[@type='password']"
        button_element = "//td[@class='btnc btnc-caption minwidth']"

        input_login = driver.find_element(By.XPATH, input_element_login)
        input_login.clear()
        input_login.send_keys(const.login) 

        input_password = driver.find_element(By.XPATH, input_element_password)
        input_password.send_keys(const.password)

        login_button = driver.find_element(By.XPATH, "//table[@name='btnLogin']/tbody/tr/td[2]") 
        login_button.click()

        
        # wait.until(EC.presence_of_element_located((By.XPATH, "//tr[@class='bt']"))).click()
        wait.until(EC.invisibility_of_element_located((By.ID, "ProgressMis")))
        wait.until(EC.presence_of_element_located((By.XPATH, button_element))).click()
        # WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//table[@name='Btn']/tbody/tr[@class='bt']"))).click()
        driver.execute_script("openWindow('PatientSearch/patient_search');")
        
        wait.until(EC.invisibility_of_element_located((By.ID, "ProgressMis")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//table[@name='ButNewPatient']"))).click()
        # driver.find_element(By.XPATH, "//table[@name='ButNewPatient']").click()

        wait.until(EC.invisibility_of_element_located((By.ID, "ProgressMis")))
        wait.until(EC.invisibility_of_element_located((By.ID, "ProgressMis")))
        surname = driver.find_element(By.XPATH, "//table[@name='SURNAME']/tbody/tr/td/input")
        surname.send_keys(f"BotSurname{randrange(1000)}")
        firstname = driver.find_element(By.XPATH, "//table[@name='FIRSTNAME']/tbody/tr/td/input")
        firstname.send_keys(f"BotFirstname{randrange(1000)}")
        birthdate = driver.find_element(By.XPATH, "//div[@name='BIRTHDATE']/div/input")
        birthdate.clear()
        birthdate.send_keys("01.01.2000")

    def tear_down(self):
        self.driver.close()
        