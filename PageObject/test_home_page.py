import time

from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from PageObject.practice_home_page import PracticeHomePage


class TestHomePage:

    def __init__(self, driver):
        self.driver = driver

    test_module = (By.XPATH, "//*[text()='Test']")
    trending_test_tile = (
    By.XPATH, "//*[contains(text(),'Trending Tests for Your Exam')]/parent::div/div[2]/div[2]/div/div[1]/div/div/div")
    take_full_test = (
    By.XPATH, "//*[contains(text(),'Take Full Tests')]/parent::div/div[2]/div[2]/div/div[1]/div/div/div")
    take_chapter_test = (
    By.XPATH, "//*[contains(text(),'Take Chapter Tests')]/parent::div/div[2]/div[2]/div/div[1]/div/div/div")
    test_btn_status = (By.XPATH, "//*[starts-with(@class,'eds-btn eds-btn--primary eds-btn--capsular eds-btn--md')]")
    start_test = (By.XPATH, "//*[text()='Start Test']")
    resume_test = (By.XPATH, "//*[text()='Resume Test']")
    learn_chapter = (By.XPATH, "//*[contains(text(), 'Chapters From')]/parent::div/div[2]/div/div/div[1]/div/div/div")
    instruct_chkbox = (By.XPATH, "//*[contains(text(), 'I have ')]")
    start_now = (By.XPATH, "//*[text()='Start Now']")
    learn_chapter_test_tile = (
    By.XPATH, "//*[@class='learn-summary-wrapper__section-data-wrapper']/div/div[2]/div[2]/div[1]/div[1]")
    option_A_click = (By.XPATH, "//div[@id='app']/main/div/div/div[4]/div/div[1]/div/div/div/div[2]/div[1]")
    question_type = (By.XPATH, "//body/div[@id='app']/main[1]/div[1]/div[1]/div[3]/div[1]/span[2]")
    save_next_btn = (By.XPATH, "//span[contains(text(),'Save & Next')]")
    submit_btn = (By.XPATH, "//*[contains(text(),'Submit Test')]")
    test_on_this_chapter = (By.XPATH, "//span[text()='Tests on this Chapter']")
    submit_confirm_btn = (
    By.XPATH, "//*[text()= 'Continue Test']/parent::span/parent::button/parent::div/button[1]/span")
    view_fb_btn = (By.XPATH, "//span[contains(text(),'View Test Feedback')]/parent::span/parent::button")
    question_count = (By.XPATH, "//div[@id='app']/main/div/div/div[4]/div[2]/div/div")
    sub_input_field = (By.XPATH, "//*[@id='app']/main/div[1]/div/div[4]/div[1]/div[1]/div/div/div/input")
    fib_1_field = (By.XPATH,
                   "//body/div[@id='app']/main[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/input[1]")
    fib_2_field = (By.XPATH,
                   "//body/div[@id='app']/main[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[2]/input[1]")
    test_env_popup = (By.XPATH, "//*[contains(text(),'You are about to enter the')]")
    sel_embibe_expUI = (By.XPATH, "//*[text()= 'Show me the EMBIBE Experience']")
    subject_buttons = (By.XPATH, "//*[@id='app']/main[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div")
    test_banner_btn = (By.CSS_SELECTOR, "[data-tour='learn-button']")
    recommended_learning = (By.XPATH, "//*[contains(text(),'Recommended Learning to ace this Test')]")
    recommended_practice = (By.XPATH, "//*[contains(text(),'Recommended Practice to ace this Test')]")
    recommend_video_click = (By.XPATH, "//div[@class='section-division']/div[2]/div/div[1]")
    recommend_practice_click = (By.XPATH, "//div[@class='section-division']/div[1]/div[5]")
    more_test = (By.XPATH, "//*[contains(text(),'More Tests on this Syllabus')]")
    cyot_tile = (By.XPATH, "//div[text()='My Custom Tests']/parent::div[1]/div/div/div[1]/div[1]/div/div/div")
    step1_select_Chapters = (
    By.XPATH, "//div[contains(@class, 'test-subjects-wrapper--subject-selection')]/div/div/div[3]/div/div")
    step2_Select_chapters = (By.XPATH, "//div[contains(@class,'test-chapters-wrapper--subjects hide')]/div")
    select_all_chapter = (By.XPATH, "//span[text()= 'All Chapters']")
    quick_5_mins_test_btn = (By.XPATH, "//span[text()='Quick 5 Minute Test']")
    custom_test_btn = (By.XPATH, "//*[text()='Custom Test']")
    your_test_name_field = (By.CSS_SELECTOR, "[placeholder='Enter Your Test Name']")
    plan_target_button = (By.XPATH, "//span[text()='Plan your targets']")

    def trending_test_embibe_exp_ui(self):
        try:
            self.driver.find_element(*TestHomePage.test_module).click()
            self.driver.find_element(*TestHomePage.trending_test_tile).click()
            time.sleep(3)
            self.test_taking()
        except NoSuchElementException as e:
            print(e.msg)

    def full_test_embibe_exp_ui(self):
        self.driver.find_element(*TestHomePage.test_module).click()
        self.driver.find_element(*TestHomePage.take_full_test).click()
        time.sleep(3)
        self.test_taking()

    def chapter_test_embibe_exp_ui(self):
        self.driver.find_element(*TestHomePage.test_module).click()
        self.driver.find_element(*TestHomePage.take_chapter_test).click()
        time.sleep(3)
        self.test_taking()

    def recommended_practice_in_trending_test_summary(self):
        self.driver.find_element(*TestHomePage.test_module).click()
        self.driver.find_element(*TestHomePage.take_chapter_test).click()
        time.sleep(3)
        self.driver.find_element(*TestHomePage.recommended_practice).click()
        time.sleep(3)
        self.driver.find_element(*TestHomePage.recommend_practice_click).click()

    def recommended_learn_video_in_trending_test_summary(self):
        self.driver.find_element(*TestHomePage.test_module).click()
        self.driver.find_element(*TestHomePage.take_chapter_test).click()
        time.sleep(3)
        self.driver.find_element(*TestHomePage.recommended_learning).click()
        self.driver.find_element(*TestHomePage.recommend_video_click).click()
        self.recommendlearningvideos()
        time.sleep(5)

    def recommended_practice_in_chapter_test_summary(self):
        self.driver.find_element(*TestHomePage.test_module).click()
        self.driver.find_element(*TestHomePage.take_chapter_test).click()
        self.driver.find_element(*TestHomePage.recommended_practice).click()
        time.sleep(3)
        self.driver.find_element(*TestHomePage.recommend_practice_click).click()
        pt = PracticeHomePage(self.driver)
        pt.practice_taking()

    def recommended_learn_in_chapter_test_summary(self):
        self.driver.find_element(*TestHomePage.test_module).click()
        self.driver.find_element(*TestHomePage.take_chapter_test).click()

        self.driver.find_element(*TestHomePage.recommended_learning).click()
        self.driver.find_element(*TestHomePage.recommend_video_click).click()
        self.recommendlearningvideos()
        # self.driver.find_element(*TestHomePage.more_test).click()
        # self.driver.find_element(*TestHomePage.carousel_click).click()

    def recommended_practice_in_full_test_summary(self):
        self.driver.find_element(*TestHomePage.test_module).click()
        self.driver.find_element(*TestHomePage.take_chapter_test).click()
        time.sleep(3)
        self.driver.find_element(*TestHomePage.recommended_practice).click()
        time.sleep(3)
        self.driver.find_element(*TestHomePage.recommend_practice_click).click()
        pt = PracticeHomePage(self.driver)
        pt.practice_taking()
        # self.driver.find_element(*TestHomePage.more_test).click()
        # self.driver.find_element(*TestHomePage.carousel_click).click()

    def recommended_learn_in_full_test_summary(self):
        self.driver.find_element(*TestHomePage.test_module).click()
        self.driver.find_element(*TestHomePage.take_chapter_test).click()
        time.sleep(3)
        self.driver.find_element(*TestHomePage.recommended_learning).click()
        self.driver.find_element(*TestHomePage.recommend_video_click).click()
        self.recommendlearningvideos()
        # self.driver.find_element(*TestHomePage.more_test).click()
        # self.driver.find_element(*TestHomePage.carousel_click).click()

    def quick_5_mins_cyot(self):
        self.driver.find_element(*TestHomePage.test_module).click()
        self.driver.find_element(*TestHomePage.cyot_tile).click()
        total_subject = self.driver.find_elements(*TestHomePage.step1_select_Chapters)
        for i in range(1, len(total_subject)):
            self.driver.find_element(By.XPATH,
                                     "//div[contains(@class, 'test-subjects-wrapper--subject-selection')]/div/div/div[3]/div/div[" + str(
                                         i) + "]").click()
            time.sleep(0.5)

        self.driver.find_element(By.XPATH, "//span[text()='Next']").click()

        chapter_count = self.driver.find_elements(*TestHomePage.step2_Select_chapters)
        for i in range(1, len(chapter_count) + 1):
            self.driver.find_element(By.XPATH,
                                     "//div[contains(@class,'test-chapters-wrapper--subjects hide')]/div[" + str(
                                         i) + "]").click()
            self.driver.find_element(*TestHomePage.select_all_chapter).click()

        self.driver.find_element(*TestHomePage.quick_5_mins_test_btn).click()
        time.sleep(10)
        self.test_taking()

    def cyot(self):

        self.driver.find_element(*TestHomePage.test_module).click()
        self.driver.find_element(*TestHomePage.cyot_tile).click()
        total_subject = self.driver.find_elements(*TestHomePage.step1_select_Chapters)
        for i in range(1, len(total_subject)):
            self.driver.find_element(By.XPATH,
                                     "//div[contains(@class, 'test-subjects-wrapper--subject-selection')]/div/div/div[3]/div/div[" + str(
                                         i) + "]").click()
            time.sleep(0.5)

        self.driver.find_element(By.XPATH, "//span[text()='Next']").click()

        chapter_count = self.driver.find_elements(*TestHomePage.step2_Select_chapters)
        for i in range(1, len(chapter_count) + 1):
            self.driver.find_element(By.XPATH,
                                     "//div[contains(@class,'test-chapters-wrapper--subjects hide')]/div[" + str(
                                         i) + "]").click()
            self.driver.find_element(*TestHomePage.select_all_chapter).click()
        self.driver.find_element(*TestHomePage.custom_test_btn).click()
        self.driver.find_element(*TestHomePage.your_test_name_field).click()
        self.driver.find_element(*TestHomePage.your_test_name_field).send_keys("Sample Test")
        self.driver.find_element(By.XPATH, "//span[text()='Next']").click()
        time.sleep(10)
        self.test_taking()

    def test_home_sub_banner(self):
        self.driver.find_element(*TestHomePage.test_module).click()
        total_subject = self.driver.find_elements(*TestHomePage.subject_buttons)
        count = len(total_subject)
        for i in range(1, count):
            self.driver.find_element(By.CSS_SELECTOR, "[id='sub0" + str(i) + "']").click()
            self.test_taking()
            self.driver.find_element(*TestHomePage.test_module).click()

    def recommendlearningvideos(self):
        try:
            popup = self.driver.find_element(By.XPATH, "//*[text()='Continue from where you left?']")
            if popup.is_displayed():
                time.sleep(2)
                self.driver.find_element(By.XPATH, "//*[text()='Yes']").click()
                time.sleep(5)
                # self.driver.find_element(*LearnHomePage.learn_button).send_keys(keys.Keys.ESCAPE)
                # self.driver.find_element(*LearnHomePage.learn_button).send_keys(keys.Keys.ESCAPE)
                self.driver.back()
                self.driver.back()
                time.sleep(5)

        except NoSuchElementException:
            time.sleep(5)
            self.driver.back()
            self.driver.back()
            time.sleep(5)

        except ElementClickInterceptedException:
            time.sleep(5)
            # Refresh the page if ElementClickInterceptedException occurs
            self.driver.refresh()

    def test_taking_in_learn_chapters(self):
        self.driver.find_element(*TestHomePage.learn_chapter).click()
        time.sleep(2)
        self.driver.find_element(*TestHomePage.test_on_this_chapter).click()
        time.sleep(2)
        self.driver.find_element(*TestHomePage.learn_chapter_test_tile).click()
        try:
            if self.driver.find_element(By.XPATH, "//*[@class='instruction-header']/span").is_displayed():
                self.driver.find_element(*TestHomePage.instruct_chkbox).click()
                self.driver.find_element(*TestHomePage.start_now).click()
                questions = self.driver.find_elements(*TestHomePage.question_count)
                for i in range(1, len(questions)+1):
                    time.sleep(3)
                    question = self.driver.find_element(*TestHomePage.question_type).text

                    if question in ['Single Choice', 'Multiple Choice', 'True-False']:
                        try:

                            self.driver.find_element(*TestHomePage.option_A_click).click()
                            self.driver.find_element(*TestHomePage.save_next_btn).click()
                        except NoSuchElementException:
                            self.driver.find_element(*TestHomePage.save_next_btn).click()

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
                self.driver.find_element(*TestHomePage.submit_confirm_btn).click()
                self.driver.find_element(*TestHomePage.view_fb_btn).click()
        except:
            print("Test already Taken")

    def test_taking(self):
        try:
            btn = self.driver.find_element(*TestHomePage.test_btn_status).text

            if btn == 'Expired':
                print("Test has been Expired")

            elif btn == 'Resume Test':
                self.driver.find_element(*TestHomePage.resume_test).click()

            elif btn == 'View Test Feedback':
                print("Test already Taken")

            elif btn =='Start Test':
                self.driver.find_element(*TestHomePage.start_test).click()

            time.sleep(5)
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

                            self.driver.find_element(*TestHomePage.option_A_click).click()
                            self.driver.find_element(*TestHomePage.save_next_btn).click()
                        except NoSuchElementException:
                            self.driver.find_element(*TestHomePage.save_next_btn).click()

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
            if self.driver.find_element(*TestHomePage.view_fb_btn).is_displayed():
                self.driver.find_element(*TestHomePage.view_fb_btn).click()
                time.sleep(10)
                assert "Predicted Improvement" == self.driver.find_element("//*[contains(text(),'Predicted')]").text
            else:
                self.driver.find_element(*TestHomePage.plan_target_button).click()
                assert "Step 2 of 3" == self.driver.find_element("//span[contains(text(),'Step 2')]").text


        except Exception as e:
            print(e)
