import random
import time

from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObject.test_home_page import TestHomePage


class achievehomepage(TestHomePage):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    achieve_module = (By.XPATH, "//span[text()= 'Achieve']")
    start_achieving_btn = (By.XPATH, "//span[text()= 'Start Achieving Now']")
    start_achieve_journey_btn = (By.XPATH, "//span[text()= ' Start your ']")
    total_sub_count = (By.XPATH, '//div[@class="eds-col-xs-12 eds-col-sm-3 eds-col-md-3 eds-col-lg-3"]/div')
    continue_btn = (By.XPATH, "//span[text()='Continue']")
    step1_total_sub_count = (
        By.XPATH, "//div[@class='chapter-selection-wrapper--subjects eds-col-md-3 eds-col-lg-3']/div")
    total_chapt_count = (By.XPATH, "//div[@class='chapter-selection-wrapper--chapters']/div[2]/div/div")
    create_journey_btn = (By.XPATH, "//div[@class='create-achieve-journey-wrapper']/div/span")
    dt1_start_test_btn = (By.XPATH, "//button[@class='eds-btn eds-btn--tertiary eds-btn--capsular eds-btn--md test-button']")
    dt1_resume_test_btn = (By.XPATH, "//span[text()='Resume']")
    dt2_start_test_btn = (By.XPATH, "//span[text()='Achieve Diagnostic Test 2']/parent::div/following-sibling::div[2]/button")
    instruction_checkbox = (By.XPATH, "//span[text()= 'I have read and understood the instructions.']")
    test_start_button = (By.XPATH, "//span[text()= 'Start Now']")
    i_will_take_test_later = (By.XPATH, "//span[text()='I will take the test later']")
    PAJ_name_field = (By.CSS_SELECTOR, "[placeholder='My Achieve Journey']")
    target_date = (By.CSS_SELECTOR, "[placeholder='dd-mm-yyyy']")
    generate_PAJ_button = (By.XPATH, "//span[contains(text(),'Start your Achievement Journey')]")
    view_fb_start_journey_btn = (By.XPATH, "//span[contains(text(),'View Feedback and Start Journey')]")
    explore_mastery = (By.XPATH, "//span[text()='Explore Mastery']")
    explore_mastery_1st_chapter = (By.XPATH, "//div[@class='achieve_homepage-content-wrapper']/div/div[2]/div[1]")
    explore_mastery_1st_topic = (By.XPATH, "//div[@class='achieve_homepage-content-wrapper']/div/div[2]/div[1]/div[2]/div[1]")
    explore_mastery_1st_video = (By.XPATH, "//*[@id='app']/main/div[2]/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div[1]/div/div/div/div[3]")
    time_spend_everyday = (By.CSS_SELECTOR, "i[color='white']")
    calendar_next_btn = (By.CSS_SELECTOR, "[aria-label='Next Month']")




    def wait_for_visibility(self, locator):
        """Wait until an element is visible and return it."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator):
        """Wait until an element is clickable and return it."""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def create_diagnostic_test(self):
        self.wait_for_clickable(achievehomepage.achieve_module).click()
        try:
            self.wait_for_clickable(achievehomepage.start_achieving_btn).click()
            self.wait_for_clickable(achievehomepage.start_achieve_journey_btn).click()
        except:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            self.wait_for_clickable(achievehomepage.create_journey_btn).click()
        time.sleep(5)
        sub_count = self.driver.find_elements(*achievehomepage.total_sub_count)
        for i in range(1, len(sub_count)):
            self.driver.find_element(By.XPATH,
                                     '//div[@class="eds-col-xs-12 eds-col-sm-3 eds-col-md-3 eds-col-lg-3"]/div[' + str(
                                         i) + ']').click()
        self.wait_for_clickable(achievehomepage.continue_btn).click()

        time.sleep(5)

        for k in range(1, len(sub_count)):
            self.driver.find_element(By.XPATH,
                                     "//div[@class='chapter-selection-wrapper--subjects eds-col-md-3 eds-col-lg-3']/div[" + str(
                                         k) + "]").click()
            chapters = self.driver.find_elements(*achievehomepage.total_chapt_count)  # Update 'locator_strategy'
            chapter_count = len(chapters)
            if chapter_count > 0:
                j = random.randint(1, chapter_count)
                self.driver.find_element(By.XPATH,
                                         "//div[@class='chapter-selection-wrapper--chapters']/div[2]/div/div[" + str(
                                             j) + "]").click()
                time.sleep(5)
            self.wait_for_clickable(achievehomepage.continue_btn).click()

        self.wait_for_visibility(achievehomepage.dt1_start_test_btn)

    def start_diagnostic_test1(self):
        self.wait_for_clickable(achievehomepage.achieve_module).click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.wait_for_clickable(achievehomepage.dt1_resume_test_btn).click()


        if self.driver.find_element(By.XPATH, "//button[@class='eds-btn eds-btn--tertiary eds-btn--capsular eds-btn--md test-button']/span/span").text == "Start Test":
                self.wait_for_clickable(achievehomepage.dt1_start_test_btn).click()
                self.wait_for_clickable(achievehomepage.instruction_checkbox).click()
                self.wait_for_clickable(achievehomepage.test_start_button).click()
        elif self.driver.find_element(By.XPATH,
                                     "//button[@class='eds-btn eds-btn--tertiary eds-btn--capsular eds-btn--md test-button']/span/span").text == "Resume":
                self.wait_for_clickable(achievehomepage.dt1_resume_test_btn).click()
                time.sleep(5)
        self.attempt_dt_test()

    def i_will_start_test_later(self):
        self.wait_for_clickable(achievehomepage.achieve_module).click()
        try:
            self.wait_for_clickable(achievehomepage.start_achieving_btn).click()
            self.wait_for_clickable(achievehomepage.start_achieve_journey_btn).click()
        except:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            self.wait_for_clickable(achievehomepage.create_journey_btn).click()
        time.sleep(5)
        sub_count = self.driver.find_elements(*achievehomepage.total_sub_count)
        for i in range(1, len(sub_count)):
            self.driver.find_element(By.XPATH,
                                     '//div[@class="eds-col-xs-12 eds-col-sm-3 eds-col-md-3 eds-col-lg-3"]/div[' + str(
                                         i) + ']').click()
        self.wait_for_clickable(achievehomepage.continue_btn).click()

        time.sleep(5)

        for k in range(1, len(sub_count)):
            self.driver.find_element(By.XPATH,
                                     "//div[@class='chapter-selection-wrapper--subjects eds-col-md-3 eds-col-lg-3']/div[" + str(
                                         k) + "]").click()
            chapters = self.driver.find_elements(*achievehomepage.total_chapt_count)  # Update 'locator_strategy'
            chapter_count = len(chapters)
            if chapter_count > 0:
                j = random.randint(1, chapter_count)
                print(f"Random Chapter Number: {j}")
                self.driver.find_element(By.XPATH,
                                         "//div[@class='chapter-selection-wrapper--chapters']/div[2]/div/div[" + str(
                                             j) + "]").click()
                time.sleep(5)
            self.wait_for_clickable(achievehomepage.continue_btn).click()
        self.wait_for_clickable(achievehomepage.i_will_take_test_later).click()
        assert self.driver.find_element(By.XPATH, "//span[text()='Explore Mastery']").text == "Explore Mastery"

    def start_diagnostic_test2(self):
        self.wait_for_clickable(achievehomepage.achieve_module).click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.wait_for_clickable(achievehomepage.dt1_resume_test_btn).click()
        try:
            if self.driver.find_element(By.XPATH,
                                    "//span[text()='Achieve Diagnostic Test 2']/parent::div/following-sibling::div[2]/button").text == "Start Test":
                self.wait_for_clickable(achievehomepage.dt2_start_test_btn).click()
                self.wait_for_clickable(achievehomepage.instruction_checkbox).click()
                self.wait_for_clickable(achievehomepage.test_start_button).click()
            elif self.driver.find_element(By.XPATH,
                                      "//span[text()='Achieve Diagnostic Test 2']/parent::div/following-sibling::div[2]/button").text == "Resume":
                self.wait_for_clickable(achievehomepage.dt2_start_test_btn).click()
                time.sleep(5)
            self.attempt_dt_test()

        except Exception as e:
            print(f"An error occurred: {e}")
            if self.wait_for_clickable(achievehomepage.dt1_start_test_btn):
                self.wait_for_clickable(achievehomepage.dt1_start_test_btn).click()
                # assert "Step 2 of 3" == self.driver.find_element(By.XPATH, "//span[contains(text(),'Step 2')]").text
            else:
                self.wait_for_clickable(achievehomepage.dt2_start_test_btn).click()

    def create_PAJ_journey(self):
        self.wait_for_clickable(achievehomepage.achieve_module).click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.wait_for_clickable(achievehomepage.dt1_resume_test_btn).click()
        self.wait_for_clickable(achievehomepage.dt2_start_test_btn).click()
        self.driver.find_element(By.XPATH,
    "//img[contains(@src,'images/overall-accuracy.svg')]/parent::div/following-sibling::div/div[4]").click()
        self.wait_for_clickable(achievehomepage.PAJ_name_field).click()
        self.wait_for_clickable(achievehomepage.PAJ_name_field).send_keys("PAJ Journey")

        for i in range(7):
            self.wait_for_clickable(achievehomepage.time_spend_everyday).click()
        self.wait_for_clickable(achievehomepage.target_date).click()
        self.wait_for_clickable(achievehomepage.calendar_next_btn).click()
        self.driver.find_element(By.XPATH, "//div[@class='DayPicker-Months']/div/div[3]/div[2]/div[3]").click()
        self.wait_for_clickable(achievehomepage.generate_PAJ_button).click()
        time.sleep(5)
        self.wait_for_clickable(achievehomepage.view_fb_start_journey_btn).click()
        assert "Here is your Achievement Journey" == self.driver.find_element(By.XPATH, "//span[contains(text(),'Here is your Achievement Journey')]").text

    def explore_mastery_tile(self):
        self.wait_for_clickable(achievehomepage.achieve_module).click()
        self.wait_for_clickable(achievehomepage.explore_mastery).click()
        time.sleep(5)

        self.wait_for_clickable(achievehomepage.explore_mastery_1st_chapter).click()
        time.sleep(5)
        self.wait_for_clickable(achievehomepage.explore_mastery_1st_topic).click()
        time.sleep(5)
        self.driver.execute_script("window.scrollBy(0, 250);")
        self.wait_for_clickable(achievehomepage.explore_mastery_1st_video).click()
        time.sleep(5)

    def extend_PAJ_journey(self):
       pass







    def attempt_dt_test(self):
        ele = self.driver.find_elements(By.XPATH, "//div[@class='test-wrapper ']/div/div[2]/div[1]/button")
        for k in range(1, len(ele) + 1):
            self.driver.find_element(By.XPATH, "//div[@class='test-wrapper ']/div/div[2]/div[1]/button[" + str(
                k) + "]").click()
            questions = self.driver.find_elements(*TestHomePage.question_count)
            for i in range(1, len(questions)):
                time.sleep(3)
                question = self.driver.find_element(*TestHomePage.question_type).text

                if question in ['Single Choice', 'Multiple Choice', 'True-False']:
                    try:
                        # Scroll to the element before clicking
                        element_to_click = self.driver.find_element(*TestHomePage.option_A_click)
                        self.driver.execute_script("arguments[0].scrollIntoView(true);", element_to_click)
                        element_to_click.click()

                        # Scroll to and click the save next button
                        save_next_btn = self.driver.find_element(*TestHomePage.save_next_btn)
                        self.driver.execute_script("arguments[0].scrollIntoView(true);", save_next_btn)
                        save_next_btn.click()
                    except ElementClickInterceptedException:
                        save_next_btn = self.driver.find_element(*TestHomePage.save_next_btn)
                        self.driver.execute_script("arguments[0].scrollIntoView(true);", save_next_btn)
                        save_next_btn.click()


                elif question == 'Subjective Answer':
                    try:

                        self.driver.find_element(*TestHomePage.sub_input_field).click()
                        self.driver.find_element(*TestHomePage.sub_input_field).send_keys("XYZ")
                        self.driver.find_element(*TestHomePage.save_next_btn).click()
                    except NoSuchElementException:
                        self.driver.find_element(*TestHomePage.save_next_btn).click()

                elif question == 'Subjective Numerical':
                    try:

                        self.driver.find_element(*TestHomePage.sub_input_field).click()
                        self.driver.find_element(*TestHomePage.sub_input_field).send_keys("123")
                        self.driver.find_element(*TestHomePage.save_next_btn).click()
                    except NoSuchElementException:
                        self.driver.find_element(*TestHomePage.save_next_btn).click()

                elif question == 'Fill in The Blanks':
                    try:

                        self.driver.find_element(*TestHomePage.fib_1_field).click()
                        self.driver.find_element(*TestHomePage.fib_1_field).send_keys("XYZ")
                        self.driver.find_element(*TestHomePage.save_next_btn).click()
                    except NoSuchElementException:
                        self.driver.find_element(*TestHomePage.save_next_btn).click()

                elif question == 'Matrix':
                    try:

                        self.driver.find_element(*TestHomePage.save_next_btn).click()
                    except NoSuchElementException:
                        self.driver.find_element(*TestHomePage.save_next_btn).click()

                elif question == 'Multiple Fill in The Blanks':
                    try:

                        self.driver.find_element(*TestHomePage.fib_1_field).click()
                        self.driver.find_element(*TestHomePage.fib_2_field).click()
                        self.driver.find_element(*TestHomePage.save_next_btn).click()
                    except NoSuchElementException:
                        self.driver.find_element(*TestHomePage.save_next_btn).click()

                else:
                    self.driver.find_element(*TestHomePage.save_next_btn).click()

        self.driver.find_element(*TestHomePage.submit_btn).click()
        time.sleep(5)
        self.driver.find_element(*TestHomePage.submit_confirm_btn).click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, "//*[contains(text(),'Continue')]").click()
        time.sleep(10)
        # assert "Achieve Diagnostic Test 2" == self.driver.find_element("//*[contains(text(),'Achieve Diagnostic Test 2')]").text
