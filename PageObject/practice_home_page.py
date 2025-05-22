import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By




class PracticeHomePage:

    def __init__(self, driver):
        self.driver = driver

    Practice_Module = (By.XPATH, "//*[text()='Practice']")
    Practice_banner_button = (By.XPATH, "//*[text()='Practice from Book']")
    Continue_Practice = (By.XPATH, "//body/div[@id='app']/main[1]/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]")
    Author_Books = (By.XPATH, "//*[text()='Books With Videos & Solutions']/parent::div/div[2]/div/div/div[1]/div[1]/div/div[1]")
    Practice_Chapter = (By.XPATH, "//*[contains(text(),'Adaptive Practice Chapters From')]/parent::div/div[2]/div/div/div[1]/div/div/div")
    Embibe_big_books = (By.XPATH, "//*[contains(text(), 'Embibe Big Books')]/parent::div/div[2]/div/div[1]/div[1]/div/div/div[1]")
    practice_now_btn = (By.XPATH, "//*[text()='Practice Now']")
    learn_chapter_test_tile = (By.XPATH, "//*[@class='learn-summary-wrapper__section-data-wrapper']/div/div[2]/div[2]/div[1]/div[1]")
    book_toc = (By.CSS_SELECTOR, "[class='toc-content']>div")
    learn_chapter = (By.XPATH, "//*[contains(text(), 'Chapters From')]/parent::div/div[2]/div/div/div[1]/div/div/div")
    book_chapter_practice = (By.XPATH, "//ol[@class=' coobo']/li[1]/img")
    learn_chapter_practice_tile = (By.XPATH, "//div[@class='section-header']/parent::div/div[2]/div[1]/div[5]")
    practice_on_this_chapter = (By.XPATH, "//span[text()='Practice on this Chapter']")

    # def test_practicemodule(self):
    #     self.driver.find_element(*practiceHome.Practice_Module).click()

    def practice_banner(self):
        self.driver.find_element(*PracticeHomePage.Practice_Module).click()
        self.driver.find_element(*PracticeHomePage.Practice_banner_button).click()
        book_toc = self.driver.find_element(*PracticeHomePage.book_toc)
        book_toc.is_displayed()
        self.driver.find_element(*PracticeHomePage.book_chapter_practice).click()
        self.practice_taking()

    def practice_chapters(self):

        self.driver.find_element(*PracticeHomePage.Practice_Module).click()
        self.driver.find_element(*PracticeHomePage.Practice_Chapter).click()
        practice_now_btn = self.driver.find_element(*PracticeHomePage.practice_now_btn)
        practice_now_btn.is_displayed()
        practice_now_btn.click()
        self.practice_taking()

    def author_books(self):

        self.driver.find_element(*PracticeHomePage.Practice_Module).click()
        self.driver.find_element(*PracticeHomePage.Author_Books).click()
        book_toc = self.driver.find_element(*PracticeHomePage.book_toc)
        book_toc.is_displayed()
        self.driver.find_element(*PracticeHomePage.book_chapter_practice).click()
        self.practice_taking()

    def embibe_big_books(self):

        self.driver.find_element(*PracticeHomePage.Practice_Module).click()
        self.driver.find_element(*PracticeHomePage.Embibe_big_books).click()
        book_toc = self.driver.find_element(*PracticeHomePage.book_toc)
        book_toc.is_displayed()
        self.driver.find_element(*PracticeHomePage.book_chapter_practice).click()
        self.practice_taking()

    def practice_taking_in_practice_chapter(self):
        self.driver.find_element(*PracticeHomePage.learn_chapter).click()
        time.sleep(2)
        self.driver.find_element(*PracticeHomePage.practice_on_this_chapter).click()
        time.sleep(5)
        self.driver.find_element(*PracticeHomePage.learn_chapter_practice_tile).click()
        time.sleep(4)
        self.practice_taking()

    def practice_taking(self):
        try:
            for i in range(1, 4):
                try:
                    time.sleep(5)
                    question_element = self.driver.find_element(By.XPATH,
                                                                "//div[@class='Title_title__og5qd']/div[2]/span[2]")
                    question = question_element.text
                    time.sleep(5)
                    print(question)

                    if question_element.is_displayed():
                        if question == "Multiple Choice":
                            time.sleep(5)
                            self.driver.find_element(By.XPATH,
                                                     "//div[@class='Title_title__og5qd']/div/div[2]/span/span/i").click()
                            self.driver.find_element(By.XPATH,
                                                     "//div[@class='question-view-body']/div[2]/div[1]").click()
                            self.driver.find_element(By.XPATH,
                                                     "//div[@class='question-view-body']/div[2]/div[2]").click()
                            self.driver.find_element(By.XPATH, "//*[text()='Check']").click()
                            time.sleep(10)
                            self.driver.find_element(By.XPATH, "//*[text()='Continue']").click()

                        # elif question == "Subjective":
                        #     self.driver.find_element(By.XPATH, "//*[text()='Full Solution']").click()
                        #     time.sleep(10)
                        #     self.driver.find_element(By.XPATH, "//*[text()='Continue']").click()

                        elif question == "Subjective Numerical":
                            self.driver.find_element(By.XPATH,
                                                     "//div[@class='Title_title__og5qd']/div/div[2]/span/span/i").click()
                            time.sleep(5)
                            try:
                                if self.driver.find_element(By.XPATH, "[status='DEFAULT']").is_displayed():
                                    self.driver.find_element(By.XPATH, "[status='DEFAULT']").click()
                                    time.sleep(2)
                                    self.driver.find_element(By.XPATH, "[status='DEFAULT']").send_keys("1")
                                    time.sleep(2)
                                    self.driver.find_element(By.XPATH, "//*[text()='Check']").click()
                                    time.sleep(10)
                                    self.driver.find_element(By.XPATH, "//*[text()='Continue']").click()
                            except:
                                self.driver.find_element(By.XPATH, "//*[text()='Solve With Us']").click()
                                self.driver.find_element(By.XPATH, "//*[text()='Full Solution']").click()
                                time.sleep(10)
                                self.driver.find_element(By.XPATH, "//*[text()='Continue']").click()

                        elif question == "Subjective Answer":
                            time.sleep(5)
                            try:
                                if self.driver.find_element(By.XPATH, "[status='DEFAULT']").is_displayed():
                                    self.driver.find_element(By.XPATH, "[status='DEFAULT']").click()
                                    time.sleep(2)
                                    self.driver.find_element(By.XPATH, "[status='DEFAULT']").send_keys("abc")
                                    time.sleep(2)
                                    self.driver.find_element(By.XPATH, "//*[text()='Check']").click()
                                    time.sleep(10)
                                    self.driver.find_element(By.XPATH, "//*[text()='Continue']").click()
                            except:
                                self.driver.find_element(By.XPATH, "//*[text()='Solve With Us']").click()
                                self.driver.find_element(By.XPATH, "//*[text()='Full Solution']").click()
                                time.sleep(10)
                                self.driver.find_element(By.XPATH, "//*[text()='Continue']").click()

                        elif question == "Fill in The Blanks":
                            time.sleep(5)
                            self.driver.find_element(By.XPATH,
                                                     "//div[@class='Title_title__og5qd']/div/div[2]/span/span/i").click()
                            self.driver.find_element(By.CSS_SELECTOR, "[id='fb-blank-0']").click()
                            self.driver.find_element(By.CSS_SELECTOR, "[status='DEFAULT']").send_keys("XYZ")
                            self.driver.find_element(By.XPATH, "//*[text()='Check']").click()
                            time.sleep(10)
                            self.driver.find_element(By.XPATH, "//*[text()='Continue']").click()

                        elif question == "Integer":
                            time.sleep(5)
                            self.driver.find_element(By.XPATH,
                                                     "//div[@class='Title_title__og5qd']/div/div[2]/span/span/i").click()
                            self.driver.find_element(By.CSS_SELECTOR, "[id='fb-blank-0']").click()
                            self.driver.find_element(By.CSS_SELECTOR, "[status='DEFAULT']").send_keys("1")
                            self.driver.find_element(By.XPATH, "//*[text()='Check']").click()
                            time.sleep(10)
                            self.driver.find_element(By.XPATH, "//*[text()='Continue']").click()

                        elif question == "Multiple Fill in The Blanks":
                            time.sleep(5)
                            self.driver.find_element(By.XPATH,
                                                     "//div[@class='Title_title__og5qd']/div/div[2]/span/span/i").click()
                            self.driver.find_element(By.CSS_SELECTOR, "[id='fb-blank-0']").click()
                            self.driver.find_element(By.CSS_SELECTOR, "[status='DEFAULT']").send_keys("XYZ")
                            time.sleep(3)
                            self.driver.find_element(By.CSS_SELECTOR, "[id='fb-blank-1']").click()
                            time.sleep(2)
                            self.driver.find_element(By.CSS_SELECTOR, "[id='fb-blank-1']>input").send_keys("abc")
                            self.driver.find_element(By.XPATH, "//*[text()='Check']").click()
                            time.sleep(10)
                            self.driver.find_element(By.XPATH, "//*[text()='Continue']").click()

                        elif question in ["True-False", "Single Choice", "Assertion"]:
                            time.sleep(5)
                            self.driver.find_element(By.XPATH,
                                                     "//div[@class='Title_title__og5qd']/div/div[2]/span/span/i").click()
                            self.driver.find_element(By.XPATH,
                                                     "//div[@class='question-view-body']/div[2]/div[1]").click()
                            self.driver.find_element(By.XPATH, "//*[text()='Check']").click()
                            time.sleep(10)
                            self.driver.find_element(By.XPATH, "//*[text()='Continue']").click()

                        elif self.driver.find_element(By.XPATH,
                                                      "//div[@id='PracticeConatiner']/div/div[1]/div/div[1]").is_displayed():
                            print("Learn Intervention screen is displayed")
                            self.driver.find_element(By.XPATH, "//*[text()='Continue Practice']").click()

                        else:
                            self.driver.find_element(By.XPATH, "//*[contains(text(),'Solve')]").click()
                            time.sleep(5)
                            self.driver.find_element(By.XPATH, "//*[contains(text(),'Full Solution')]").click()
                            time.sleep(5)
                            self.driver.find_element(By.XPATH, "//*[contains(text(),'Continue')]").click()
                            time.sleep(5)
                except NoSuchElementException:
                    self.driver.find_element(By.XPATH, "//div[contains(text(), 'Congratulations,')]").is_displayed()
                    print("Congratulations, you have finished this topic. Let's move on to the next one.")


        except NoSuchElementException:
                    self.driver.find_element(By.XPATH, "//div[contains(text(), 'Congratulations,')]").is_displayed()
                    print("Congratulations, you have finished this topic. Let's move on to the next one.")

        self.driver.find_element(By.CSS_SELECTOR,
                                     "i[class='demo-icon demo-icon--filled demo-icon--sm Title_endSessionIcon__2QErK']").click()
        self.driver.find_element(By.XPATH, "//*[text()='End Session']").click()
        time.sleep(5)



















