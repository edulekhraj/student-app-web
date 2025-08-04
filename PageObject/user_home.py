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
    By.XPATH, "//div[@id='embibe-live-classes']/span")
    past_live_class_watch_now_btn = (By.XPATH,
                                     "//div[text()='Past Classes']/parent::div/div[2]/div[2]/div/div[1]/div/div/div/div[5]/button/span/span")
    live_class_watch_recording_btn = (By.XPATH, "//*[text()='Watch Recording']")
    live_class_chat_button = (By.XPATH, "//*[text()='Chat']")
    live_class_performance_button = (By.XPATH, "//*[text()='Performance']")
    embibe_explainers = (By.XPATH, "//*[text()='Embibe Explainers']/parent::div/div[2]/div/div/div[2]/div/div/div")
    recap_video_tile = (By.XPATH, "//*[contains(text(),'Recap Videos from QA Prod')]/parent::div/div[2]/div[2]/div/div[1]/div/div/div")
    assignment_tile = (By.XPATH, "//div[@class='home-assignment-wrapper__section-data-wrapper hide-scrollbar']/div/div[2]/div[1]/div/div[1]")
    prerequisite_video_tile = (By.XPATH, "//*[contains(text(),'Pre-Requisite')]/parent::div/div[2]/div[2]/div/div[1]/div/div/div")
    school_full_test_tile = (By.XPATH, "//*[contains(text(),'Test from QA Prod')]/parent::div/div[2]/div[2]/div/div[1]/div/div/div/img")
    school_chapter_test_tile = (
    By.XPATH, "//*[contains(text(),'Test from QA Prod')]/parent::div/div[2]/div[2]/div/div[2]/div/div/div/img")
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

    def school_assignment_recap_videos(self):
        self.click_element(UserHome.user_home)
        recap_videos_carousel = self.wait_for_visibility((By.XPATH, "//*[contains(text(),'Recap Videos from QA Prod')]"))
        self.driver.execute_script("arguments[0].scrollIntoView();", recap_videos_carousel)
        self.click_element(UserHome.recap_video_tile)
        self.click_element(UserHome.assignment_tile)
        time.sleep(5)

    def school_assignment_prerequisite_videos(self):
        self.click_element(UserHome.user_home)
        prerequisite_videos_carousel = self.wait_for_visibility(
            (By.XPATH, "//*[contains(text(),'Pre-Requisite Readiness Videos')]"))
        self.driver.execute_script("arguments[0].scrollIntoView();", prerequisite_videos_carousel)
        self.click_element(UserHome.prerequisite_video_tile)
        self.click_element(UserHome.assignment_tile)
        time.sleep(5)

    def school_assignment_full_tests(self):
        self.click_element(UserHome.user_home)
        school_test_carousel = self.wait_for_visibility(
            (By.XPATH, "//*[contains(text(),'Test from')]"))
        self.driver.execute_script("arguments[0].scrollIntoView();", school_test_carousel)
        self.click_element(UserHome.school_full_test_tile)
        self.click_element(UserHome.assignment_tile)
        self.test_taking()

    def school_assignment_chapter_tests(self):
        self.click_element(UserHome.user_home)
        school_test_carousel = self.wait_for_visibility(
            (By.XPATH, "//*[contains(text(),'Test from')]"))
        self.driver.execute_script("arguments[0].scrollIntoView();", school_test_carousel)
        self.click_element(UserHome.school_chapter_test_tile)
        self.click_element(UserHome.assignment_tile)
        time.sleep(5)
        self.test_taking()

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
        self.driver.get("https://www.embibe.com/user-home/embibe-live-classes")
        time.sleep(5)
        # self.driver.execute_script("window.scrollBy(0, 200);")
        # self.click_element(UserHome.UH_live_class_btn)
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
        self.driver.find_element(*UserHome.embibe_explainers).click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, "//*[text()='Bookmark']").click()
        time.sleep(3)
        self.driver.get("https://www.embibe.com/user-home")
        # self.click_element(UserHome.user_home)
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

