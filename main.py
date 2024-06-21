from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Manage_Exam.login_Page import LoginPage
from Manage_Exam.create_exam import CreateExamPage
from Manage_Exam.update_exam import UpdateExamPage
from Manage_Exam.exam_status import ExamStatusPage
from Manage_Exam.view_exam import ViewExamPage
from Manage_Corporate.Manage_CorporateCourse import CreateCorporateCourse
import configparser
from utils import WebPageUtils



config=configparser.RawConfigParser()
config.read('config.properties')
config.read('my.properties')
def run_test_cases():
    # Set up WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
   # driver.get("http://139.59.64.128:8080/icleaf/#/login")
    #driver.get(config.get('M','base_url'))
    driver.get(config.get('ME', 'base_url'))
    driver.maximize_window()

    # Login
    login_page = LoginPage(driver)  # Instantiate the login page with the driver object
    if not login_page.login():
        print("Login failed, terminating the script.")
        driver.quit()
    # Create Exam
    create_exam_page = CreateExamPage(driver)  # Instantiate the create exam page with the driver object
    try:
        create_exam_page.create_exam()
        create_exam_page.instructions()
    except Exception as e:
        print(f"Error during exam creation: {e}")

    # Update Exam
    update_exam_page = UpdateExamPage(driver)  # Instantiate the update exam page with the driver object
    try:
        update_exam_page.exam_update()
    except Exception as e:
        print(f"Error during exam update: {e}")

    # Exam Status (if applicable)
    exam_status_page = ExamStatusPage(driver)  # Instantiate the exam status page with the driver object
    try:
        exam_status_page.exam_status()
    except Exception as e:
        print(f"Error during exam status check: {e}")

    # View Exam
    view_exam_page = ViewExamPage(driver)  # Instantiate the view exam page with the driver object
    try:
        view_exam_page.exam_view()
    except Exception as e:
        print(f"Error during exam view: {e}")

    # Close the browser after all test cases are executed'''

    # Corpoarte course
    create_corpoarte= CreateCorporateCourse(driver)
    try:
        create_corpoarte.create_corporate_course()
        create_corpoarte.edit_corp_course()

    except Exception as e:
        print(f"Error during create corp: {e}")



    driver.quit()

if __name__ == "__main__":

    run_test_cases()
