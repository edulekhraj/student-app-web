import time

from selenium.common import NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

from PageObject.test_home_page import TestHomePage


class LearnHomePage:

    def __init__(self, driver):
        self.driver = driver

    Curated_Video = (
    By.XPATH, '//*[text() = "World''s Best Curated Learning Content"]/parent::div/div[2]/div/div/div[1]/div/div/div')
    learn_chapter = (By.XPATH, "//*[contains(text(), 'Chapters From')]/parent::div/div[2]/div/div/div[1]/div/div/div")
    trending_videos = (
    By.XPATH, "//*[text()='Trending Videos for Your Exam']/parent::div/div[2]/div/div/div[1]/div/div/div")
    embibe_explainers = (By.XPATH, "//*[text()='Embibe Explainers']/parent::div/div[2]/div/div/div[1]/div/div/div")
    learn_module = (By.CSS_SELECTOR, "[to='/learn/home']")
    hero_button = (By.CSS_SELECTOR, "[data-tour='learn-button']")
    subject_buttons = (By.XPATH, "//div[text()= 'Subjects']/parent::div/div[2]/div/div/div")
    # last_subject_button = (By.CSS_SELECTOR, "[id='subL']")
    video_play = (By.CSS_SELECTOR, "[data-tour='learn-button']")
    continue_learning = (By.XPATH, '//*[text() = "Continue Learning"]/parent::div/div[2]/div/div/div[1]/div/div/div')
    learn_button = (By.XPATH, "//div[@class='action-bar-wrapper']/div/button")
    more_topic = (By.XPATH, "//*[text()='More on this Topic']")
    topic_video = (By.XPATH, "//*[@class = 'video-summary-wrapper__section-data-wrapper']/div/div[2]/div[1]/div/div[1]")
    related_video = (By.XPATH, "//*[text()='Related Videos']")
    related_video_click = (By.XPATH, "//div[@class='video-summary-wrapper__section-data-wrapper']/div/div[2]/div[1]/div/div[1]")
    # all_videos = (By.XPATH, "//*[@class='learn-summary-wrapper__section-data-wrapper']/div/div[2]/div[2]/div[1]/div[1]")
    topic_in_this_chapter = (By.XPATH, "//*[text()='Topics in this Chapter']")
    video_click = (
    By.XPATH, "//*[@class='learn-summary-wrapper__section-data-wrapper']/div/div[2]/div[2]/div[1]/div[1]")
    test_on_this_chapter = (By.XPATH, "//span[text()='Tests on this Chapter']")
    hero_banner_sub = (By.XPATH, "//*[contains(@class,'banner--info-content')]/div/div[2]/div/div[1]/span[1]/span[1]")
    practice_module = (By.XPATH, "//*[text()='Practice']")
    test_module = (By.XPATH, "//*[text()='Test']")
    ptr = (By.XPATH, "//*[text()='Points to Remember']")
    prerequisite = (By.XPATH, "//*[text()='Prerequisite Topics to ace this Topic']")
    practice_banner_button = (By.XPATH, "//*[text()='Practice from Book']")
    custom_test = (By.XPATH, "//div[contains(text(),'My Custom Tests')]")
    achieve_module = (By.CSS_SELECTOR, "[to='/achieve/landing']")
    start_achieving = (By.XPATH, "//span[contains(text(),'Start Achieving Now')]")
    user_home = (By.XPATH, "//span[contains(text(),'Home')]")
    parent_assignment = (By.XPATH, "//div[contains(text(),'Assignment from My Parents')]")
    enrich_your_learning_carousel = (By.XPATH, "//*[contains(text(),'Enrich')]")
    enrich_tile = (By.XPATH, "//*[contains(text(),'Enrich')]/parent::div/div[2]/div[2]/div[1]/div[1]/div/div/div")
    author_books = (By.XPATH, "//*[contains(text(), 'Books With')]")
    embibe_big_book = (By.XPATH, "//*[contains(text(), 'Books With')]")
    book_chapters_list = (By.XPATH, "//li[@class='rowBookList list-center ']")
    book_topic_practice_tile = (By.XPATH, "//ol[@class=' coobo']/li[contains(@class, 'rowPracticeList')]")
    bookmark_button = (By.XPATH, "//*[@class='summary-banner-wrapper__icon-title']/span")
    book_cheat_sheet = (By.XPATH, "//ol[@class='toc-content']/li[@class='rowPracticeList cheatSheetTile']")
    book_cheat_sheet_tile = (By.CSS_SELECTOR, "[alt='cheatsheet']")
    book_cheat_sheet_close_btn = (By.CSS_SELECTOR, "[alt='icon']")

    sub_embibe_explainers = (By.XPATH, "//*[contains(text(), 'Embibe Explainers For')]")
    sub_embibe_explainers_tile = (
    By.XPATH, "//*[contains(text(), 'Embibe Explainers For')]/parent::div/div[2]/div/div/div[1]/div/div/div")
    sub_trendingvideos = (By.XPATH, "//*[contains(text(), 'Trending Videos for Your Exam')]")
    sub_trendingvideos_tile = (
    By.XPATH, "//*[contains(text(), 'Trending Videos for Your Exam')]/parent::div/div[2]/div/div/div[1]/div/div/div")
    sub_enrich_your_learning_tile = (
    By.XPATH, "//*[contains(text(), 'Enrich Your Learning')]/parent::div/div[2]/div[2]/div/div[1]/div/div/div")

    sub_topic_video = (
    By.XPATH, "//body[1]/div[1]/main[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]")
    sub_related_video = (By.XPATH,
                         "//body/div[@id='app']/main[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[5]")
    sub_all_video = (By.XPATH,
                     "//body/div[@id='app']/main[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[6]")
    sub_prerequisite_video = (By.XPATH,
                              "//body/div[@id='app']/main[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]")
    sub_author_books = (
    By.XPATH, "//*[contains(text(), 'Books With')]/parent::div/div[2]/div[2]/div/div[1]/div/div/div")
    sub_embibe_big_book = (By.XPATH, "//*[contains(text(), 'Big Books')]/parent::div/div[2]/div/div/div/div/div/div")
    book_video_tile = (By.XPATH, "//ol[@class=' coobo']/li[1]/div/div[1]")

    def learn_hero_banner(self):
        self.driver.find_element(*LearnHomePage.learn_module).click()
        self.driver.find_element(*LearnHomePage.hero_button).is_displayed()
        total_subject = self.driver.find_elements(*LearnHomePage.subject_buttons)
        count = len(total_subject)
        for i in range(0, count - 2):
            self.driver.find_element(By.CSS_SELECTOR, "[id='sub" + str(i) + "']").click()
            self.driver.refresh()
            self.driver.find_element(*LearnHomePage.hero_button).click()
            time.sleep(20)
            self.driver.find_element(*LearnHomePage.hero_button).send_keys(keys.Keys.ESCAPE)
            self.driver.find_element(*LearnHomePage.hero_button).send_keys(keys.Keys.ESCAPE)

    def Banner_belongs_to_the_current_exam(self):
        self.driver.find_element(*LearnHomePage.learn_module).click()
        self.driver.find_element(*LearnHomePage.hero_button).is_displayed()
        total_subject = self.driver.find_elements(*LearnHomePage.subject_buttons)
        count = len(total_subject)
        for i in range(0, count - 2):
            self.driver.find_element(By.CSS_SELECTOR, "[id='sub" + str(i) + "']").click()
            self.driver.refresh()
            subname = self.driver.find_element(By.CSS_SELECTOR, "[id='sub" + str(i) + "']").text
            hero_banner_subject = self.driver.find_element(*LearnHomePage.hero_banner_sub).text
            print(subname, hero_banner_subject)
            assert subname.casefold() == hero_banner_subject.casefold(), "Assertion failed: subname is not equal to hero_banner_subject"

        self.driver.find_element(*LearnHomePage.last_subject_button).click()
        subname = self.driver.find_element(By.CSS_SELECTOR, "[id='sub" + str(i) + "']").text
        hero_banner_subject = self.driver.find_element(*LearnHomePage.hero_banner_sub).text
        print(subname, hero_banner_subject)
        assert subname.casefold() == hero_banner_subject.casefold(), "Assertion failed: subname is not equal to hero_banner_subject"

    def click_each_module_Tab_is_navigation_to_module(self):
        self.driver.find_element(*LearnHomePage.learn_module).click()
        self.driver.find_element(*LearnHomePage.hero_button).is_displayed()
        self.driver.find_element(*LearnHomePage.test_module).click()
        self.driver.find_element(*LearnHomePage.custom_test).click()
        self.driver.find_element(*LearnHomePage.practice_module).click()
        self.driver.find_element(*LearnHomePage.practice_banner_button).is_displayed()
        self.driver.find_element(*LearnHomePage.achieve_module).click()
        # self.driver.find_element(*LearnHomePage.start_achieving).is_displayed()
        self.driver.find_element(*LearnHomePage.user_home).click()
        self.driver.find_element(*LearnHomePage.parent_assignment).is_displayed()

    def learn_trending_videos(self):
        self.driver.find_element(*LearnHomePage.trending_videos).click()
        time.sleep(5)
        self.play_video_button()
        try:
            self.driver.find_element(*LearnHomePage.more_topic).click()
            self.driver.find_element(*LearnHomePage.topic_video).click()
            self.play_video_button()
            self.driver.back()
        except NoSuchElementException:
            print("More Topics Link is not present")

        # try:
        #     self.driver.find_element(*LearnHomePage.related_video).click()
        #     self.driver.find_element(*LearnHomePage.related_video_click).click()
        #     self.play_video_button()
        #     self.driver.back()
        #
        # except NoSuchElementException:
        #     print("Related Videos Link is not present")

    def learn_author_books(self):
        try:
            self.driver.find_element(*LearnHomePage.author_books).is_displayed()
            time.sleep(5)
            # self.driver.find_element(*LearnHomePage.sub_embibe_explainers).click()
            self.driver.find_element(*LearnHomePage.sub_author_books).click()
            self.driver.find_element(*LearnHomePage.book_video_tile).click()
            try:
                popup = self.driver.find_element(By.CSS_SELECTOR, "[class='sc-llJcti cLATmR sc-jfmDQi LQhpp']")
                if popup.is_displayed():
                    time.sleep(2)
                    self.driver.find_element(By.CSS_SELECTOR,
                                             "[class='sc-gicCDI kMRQrC']>button:nth-of-type(1)").click()
                    time.sleep(10)
                    for _ in range(4):
                        self.driver.back()
            except NoSuchElementException:
                time.sleep(10)
                # self.driver.find_element(*LearnHomePage.learn_button).send_keys(keys.Keys.ESCAPE)
                # self.driver.find_element(*LearnHomePage.learn_button).send_keys(keys.Keys.ESCAPE)
                # time.sleep(5)
                for _ in range(4):
                    self.driver.back()

            except ElementClickInterceptedException:
                time.sleep(5)
                # self.driver.find_element(*LearnHomePage.learn_button).send_keys(keys.Keys.ESCAPE)
                # self.driver.find_element(*LearnHomePage.learn_button).send_keys(keys.Keys.ESCAPE)
                for _ in range(4):
                    self.driver.back()
        except NoSuchElementException:
            print("No Books with videos and solutions")

    def learn_select_chapter_topics_in_author_books(self):
        try:
            self.driver.find_element(*LearnHomePage.author_books).is_displayed()
            time.sleep(5)
            self.driver.find_element(*LearnHomePage.sub_author_books).click()
            ele = self.driver.find_elements(*LearnHomePage.book_chapters_list)
            for i in range(0, len(ele)):
                time.sleep(1)
                self.driver.find_element(By.XPATH, "//ol[@class='toc-content']/li[@id='ROW 0" + str(i) + "']").click()

        except NoSuchElementException:
            print("No Books with videos and solutions")

    def learn_cheat_sheet_present_in_author_books(self):
        try:
            self.driver.find_element(*LearnHomePage.author_books).is_displayed()
            time.sleep(5)
            self.driver.find_element(*LearnHomePage.sub_author_books).click()
            ele = self.driver.find_elements(*LearnHomePage.book_chapters_list)
            for i in range(0, len(ele)):
                self.driver.find_element(By.XPATH, "//ol[@class='toc-content']/li[@id='ROW 0" + str(i) + "']").click()
                try:
                    if self.driver.find_element(*LearnHomePage.book_cheat_sheet).is_displayed():
                        time.sleep(3)
                        self.driver.find_element(*LearnHomePage.book_cheat_sheet_tile).click()
                        time.sleep(3)
                        self.driver.find_element(*LearnHomePage.book_cheat_sheet_close_btn).click()
                    else:
                        print("Element is not displayed")
                except StaleElementReferenceException:
                    print("Stale Element Exception occurred. Trying again...")


        except NoSuchElementException:
            print("No Books with videos and solutions")

    def learn_embibe_big_books(self):
        try:
            self.driver.find_element(*LearnHomePage.author_books).is_displayed()
            time.sleep(5)
            # self.driver.find_element(*LearnHomePage.sub_embibe_explainers).click()
            self.driver.find_element(*LearnHomePage.sub_author_books).click()
            self.driver.find_element(*LearnHomePage.book_video_tile).click()
            try:
                popup = self.driver.find_element(By.CSS_SELECTOR, "[class='sc-llJcti cLATmR sc-jfmDQi LQhpp']")
                if popup.is_displayed():
                    time.sleep(2)
                    self.driver.find_element(By.CSS_SELECTOR,
                                             "[class='sc-gicCDI kMRQrC']>button:nth-of-type(1)").click()
                    time.sleep(10)
                    for _ in range(4):
                        self.driver.back()
            except NoSuchElementException:
                time.sleep(10)
                # self.driver.find_element(*LearnHomePage.learn_button).send_keys(keys.Keys.ESCAPE)
                # self.driver.find_element(*LearnHomePage.learn_button).send_keys(keys.Keys.ESCAPE)
                # time.sleep(5)
                for _ in range(4):
                    self.driver.back()

            except ElementClickInterceptedException:
                time.sleep(5)
                # self.driver.find_element(*LearnHomePage.learn_button).send_keys(keys.Keys.ESCAPE)
                # self.driver.find_element(*LearnHomePage.learn_button).send_keys(keys.Keys.ESCAPE)
                for _ in range(4):
                    self.driver.back()
        except NoSuchElementException:
            print("No Books with videos and solutions")

    def learn_embibe_explainers(self):
        self.driver.find_element(*LearnHomePage.embibe_explainers).click()
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

    def learn_continue_learning(self):
        self.driver.find_element(*LearnHomePage.continue_learning).click()
        self.play_video_button()
        self.driver.back()

    def learn_learn_chapter(self):
        self.driver.find_element(*LearnHomePage.learn_chapter).click()
        time.sleep(5)

        # self.play_video_button()
        # try:
        #     self.driver.find_element(*LearnHomePage.video_click).click()
        #     time.sleep(5)
        #     self.play_video_button()
        #     self.driver.back()
        # except:
        #     print("No Topic in this Chapter link present")
        # try:
        #     self.driver.find_element(*LearnHomePage.topic_in_this_chapter).click()
        #     time.sleep(2)
        #     self.driver.find_element(*LearnHomePage.video_click).click()
        #     time.sleep(5)
        #     self.play_video_button()
        #     self.driver.back()
        # except:
        #     print("No Topic in this Chapter link present")
        #
        # self.driver.find_element(*LearnHomePage.ptr).click()
        # try:
        #     self.driver.find_element(*LearnHomePage.prerequisite).click()
        #     self.driver.find_element(*LearnHomePage.video_click).click()
        #     time.sleep(5)
        #     self.play_video_button()
        #     self.driver.back()
        # except:
        #     print("No Prerequisite Videos present")

    def sub_learn_chapter(self):
        self.driver.find_element(*LearnHomePage.learn_module).click()
        total_subject = self.driver.find_elements(*LearnHomePage.subject_buttons)
        count = len(total_subject)
        for i in range(2, count + 1):
            self.driver.find_element(By.XPATH, "//div[@class='section subject-section']/div[2]/div/div/div[" + str(
                i) + "]").click()
            self.driver.find_element(*LearnHomePage.learn_chapter).click()
            time.sleep(5)
            self.play_video_button()
            try:
                self.driver.find_element(*LearnHomePage.topic_in_this_chapter).click()
                time.sleep(3)
                self.driver.find_element(*LearnHomePage.video_click).click()
                time.sleep(3)
                self.play_video_button()
                self.driver.back()
            except:
                print("Topics in this Chapter link is not present")

            self.driver.find_element(*LearnHomePage.ptr).click()

            try:
                self.driver.find_element(*LearnHomePage.prerequisite).click()
                self.driver.find_element(*LearnHomePage.video_click).click()
                time.sleep(5)
                self.play_video_button()
                self.driver.back()
                self.driver.back()
                self.driver.back()
            except:
                print("No PreRequisite videos present")

        # self.driver.find_element(*LearnHomePage.last_subject_button).click()
        # self.driver.find_element(*LearnHomePage.learn_chapter).click()
        # time.sleep(5)
        # self.play_video_button()
        #
        # try:
        #     self.driver.find_element(*LearnHomePage.topic_in_this_chapter).click()  # need to check
        #     time.sleep(5)
        #     self.driver.find_element(*LearnHomePage.video_click).click()
        #     self.play_video_button()
        #     self.driver.back()
        # except:
        #     print("Topic in this Chapter is not present")
        #
        # self.driver.find_element(*LearnHomePage.ptr).click()
        # try:
        #     self.driver.find_element(*LearnHomePage.prerequisite).click()
        #     self.driver.find_element(*LearnHomePage.video_click).click()
        #     time.sleep(5)
        #     self.play_video_button()
        #     self.driver.back()
        #     self.driver.back()
        # except:
        #     print("No Prerequisite Videos Present")

    def all_subject_tile_is_present_in_LPT(self):
        # self.driver.find_element(*LearnHomePage.learn_module).click()
        learn_total_subject = self.driver.find_elements(*LearnHomePage.subject_buttons)
        learn_sub_count = len(learn_total_subject)

        self.driver.find_element(*LearnHomePage.test_module).click()
        test_total_subject = self.driver.find_elements(*LearnHomePage.subject_buttons)
        test_sub_count = len(test_total_subject)

        self.driver.find_element(*LearnHomePage.practice_module).click()
        practice_total_subject = self.driver.find_elements(*LearnHomePage.subject_buttons)
        practice_sub_count = len(practice_total_subject)

        assert learn_sub_count == test_sub_count == practice_sub_count, "Assertion failed: Not all elements have the same value"

    def enrich_your_learning_carousels(self):
        try:
            self.driver.find_element(*LearnHomePage.enrich_your_learning_carousel).is_displayed()
            time.sleep(5)
            self.driver.find_element(*LearnHomePage.enrich_tile).click()
            self.play_video_button()

            try:
                self.driver.find_element(*LearnHomePage.more_topic).click()
                time.sleep(3)
                self.driver.find_element(*LearnHomePage.topic_video).click()
                time.sleep(5)
                self.play_video_button()
                self.driver.back()
            except NoSuchElementException:
                print("No Topic Videos Present")
                self.driver.back()

            # try:
            #     self.driver.find_element(*LearnHomePage.related_video).click()
            #     time.sleep(5)
            #     self.driver.find_element(*LearnHomePage.related_video_click).click()
            #     time.sleep(5)
            #     self.play_video_button()
            #     self.driver.back()
            #     self.driver.back()
            # except NoSuchElementException:
            #     print("No related Videos Present")
            #     self.driver.back()

        except NoSuchElementException:
            print("Enrich Your Carousel is not present")

    def sub_embibe_explainers_carousels(self):
        total_subject = self.driver.find_elements(*LearnHomePage.subject_buttons)
        count = len(total_subject)
        print(count)
        for i in range(2, count):
            self.driver.find_element(By.XPATH, "//div[@class='section subject-section']/div[2]/div/div/div[" + str(
                i) + "]/div/div/div/img").click()
            time.sleep(5)
            try:
                self.driver.find_element(*LearnHomePage.sub_embibe_explainers).is_displayed()
                time.sleep(5)
                self.driver.find_element(*LearnHomePage.sub_embibe_explainers).click()
                self.driver.find_element(*LearnHomePage.sub_embibe_explainers_tile).click()
                self.play_video_button()
                try:
                    self.driver.find_element(*LearnHomePage.more_topic).click()
                    time.sleep(3)
                    self.driver.find_element(*LearnHomePage.topic_video).click()
                    time.sleep(5)
                    self.play_video_button()
                    self.driver.back()
                except NoSuchElementException:
                    print("No Topic Videos Present")
                    self.driver.back()

                try:
                    self.driver.find_element(*LearnHomePage.related_video).click()
                    time.sleep(5)
                    self.driver.find_element(*LearnHomePage.topic_video).click()
                    time.sleep(5)
                    self.play_video_button()
                    self.driver.back()
                    time.sleep(2)
                    self.driver.back()
                except NoSuchElementException:
                    print("No related Videos Present")
                    self.driver.back()
                    self.driver.back()


            except NoSuchElementException:
                print("Embibe Explainers Carousel is not present")


    def sub_trending_videos_carousels(self):
        total_subject = self.driver.find_elements(*LearnHomePage.subject_buttons)
        count = len(total_subject)
        print(count)
        for i in range(2, count):
            self.driver.find_element(By.XPATH, "//div[@class='section subject-section']/div[2]/div/div/div[" + str(
                i) + "]").click()
            time.sleep(5)
            try:
                self.driver.find_element(*LearnHomePage.sub_trendingvideos).is_displayed()
                time.sleep(5)
                self.driver.find_element(*LearnHomePage.sub_trendingvideos_tile).click()
                self.play_video_button()
                try:
                    self.driver.find_element(*LearnHomePage.more_topic).click()
                    time.sleep(3)
                    self.driver.find_element(*LearnHomePage.topic_video).click()
                    time.sleep(5)
                    self.play_video_button()
                    self.driver.back()
                except NoSuchElementException:
                    print("No Topic Videos Present")
                    self.driver.back()

                # try:
                #     self.driver.find_element(*LearnHomePage.related_video).click()
                #     time.sleep(5)
                #     self.driver.find_element(*LearnHomePage.related_video_click).click()
                #     time.sleep(5)
                #     self.play_video_button()
                #     self.driver.back()
                #     time.sleep(2)
                #     self.driver.back()
                # except NoSuchElementException:
                #     print("No related Videos Present")
                #     self.driver.back()

            except NoSuchElementException:
                print("Trending Videos Carousel is not present")

    def sub_enrich_your_learning_carousels(self):
        total_subject = self.driver.find_elements(*LearnHomePage.subject_buttons)
        count = len(total_subject)
        for i in range(2, count + 1):
            self.driver.find_element(By.XPATH, "//div[@class='section subject-section']/div[2]/div/div/div[" + str(
                i) + "]").click()
            try:
                self.driver.find_element(*LearnHomePage.enrich_your_learning_carousel).is_displayed()
                time.sleep(5)
                # self.driver.find_element(*LearnHomePage.sub_embibe_explainers).click()
                self.driver.find_element(*LearnHomePage.sub_enrich_your_learning_tile).click()
                self.play_video_button()
                try:
                    self.driver.find_element(*LearnHomePage.more_topic).click()
                    time.sleep(3)
                    self.driver.find_element(*LearnHomePage.topic_video).click()
                    time.sleep(5)
                    self.play_video_button()
                    self.driver.back()
                except NoSuchElementException:
                    print("No Topic Videos Present")
                    self.driver.back()

            #     try:
            #         self.driver.find_element(*LearnHomePage.related_video).click()
            #         time.sleep(5)
            #         self.driver.find_element(*LearnHomePage.related_video_click).click()
            #         time.sleep(5)
            #         self.play_video_button()
            #         self.driver.back()
            #         self.driver.back()
            #     except NoSuchElementException:
            #         print("No related Videos Present")
            #         self.driver.back()
            #
            except NoSuchElementException:
                print("Enrich your Learning Carousel is not present")
        # self.driver.find_element(*LearnHomePage.last_subject_button).click()
        # try:
        #     self.driver.find_element(*LearnHomePage.sub_trendingvideos).is_displayed()
        #     time.sleep(5)
        #     # self.driver.find_element(*LearnHomePage.sub_embibe_explainers).click()
        #     self.driver.find_element(*LearnHomePage.sub_trendingvideos_tile).click()
        #     self.play_video_button()
        #     try:
        #         self.driver.find_element(*LearnHomePage.more_topic).click()
        #         time.sleep(3)
        #         self.driver.find_element(*LearnHomePage.topic_video).click()
        #         time.sleep(5)
        #         self.play_video_button()
        #         self.driver.back()
        #     except NoSuchElementException:
        #         print("No Topic Videos Present")
        #         self.driver.back()
        #
        #     try:
        #         self.driver.find_element(*LearnHomePage.related_video).click()
        #         time.sleep(5)
        #         self.driver.find_element(*LearnHomePage.related_video_click).click()
        #         time.sleep(5)
        #         self.play_video_button()
        #         self.driver.back()
        #         self.driver.back()
        #     except NoSuchElementException:
        #         print("No related Videos Present")
        #         self.driver.back()
        #
        # except NoSuchElementException:
        #     print("Trending Carousel is not present")

    def sub_books_with_videos_and_solutions(self):
        total_subject = self.driver.find_elements(*LearnHomePage.subject_buttons)
        count = len(total_subject)
        for i in range(2, count + 1):
            self.driver.find_element(By.XPATH, "//div[@class='section subject-section']/div[2]/div/div/div[" + str(
                i) + "]").click()
            try:
                self.driver.find_element(*LearnHomePage.author_books).is_displayed()
                time.sleep(5)
                # self.driver.find_element(*LearnHomePage.sub_embibe_explainers).click()
                self.driver.find_element(*LearnHomePage.sub_author_books).click()
                self.driver.find_element(*LearnHomePage.book_video_tile).click()
                try:
                    self.driver.find_element(*LearnHomePage.embibe_big_book).is_displayed()
                    time.sleep(5)
                    # self.driver.find_element(*LearnHomePage.sub_embibe_explainers).click()
                    self.driver.find_element(*LearnHomePage.sub_embibe_big_book).click()
                    self.driver.find_element(*LearnHomePage.book_video_tile).click()
                    try:
                        popup = self.driver.find_element(By.XPATH, "//*[text()='Continue from where you left?']")
                        if popup.is_displayed():
                            time.sleep(2)
                            self.driver.find_element(By.XPATH, "//*[text()='Yes']").click()
                            time.sleep(5)
                            self.driver.find_element(*LearnHomePage.learn_button).send_keys(keys.Keys.ESCAPE)
                            self.driver.find_element(*LearnHomePage.learn_button).send_keys(keys.Keys.ESCAPE)
                            time.sleep(5)
                    except NoSuchElementException:
                        time.sleep(5)
                        self.driver.find_element(*LearnHomePage.learn_button).send_keys(keys.Keys.ESCAPE)
                        self.driver.find_element(*LearnHomePage.learn_button).send_keys(keys.Keys.ESCAPE)
                        time.sleep(5)

                except ElementClickInterceptedException:
                    time.sleep(5)
                    self.driver.find_element(*LearnHomePage.learn_button).send_keys(keys.Keys.ESCAPE)
                    self.driver.find_element(*LearnHomePage.learn_button).send_keys(keys.Keys.ESCAPE)
            except NoSuchElementException:
                print("No Books with videos and solutions")

    def sub_embibe_big_books(self):
        total_subject = self.driver.find_elements(*LearnHomePage.subject_buttons)
        count = len(total_subject)
        for i in range(2, count + 1):
            self.driver.find_element(By.XPATH, "//div[@class='section subject-section']/div[2]/div/div/div[" + str(
                i) + "]").click()
            try:
                self.driver.find_element(*LearnHomePage.embibe_big_book).is_displayed()
                time.sleep(5)
                # self.driver.find_element(*LearnHomePage.sub_embibe_explainers).click()
                self.driver.find_element(*LearnHomePage.sub_embibe_big_book).click()
                self.driver.find_element(*LearnHomePage.book_video_tile).click()
                try:
                    popup = self.driver.find_element(By.XPATH, "//*[text()='Continue from where you left?']")
                    if popup.is_displayed():
                        time.sleep(2)
                        self.driver.find_element(By.XPATH, "//*[text()='Yes']").click()
                        time.sleep(5)
                        self.driver.find_element(*LearnHomePage.learn_button).send_keys(keys.Keys.ESCAPE)
                        self.driver.find_element(*LearnHomePage.learn_button).send_keys(keys.Keys.ESCAPE)
                        time.sleep(5)
                except NoSuchElementException:
                    time.sleep(5)
                    self.driver.find_element(*LearnHomePage.learn_button).send_keys(keys.Keys.ESCAPE)
                    self.driver.find_element(*LearnHomePage.learn_button).send_keys(keys.Keys.ESCAPE)
                    time.sleep(5)

            except ElementClickInterceptedException:
                time.sleep(5)
                self.driver.find_element(*LearnHomePage.learn_button).send_keys(keys.Keys.ESCAPE)
                self.driver.find_element(*LearnHomePage.learn_button).send_keys(keys.Keys.ESCAPE)

    def bookmark_video(self):
        self.driver.find_element(*LearnHomePage.trending_videos).click()
        self.handle_bookmark()
        self.driver.back()
        self.driver.find_element(*LearnHomePage.sub_embibe_explainers_tile).click()
        self.handle_bookmark()

    def handle_bookmark(self):
        ele = self.driver.find_element(*LearnHomePage.bookmark_button).text
        print(ele)
        if ele == "Bookmark":
            time.sleep(3)
            self.driver.find_element(*LearnHomePage.bookmark_button).click()
        else:
            print("Video is already bookmarked")

    def play_video_button(self):

        self.driver.find_element(*LearnHomePage.learn_button).click()
        time.sleep(3)
        try:
            popup = self.driver.find_element(By.XPATH, "//*[text()='Continue from where you left?']")
            if popup.is_displayed():
                time.sleep(2)
                self.driver.find_element(By.XPATH, "//*[text()='Yes']").click()
                time.sleep(5)
                self.driver.find_element(*LearnHomePage.learn_button).send_keys(keys.Keys.ESCAPE)
                time.sleep(2)
                self.driver.find_element(*LearnHomePage.learn_button).send_keys(keys.Keys.ESCAPE)
                time.sleep(5)
        except NoSuchElementException:
            time.sleep(5)
            self.driver.find_element(*LearnHomePage.learn_button).send_keys(keys.Keys.ESCAPE)
            time.sleep(2)
            self.driver.find_element(*LearnHomePage.learn_button).send_keys(keys.Keys.ESCAPE)
            time.sleep(5)

        except ElementClickInterceptedException:
            time.sleep(5)
            self.driver.find_element(*LearnHomePage.learn_button).send_keys(keys.Keys.ESCAPE)
            time.sleep(5)
            # self.driver.find_element(*LearnHomePage.learn_button).send_keys(keys.Keys.ESCAPE)
            self.driver.find_element(By.XPATH, "//*[text()='Close']").click()
