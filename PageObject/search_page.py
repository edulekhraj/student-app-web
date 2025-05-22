
import time
from Utilities import utility
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from PageObject.learn_home_page import LearnHomePage
from PageObject.practice_home_page import PracticeHomePage
from PageObject.test_home_page import TestHomePage


class SearchPage:

    def __init__(self,driver):
        self.driver=driver

    search_field = (By.NAME, "search-box")
    videos_tab= (By.XPATH, "//span[contains(text(), 'Videos')]")
    books_tab= (By.XPATH, "//span[contains(text(), 'Books')]")
    questions_tab= (By.XPATH, "//span[contains(text(), 'Questions')]")
    practice_tab= (By.XPATH, "//div[@class='filter_name']/span[contains(text(), 'Practice')]")
    test_tab= (By.XPATH, "//div[@class='filter_name']/span[contains(text(), 'Test')]")
    ptr_tabs= (By.XPATH, "//div[@class='filter_name']/span[contains(text(), 'Points to Remember')]")
    search_result_tile = (By.XPATH, "//div[@class='embibe-search-result-data']/div/div[1]/div/div[1]")
    practice_now = (By.XPATH, "//span[contains(text(),'Practice Now')]")
    goal_update_popup = (By.XPATH, "//span[contains(text(),'Do you want to take ')]")
    update_btn_click =(By.XPATH, "//span[contains(text(),'Update')]")

    keyword = utility.utility.readConfig('Prod', 'search_keyword')

    def search_videos_tabs(self):

        try:
            self.driver.find_element(*SearchPage.search_field).click()
            self.driver.find_element(*SearchPage.search_field).send_keys(self.keyword)
            self.driver.find_element(*SearchPage.search_field).send_keys(Keys.ENTER)
            time.sleep(5)
            self.driver.find_element(*SearchPage.videos_tab).click()
            time.sleep(2)
            self.driver.find_element(*SearchPage.search_result_tile).click()
            time.sleep(3)
            self.play_video_button()
            try:
                self.driver.find_element(*LearnHomePage.more_topic).click()
                self.driver.find_element(*LearnHomePage.topic_video).click()
                self.play_video_button()
                self.driver.back()
            except NoSuchElementException:
                print("More Topics Link is not present")

            try:
                self.driver.find_element(*LearnHomePage.related_video).click()
                self.driver.find_element(*LearnHomePage.related_video_click).click()
                self.play_video_button()
                self.driver.back()

            except NoSuchElementException:
                print("Related Videos Link is not present")

        except NoSuchElementException as e:
                print("No Search result Found for the searched topic", e)

    def search_books_tabs(self):
        try:
            self.driver.find_element(*SearchPage.search_field).click()
            self.driver.find_element(*SearchPage.search_field).send_keys(self.keyword)
            self.driver.find_element(*SearchPage.search_field).send_keys(Keys.ENTER)
            time.sleep(5)
            self.driver.find_element(*SearchPage.books_tab).click()
            time.sleep(3)
            self.driver.find_element(*SearchPage.search_result_tile).click()
            time.sleep(8)
            self.driver.find_element(*LearnHomePage.book_video_tile).click()
            self.driver.find_element(By.XPATH, "//*[@id='app']/main/div[2]/div[2]/div[1]/div/div[1]/div[2]/div").is_displayed()
        except NoSuchElementException as e:
            print("No Search result Found for the searched topic", e)

    def search_questions_tab(self):
        try:
            self.driver.find_element(*SearchPage.search_field).click()
            self.driver.find_element(*SearchPage.search_field).send_keys(self.keyword)
            self.driver.find_element(*SearchPage.search_field).send_keys(Keys.ENTER)
            time.sleep(5)
            self.driver.find_element(*SearchPage.questions_tab).click()
            time.sleep(3)
            self.driver.find_element(*SearchPage.search_result_tile).click()
            time.sleep(3)
        except NoSuchElementException as e:
            print("No Search result Found for the searched topic", e)

    def search_practice_tab(self):
        try:
            self.driver.find_element(*SearchPage.search_field).click()
            self.driver.find_element(*SearchPage.search_field).send_keys(self.keyword)
            self.driver.find_element(*SearchPage.search_field).send_keys(Keys.ENTER)
            time.sleep(10)
            self.driver.find_element(*SearchPage.practice_tab).click()
            time.sleep(3)
            self.driver.find_element(*SearchPage.search_result_tile).click()
            time.sleep(3)
            try:
                self.driver.find_element(*SearchPage.practice_now).is_displayed()
                php = PracticeHomePage(self.driver)
                self.driver.find_element(*SearchPage.practice_now).click()
                php.practice_taking()

            except:
                self.play_video_button()



        except NoSuchElementException as e:
            print("No Search result Found for the searched topic", e)

    def search_test_tab(self):
        try:
            self.driver.find_element(*SearchPage.search_field).click()
            self.driver.find_element(*SearchPage.search_field).send_keys(self.keyword)
            self.driver.find_element(*SearchPage.search_field).send_keys(Keys.ENTER)
            time.sleep(5)
            self.driver.find_element(*SearchPage.test_tab).click()
            time.sleep(3)
            self.driver.find_element(*SearchPage.search_result_tile).click()
            time.sleep(3)
            thp = TestHomePage(self.driver)
            try:
                self.driver.find_element(*SearchPage.goal_update_popup).is_displayed()
                self.driver.find_element(*SearchPage.update_btn_click).click()
                thp.test_taking()
            except:
                thp = TestHomePage(self.driver)
                thp.test_taking()

        except NoSuchElementException as e:
            print("No Search result Found for the searched topic", e)

    def search_ptr_tab(self):
        try:
            self.driver.find_element(*SearchPage.search_field).click()
            self.driver.find_element(*SearchPage.search_field).send_keys(self.keyword)
            self.driver.find_element(*SearchPage.search_field).send_keys(Keys.ENTER)
            time.sleep(5)
            self.driver.find_element(*SearchPage.ptr_tabs).click()
            time.sleep(3)
            self.driver.find_element(*SearchPage.search_result_tile).click()
            time.sleep(3)
        except NoSuchElementException as e:
            print("No Search result Found for the searched topic", e)

    def play_video_button(self):

        self.driver.find_element(*LearnHomePage.learn_button).click()
        try:
            time.sleep(3)
            popup = self.driver.find_element(By.XPATH,
                                             "//span[text()='Continue from where you left?']/parent::div/parent::div")
            if popup.is_displayed():
                time.sleep(2)
                self.driver.find_element(By.XPATH, "//span[text()='Yes']").click()
                time.sleep(10)
                self.driver.find_element(*LearnHomePage.learn_button).send_keys(keys.Keys.ESCAPE)
                self.driver.find_element(*LearnHomePage.learn_button).send_keys(keys.Keys.ESCAPE)
                time.sleep(5)
        except NoSuchElementException:
            time.sleep(10)
            self.driver.find_element(*LearnHomePage.learn_button).send_keys(keys.Keys.ESCAPE)
            self.driver.find_element(*LearnHomePage.learn_button).send_keys(keys.Keys.ESCAPE)
            time.sleep(5)

        except ElementClickInterceptedException:
            time.sleep(5)
            self.driver.find_element(*LearnHomePage.learn_button).send_keys(keys.Keys.ESCAPE)
            self.driver.find_element(*LearnHomePage.learn_button).send_keys(keys.Keys.ESCAPE)


