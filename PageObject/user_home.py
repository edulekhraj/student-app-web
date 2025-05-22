import time

from PageObject.practice_home_page import PracticeHomePage
from PageObject.test_home_page import TestHomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class UserHome(PracticeHomePage, TestHomePage):

    def __init__(self, driver):
        self.driver = driver

    user_home = (By.XPATH, "//span[text()='Home']")
    bookmark_video_tile = (
        By.XPATH, "//div[text()='My Bookmarks']/parent::div/div[2]/div/div[1]/div[1]/div/div/div/div[2]")
    bookmark_question_tile = (By.XPATH, "//div[text()='My Bookmarks']/parent::div/div[2]/div/div[1]/div[2]/div/div")
    play_all_btn = (By.XPATH, "//span[text()='Play All']")
    practice_all_btn = (By.XPATH, "//span[text()='Practice All']")
    video_bookmark = (By.XPATH, "//*[@class='summary-banner-wrapper__icon-title']/span")
    practice_bookmark_button = (By.XPATH, "//i[@class='demo-icon demo-icon--filled demo-icon--xs icon-style']")
    video_carousel = (
        By.XPATH, "//div[text()='Trending Videos for Your Exam']/parent::div/div[2]/div[2]/div/div[4]/div")
    add_fav_book = (By.XPATH,
                    "//div[@id='app']/main/div[2]/div/div[4]/div[2]/div/div/div[1]/div/div/div/div[1]/div")
    add_book = (By.XPATH, "//*[@id='app']/main/div[2]/div/div/div[1]/div[4]/div/div[2]/div/div[4]/div/div/div/div[2]")
    done_button = (By.XPATH, "//*[text()='Done']")
    test_tile = (By.XPATH, '//*[@id="app"]/main/div[2]/div/div[6]/div[2]/div[2]/div/div[1]/div/div/div/div[4]')
    view_test_fb = (By.XPATH, "//*[text()='View Test Feedback']")
    revision_list = (By.ID, "revision-lists")
    rl_important_ques = (By.XPATH, "//*[text()='IMPORTANT QUESTIONS']")
    rl_important_ques_chap_1 = (
    By.XPATH, "//*[text()='IMPORTANT QUESTIONS']/parent::div/parent::div/parent::div/parent::div/div[2]/div[1]")
    rl_practice_btn = (By.CSS_SELECTOR, "[class='accordian-button-wrapper']")
    rl_filter_dd = (By.XPATH, "//*[text()='Questions To Revise']")
    rl_topics_to_revise = (By.XPATH, "//*[text()='Topics To Revise']")
    rl_solved_examples = (By.XPATH, "//div[@class='accordion-wrapper topic-accordian-wrapper']/div[1]/div[1]/div/div/i")
    rl_solved_examples_chap_1 = (
    By.XPATH, "//div[@class='accordion-wrapper topic-accordian-wrapper']/div[1]/div[2]/div[1]")
    rl_topics_to_revise_learn_button = (By.XPATH,
                                        "//div[@class='accordion-wrapper topic-accordian-wrapper']/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div[1]")
    rl_sub_dd = (By.XPATH, "//*[text()='All Subjects']")
    rl_sub_options = (
    By.XPATH, "//*[@class='eds-dropdown-menu__wrapper revision-list-filter-menu-wrapper']/li[2]/button/div/span")
    rl_unit_dd = (By.XPATH, "//*[text()='All Units']")
    rl_chapters_dd = (By.XPATH, "//*[text()='All Chapters']")
    UH_live_class_btn = (
    By.XPATH, "//*[@id='embibe-live-classes']/img")
    past_live_class_watch_now_btn = (By.XPATH,
                                     "//*[text()='Past Live Classes']/parent::div/div[2]/div[2]/div/div[@data-index='0']/div/div/div/div[5]/button")
    live_class_watch_recording_btn = (By.XPATH, "//*[text()='Watch Recording']")
    live_class_chat_button = (By.XPATH, "//*[text()='Chat']")
    live_class_performance_button = (By.XPATH, "//*[text()='Performance']")

    def click_element(self, locator, timeout=10):
        """Click an element after waiting for it to be clickable."""
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator)).click()

    def wait_for_visibility(self, locator, timeout=10):
        """Wait for an element to be visible."""
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def scroll_to_bottom(self):
        """Scroll to the bottom of the page."""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def practice_in_revision_list(self):
        self.click_element(UserHome.user_home)
        self.click_element(UserHome.revision_list)
        self.click_element(UserHome.rl_important_ques)
        self.click_element(UserHome.rl_important_ques_chap_1)
        self.click_element(UserHome.rl_practice_btn)

        assert self.wait_for_visibility((By.CSS_SELECTOR, ".demo-icon.demo-icon--filled.demo-icon--xs.icon-style")), \
            "Expected icon not found."

    def learn_in_revision_list(self):
        self.click_element(UserHome.user_home)
        self.click_element(UserHome.revision_list)
        self.click_element(UserHome.rl_filter_dd)
        self.click_element(UserHome.rl_topics_to_revise)
        self.click_element(UserHome.rl_solved_examples)
        self.click_element(UserHome.rl_solved_examples_chap_1)
        self.click_element(UserHome.rl_topics_to_revise_learn_button)

        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element((By.CLASS_NAME, "loader"))
        )
        self.recommendlearningvideos()

    def watch_past_live_class(self):
        self.click_element(UserHome.user_home)
        time.sleep(5)
        self.click_element(UserHome.UH_live_class_btn)
        self.click_element(UserHome.past_live_class_watch_now_btn)
        self.click_element(UserHome.live_class_watch_recording_btn)
        self.click_element(UserHome.live_class_performance_button)
        time.sleep(5)
        self.wait_for_visibility(UserHome.live_class_chat_button)
        self.click_element(UserHome.live_class_performance_button)

        assert self.driver.find_element(By.CSS_SELECTOR, "[class='text']").text == \
               "You have not attended this class!", "Unexpected class status."

    def add_favourite_book(self):
        self.click_element(UserHome.user_home)

        fav_books_element = self.wait_for_visibility((By.XPATH, "//*[contains(text(),'My Favourite Books')]"))
        self.driver.execute_script("arguments[0].scrollIntoView();", fav_books_element)
        time.sleep(5)
        self.click_element(UserHome.add_fav_book)

    #     icon_xpath = "//*[@id='app']/main/div[2]/div/div/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[2]/i"
    #
    #     try:
    #     # Check if the element is displayed and click it
    #         icon_element = self.driver.find_element(By.XPATH, icon_xpath)
    #         if icon_element.is_displayed():
    #             icon_element.click()
    #     except Exception as e:
    #         print(f"Icon element not found or not clickable: {e}")
    #
    # # Click on the 'Add Book' button
    #     WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable(UserHome.add_book)
    #     ).click()
    #
    # # Click on the 'Done' button
    #     WebDriverWait(self.driver, 10).until(
    #     EC.element_to_be_clickable(UserHome.done_button)
    #     ).click()



    def video_bookmark_button(self):
        self.click_element(UserHome.video_carousel)
        self.click_element((By.XPATH, "//*[@class='summary-banner-wrapper__icon-title']/span"))

        desc = self.wait_for_visibility((By.XPATH, "//*[@class='eds-row eds-row-start eds-row-top']/div/p")).text
        print(desc)

        self.click_element(UserHome.user_home)
        self.scroll_to_bottom()

        self.click_element(UserHome.bookmark_video_tile)

        exp_desc = self.wait_for_visibility(
            (By.XPATH, "//div[@class='section-division']/div[1]/div/div[2]/div/div[1]/div")
        ).text
        print(exp_desc)

        assert desc == exp_desc, "Bookmark video descriptions do not match."

    def play_bookmark_video(self):
        self.click_element(UserHome.user_home)
        self.scroll_to_bottom()
        self.click_element(UserHome.bookmark_video_tile)
        self.click_element(UserHome.play_all_btn)

    def practice_bookmark_question(self):
        self.click_element(UserHome.user_home)
        self.scroll_to_bottom()
        self.click_element(UserHome.bookmark_question_tile)
        self.click_element(UserHome.practice_all_btn)

    def test_i_have_taken(self):
        self.click_element(UserHome.user_home)
        self.scroll_to_bottom()
        self.click_element(UserHome.test_tile)
        self.click_element(UserHome.view_test_fb)

        score = self.wait_for_visibility(
            (By.CSS_SELECTOR, "[class='tf-score-card__item-value-score']>div:nth-of-type(1)")
        )
        print(score.text)
        score.click()

        obtained_score = self.wait_for_visibility(
            (By.CSS_SELECTOR, "[class='tf-score-value']>div:nth-of-type(1)")
        ).text
        print(obtained_score)

        # Handling negative and positive behaviors
        try:
            self.click_element((By.XPATH, "//div[@class='test-feedback-container ']/div[2]/div[2]/div/div[2]"))
            self.click_element((By.XPATH, "//div[@class='tf-section-detail-page']/div/div[2]/div[1]/div[1]/div/div[1]"
                                          "/div[1]/picture"))
        except NoSuchElementException:
            print("No Negative Behavior")

        self.click_element((By.XPATH, "//*[text()='Time Management']"))
        self.click_element((By.XPATH, "//*[contains(text(), 'Chapterwise Analysis')]"))
        self.click_element((By.XPATH, "//*[contains(text(), 'Overall Strong')]"))
        self.click_element((By.XPATH, "//*[contains(text(), 'Questionwise Analysis')]"))

