from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from Basic.PatientCard import PatientCard

bot = PatientCard()
bot.take_first_page()
bot.log_into_base()
try:
    WebDriverWait(bot.driver, 10000).until(EC.presence_of_element_located((By.ID, 'JustWaiting')))
except:
    bot.driver.quit()
# def log_in(self):
#         input_element_login = "//td[@class='td_edit_control']/input[@class='input-ctrl']"
#         input_element_password = "//input[@type='password']"
#         button_element = "//td[@class='btnc btnc-caption minwidth']"

#         input_login = self.find_element(By.XPATH, input_element_login)
#         self.input_login.clear()
#         self.input_login.send_keys(const.login) 

#         self.input_password = self.find_element(By.XPATH, input_element_password)
#         self.input_password.send_keys(const.password)
        
#         self.login_button = self.find_element(By.XPATH, button_element)
#         self.login_button.click()
#         WebDriverWait(self, 2).until(EC.presence_of_element_located((By.XPATH, button_element)))
#         self.enter_button = self.find_element(By.XPATH, button_element)
#         self.enter_button.click()
