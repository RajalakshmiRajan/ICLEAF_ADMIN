from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from utils import WebPageUtils
import time
import configparser
import mysql.connector
from db_utils import query_database


config=configparser.RawConfigParser()
config.read('/home/adminroot/PycharmProjec/pythonProject/Manage_Content/config.properties')

class CreateCorporateCourse:

    def __init__(self, driver):
        self.driver = driver
    def create_corporate_course(self):
        #values_list = []
        try:
            WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,config.get('ME',   'manage_corporate')))).click()
            time.sleep(2)
            utils = WebPageUtils(self.driver)
            utils.url_display()
            Manage_corp_c= WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, config.get('ME','manage_corporate_course'))))
            Manage_corp_c.click()
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ME', 'create_corp_course_button')))).click()

            input_element = WebDriverWait(self.driver, 50).until(
                EC.visibility_of_element_located((By.XPATH, config.get('ME', 'course_type'))))
            input_element.click()
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ME', 'coursetype')))).click()

            input_element = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, config.get('ME', 'subject_type'))))
            input_element.click()

            self.driver.execute_script("arguments[0].scrollIntoView(true);", input_element)
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ME', 'subject_name')))).click()

            time.sleep(1)
            input_element = WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, config.get('ME',   'coursename'))))
            input_element.click()
            input_element.send_keys("Selenium")
            input_element = WebDriverWait(self.driver, 50).until(
                EC.visibility_of_element_located((By.XPATH, config.get('ME', 'coursedesc'))))
            input_element.click()
            time.sleep(1)
            input_element.send_keys("Selenium descrip")
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, config.get('ME', 'courseprice')))).send_keys("500")
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, config.get('ME', 'course_duration')))).send_keys("30")
            input_element = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, config.get('ME', 'script_lan'))))
            input_element.click()
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ME', 'script_subject')))).click()


            utils.scroll(By.XPATH, config.get('ME', 'save_button'))
            checkbox_xpaths = [
                config.get('ME', 'survey'),
                config.get('ME', 'certificate'),
                config.get('ME', 'exam_pack'),
                config.get('ME', 'course_progress'),
                config.get('ME', 'user_progress'),
                config.get('ME', 'course_track'),
                config.get('ME', 'navigate_section')
            ]

            # Loop through each checkbox XPATH
            for checkbox_xpath in checkbox_xpaths:
                checkbox = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, checkbox_xpath)))
                if not checkbox.is_selected():
                    checkbox.click()
                time.sleep(2)
                '''
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, config.get('ME', 'certificate_no')))).send_keys("1")'''
            time.sleep(1)
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, config.get('ME', 'mail_id')))).send_keys("admin@gmain.com")

            self.driver.save_screenshot("/home/adminroot/PycharmProjec/pythonProject/Screenshots/create_CorpCourse1.png")
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ME', 'save_button')))).click()
            time.sleep(1)

            print("Corporate course created successfully")
        except Exception as e:
            print(f"An error occurred: {e}")

    def edit_corp_course(self):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ME', 'manage_corporate')))).click()
            time.sleep(2)
            utils = WebPageUtils(self.driver)
            utils.url_display()
            Manage_corp_c = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, config.get('ME', 'manage_corporate_course'))))
            Manage_corp_c.click()
            time.sleep(3)
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, config.get('ME', 'search_specific_exam')))).send_keys(
                "Test Automation")
            time.sleep(3)

            Manage_corp_c = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, config.get('ME', 'edit_corp'))))
            Manage_corp_c.click()
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, config.get('ME', 'edit')))).click()
            time.sleep(3)

            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, config.get('ME', 'course_duration')))).send_keys("50")
            # Click on the SVG element
            input_element=WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, config.get('ME', 'script_lan'))))
            input_element.click()
            time.sleep(2)
            input_element.send_keys("NA")
            time.sleep(2)
            ActionChains(self.driver).send_keys(Keys.PAGE_DOWN).perform()
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ME', 'button_syn')))).click()
            time.sleep(2)

            # Wait for the specific div to be visible
            parent_div = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, config.get('ME', 'message_f')))
            )

            # Find the span element inside the parent div
            message_element = parent_div.find_element(By.CSS_SELECTOR,config.get('ME', 'message_c'))

            # Extract the text content from the span element
            message_text = message_element.text

            print("Pop-up Message:", message_text)
            okay_button = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.CLASS_NAME, config.get('ME', 'okay_button'))))
            self.driver.save_screenshot("/home/adminroot/PycharmProjec/pythonProject/Screenshots/create_CorpCourse2.png")
            okay_button.click()
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ME', 'save_button')))).click()


            # Wait for the specific div to be visible
            parent_div = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH,config.get('ME', 'message2_f'))))

            # Find the span element inside the parent div
            message_element = parent_div.find_element(By.XPATH,config.get('ME', 'message2_c'))

            # Extract the text content from the span element
            message_text = message_element.text

            print("Pop-up Message:", message_text)

            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, config.get('ME', 'okay1')))).click()



        except Exception as e:
            print(f"An error occurred: {e}")






