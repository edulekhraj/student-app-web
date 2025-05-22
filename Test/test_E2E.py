import time

import pytest

from PageObject.achieve_page import achievehomepage
from PageObject.goal_exam import GoalExamPage
from PageObject.learn_home_page import LearnHomePage
from PageObject.monetisation import EmbibeMonetisation
from PageObject.practice_home_page import PracticeHomePage
from PageObject.search_page import SearchPage
from PageObject.signUp_signIn import signIn_up
from PageObject.test_home_page import TestHomePage
from PageObject.user_home import UserHome
from Utilities.utility import utility


class TestEmbibe(utility):

    @pytest.mark.usefixtures("setup", "log_on_failure")
    def test_sign_in_password(self):
        login = signIn_up(self.driver)
        login.test_sign_in_password()
        log = self.getLogger()
        log.info("Testcase: Sign in with Password")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    def test_signIn_mobile(self):
        log = self.getLogger()
        login = signIn_up(self.driver)
        login.sign_in_with_mobile()
        log.info("Testcase: Sign in with Mobile number")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.landingpage
    def test_signIn_email(self):
        log = self.getLogger()
        login = signIn_up(self.driver)
        login.sign_in_with_email()
        log.info("Testcase: Sign in with Email ID")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.landingpage
    def test_signIn_tos(self):
        log = self.getLogger()
        login = signIn_up(self.driver)
        login.terms_and_conditions()
        log.info("Testcase: User clicks on Terms and Conditions link in SignIn page")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.landingpage
    def test_signIn_privacy_policy(self):
        log = self.getLogger()
        login = signIn_up(self.driver)
        login.privacy_and_policy()
        log.info("Testcase: User clicks on Privacy Policy link in SignIn page")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.profile
    def test_goal_exam_en(self):
        log = self.getLogger()
        self.test_sign_in_password()
        gep = GoalExamPage(self.driver)
        gep.hero_banner_goal_exam_selection_eng()
        log.info("Test case : User Updates Goal & Exam")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.learn
    def test_same_exam_subject_button_is_present_in_LPT_Modules(self):
        log = self.getLogger()
        self.test_sign_in_password()
        learn = LearnHomePage(self.driver)
        learn.all_subject_tile_is_present_in_LPT()
        log.info("Testcase: Same Exam Subjects button is present in Learn,Practice, Test Module")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.learn
    def test_click_each_module_Tab_is_navigating_to_its_module(self):
        log = self.getLogger()
        self.test_sign_in_password()
        learn = LearnHomePage(self.driver)
        learn.click_each_module_Tab_is_navigation_to_module()
        log.info(
            "Testcase: User is redirected to relevant screen on clicking on Learn/Practice/Test/Achieve/UserHome Tab")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.learn
    def test_enrich_your_learning_carousel(self):
        log = self.getLogger()
        self.test_sign_in_password()
        learn = LearnHomePage(self.driver)
        learn.enrich_your_learning_carousels()
        log.info("Testcase: Verify Enrich Your Learning carousel is present and no issues in video player")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.learn
    def test_bookmark_videos(self):
        log = self.getLogger()
        self.test_sign_in_password()
        learn = LearnHomePage(self.driver)
        learn.bookmark_video()
        log.info("Testcase: Verify user is able to Bookmark the video")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.learn
    def test_learn_embibe_big_books(self):
        log = self.getLogger()
        self.test_sign_in_password()
        learn = LearnHomePage(self.driver)
        learn.learn_embibe_big_books()
        log.info("Testcase: Verify Embibe Big Books - <Subject> carousel is present and no issues in video player")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.learn
    def test_learn_select_chapter_topics_in_author_books(self):
        log = self.getLogger()
        self.test_sign_in_password()
        learn = LearnHomePage(self.driver)
        learn.learn_select_chapter_topics_in_author_books()
        log.info("Testcase: Verify User is able to select Chapters in the Author Books")
        log.info("Testcase: Verify User is able to select Topics in the Author Books")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.learn
    def test_learn_cheat_sheet_present_in_author_books(self):
        log = self.getLogger()
        self.test_sign_in_password()
        learn = LearnHomePage(self.driver)
        learn.learn_cheat_sheet_present_in_author_books()
        log.info("Testcase: Verify Cheat Sheet is present in the Author Books")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.xfail
    def test_sub_embibe_explainers_carousel(self):
        log = self.getLogger()
        self.test_sign_in_password()
        learn = LearnHomePage(self.driver)
        learn.sub_embibe_explainers_carousels()
        log.info(
            "Testcase: Verify Embibe Explainers carousel is present in Subject filter and no issues in video player")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.xfail
    def test_sub_trending_videos_carousel(self):
        log = self.getLogger()
        self.test_sign_in_password()
        learn = LearnHomePage(self.driver)
        learn.sub_trending_videos_carousels()
        log.info("Testcase: Verify Trending Videos carousel is present")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.xfail
    def test_sub_enrich_your_learning_carousel(self):
        log = self.getLogger()
        self.test_sign_in_password()
        learn = LearnHomePage(self.driver)
        learn.sub_enrich_your_learning_carousels()
        log.info("Testcase: Verify Enrich Your Learning In <Subject> carousel is present")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.xfail
    def test_sub_books_with_videos_and_solutions_carousel(self):
        log = self.getLogger()
        self.test_sign_in_password()
        learn = LearnHomePage(self.driver)
        learn.sub_books_with_videos_and_solutions()
        log.info("Testcase: Verify Books With Videos & Solutions - <Subject>")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.xfail
    def test_sub_learn_chapters(self):
        log = self.getLogger()
        self.test_sign_in_password()
        learn = LearnHomePage(self.driver)
        learn.sub_learn_chapter()
        log.info("Test case: Verify Learn <Subject> Chapters From <Class>")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.learn
    @pytest.mark.xfail
    def test_sub_big_books_carousel(self):
        log = self.getLogger()
        self.test_sign_in_password()
        learn = LearnHomePage(self.driver)
        learn.sub_embibe_big_books()
        log.info("Testcase: Verify Embibe Big Books - <Subject>")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.learn
    def test_learn_continue_learning(self):
        log = self.getLogger()
        log.info("Test case: Playing Videos present in the Continue Learning Carousel")
        self.test_sign_in_password()
        learn = LearnHomePage(self.driver)
        learn.learn_continue_learning()

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.learn
    def test_learn_trending_videos(self):
        self.test_sign_in_password()
        learn = LearnHomePage(self.driver)
        learn.learn_trending_videos()
        log = self.getLogger()
        log.info("Test case: Playing  Videos present in the Trending Videos")
        log.info(
            "Test case: Playing Videos present in the More Topic Carousel present inside Trending Videos details Page")
        log.info(
            "Test case: Playing Videos present in the Related Videos Carousel present inside Trending Videos details Page")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    def test_learn_embibe_explainers(self):
        self.test_sign_in_password()
        learn = LearnHomePage(self.driver)
        learn.learn_embibe_explainers()
        log = self.getLogger()
        log.info("Test case: Playing Videos present in the Embibe Explainers Carousel")
        log.info(
            "Test case: Playing Video present in the More Topics carousel present in Embibe Explainers details Page")
        log.info(
            "Test case: Playing Video present in the Related Videos carousel present in Embibe Explainers details Page")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.learn
    def test_learn_chapter(self):
        self.test_sign_in_password()
        learn = LearnHomePage(self.driver)
        learn.learn_learn_chapter()
        log = self.getLogger()
        log.info("Test case: Playing Video in the Continue Learning Carousel")
        log.info("Test case: Playing Video present in the All Videos carousel present in Learn Chapter Summary Page")
        log.info("Test case: Playing Video present in the Topic Videos carousel present in Learn Chapter Summary Page")
        log.info("Test case: Displaying Points to Remember  in Learn Chapter Summary Page")
        log.info("Test case: Playing Video present in the Prerequisite  carousel present in Learn Chapter Summary Page")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.learn
    def test_learn_chapter_test_taking(self):
        log = self.getLogger()
        self.test_sign_in_password()
        ttp = TestHomePage(self.driver)
        ttp.test_taking_in_learn_chapters()
        log.info("Testcase: Tests on this chapter (selected) option is present ")
        log.info("Testcase: Tests on this chapter (select from list) option is present")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.practice
    def test_learn_chapter_practice_taking(self):
        log = self.getLogger()
        self.test_sign_in_password()
        php = PracticeHomePage(self.driver)
        php.practice_taking_in_practice_chapter()
        log.info("Testcase : Practice on this chapter (selected) tile is present in Learn Chapter")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.practice
    def test_practicechapters(self):
        log = self.getLogger()
        self.test_sign_in_password()
        ph = PracticeHomePage(self.driver)
        log.info("Test case: Clicking on Practice Chapter in Practice Home")
        log.info("Test case: Practice Now Button is displayed in the Practice Summary")
        log.info("Test case: User is navigated to Practice Taking Screen on clicking on Practice Now button")
        ph.practice_chapters()
        log.info("Test case: User attempts 5 questions and view Learn Intervention screen")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.test
    def test_trending_test_embibe_exp_ui(self):
        log = self.getLogger()
        self.test_sign_in_password()
        ttp = TestHomePage(self.driver)
        ttp.trending_test_embibe_exp_ui()
        log.info("Test case: Click on Trending Test")
        log.info("Test case: Start Test Button is displayed in the Test Summary")
        log.info("Test case: User is navigated to Test Taking Screen on clicking on Start Test button")
        log.info("Test case: User submits the test after attempting all questions in the Test taking screen")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.test
    def test_full_test_embibe_exp_ui(self):
        log = self.getLogger()
        self.test_sign_in_password()
        ttp = TestHomePage(self.driver)
        ttp.full_test_embibe_exp_ui()
        log.info("Test case: Click on Full Test")
        log.info("Test case: Start Test Button is displayed in the Test Summary")
        log.info("Test case: User is navigated to Test Taking Screen on clicking on Start Test button")
        log.info("Test case: User submits the test after attempting all questions in the Test taking screen")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.test
    def test_chapter_test_embibe_exp_ui(self):
        log = self.getLogger()
        self.test_sign_in_password()
        ttp = TestHomePage(self.driver)
        ttp.chapter_test_embibe_exp_ui()
        log.info("Test case: Click on Chapter Test")
        log.info("Test case: Start Test Button is displayed in the Test Summary")
        log.info("Test case: User is navigated to Test Taking Screen on clicking on Start Test button")
        log.info("Test case: User submits the test after attempting all questions in the Test taking screen")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.test
    def test_recommended_practice_in_trending_test_summary(self):
        log = self.getLogger()
        self.test_sign_in_password()
        ttp = TestHomePage(self.driver)
        ttp.recommended_practice_in_trending_test_summary()
        log.info("Test case: User clicks on Recommended Practice in Full Test Summary")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.test
    def test_recommended_learn_videos_in_trending_test_summary(self):
        log = self.getLogger()
        self.test_sign_in_password()
        ttp = TestHomePage(self.driver)
        ttp.recommended_learn_video_in_trending_test_summary()
        log.info("Test case: User clicks on Recommended Video in Trending Test Summary")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.test
    def test_recommended_practice_in_chapter_test_summary(self):
        log = self.getLogger()
        self.test_sign_in_password()
        ttp = TestHomePage(self.driver)
        ttp.recommended_practice_in_chapter_test_summary()
        log.info("Test case: User clicks on Recommended Learn in Chapter Test Summary")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.test
    def test_recommended_learn_in_chapter_test_summary(self):
        log = self.getLogger()
        self.test_sign_in_password()
        ttp = TestHomePage(self.driver)
        ttp.recommended_learn_in_chapter_test_summary()
        log.info("Test case: User clicks on Recommended Video in Chapter Test Summary")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.test
    def test_recommended_practice_in_full_test_summary(self):
        log = self.getLogger()
        self.test_sign_in_password()
        ttp = TestHomePage(self.driver)
        ttp.recommended_practice_in_full_test_summary()
        log.info("Test case: User clicks on Recommended Practice in Full Test Summary")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.test
    def test_recommended_learn_in_full_test_summary(self):
        log = self.getLogger()
        self.test_sign_in_password()
        ttp = TestHomePage(self.driver)
        ttp.recommended_learn_in_full_test_summary()
        log.info("Test case: User clicks on Recommended Video in Full Test Summary")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.practice
    def test_practice_author_books(self):
        log = self.getLogger()
        self.test_sign_in_password()
        ph = PracticeHomePage(self.driver)
        ph.author_books()
        log.info("Test case: Click on the Author Books")
        log.info("Test case: Clicking on the Practice Tile present in the Book TOC")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.practice
    def test_practice_embibe_big_books(self):
        log = self.getLogger()
        self.test_sign_in_password()
        ph = PracticeHomePage(self.driver)
        ph.embibe_big_books()
        log.info("Test case: Click on the Big Books")
        log.info("Test case: Clicking on the Practice Tile present in the Book TOC")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.test
    def test_quick_5_mins_test(self):
        log = self.getLogger()
        self.test_sign_in_password()
        ttp = TestHomePage(self.driver)
        ttp.quick_5_mins_cyot()
        log.info("Test case: Create CYOT - 5 Mins Test")
        log.info("Test case: User is able to take CYOT - 5 Mins Test")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.test
    def test_CYOT(self):
        log = self.getLogger()
        self.test_sign_in_password()
        ttp = TestHomePage(self.driver)
        ttp.cyot()
        log.info("Test case: Create CYOT - Custom Test")
        log.info("Test case: User is able to take CYOT - Custom Test")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.search
    def test_search_videos(self):
        log = self.getLogger()
        self.test_sign_in_password()
        SP = SearchPage(self.driver)
        SP.search_videos_tabs()
        log.info("Test case : User searches for video in the search field")
        log.info("Test case : User watches the searched video")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.search
    def test_search_books(self):
        log = self.getLogger()
        self.test_sign_in_password()
        SP = SearchPage(self.driver)
        SP.search_books_tabs()
        log.info("Test case : User searches for Books in the search field")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.search
    def test_search_questions(self):
        log = self.getLogger()
        self.test_sign_in_password()
        SP = SearchPage(self.driver)
        SP.search_questions_tab()
        log.info("Test case : User searches for Question in the search field")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.search
    def test_search_practice(self):
        log = self.getLogger()
        self.test_sign_in_password()
        SP = SearchPage(self.driver)
        SP.search_practice_tab()
        log.info("Test case : User searches for Practice in the search field")
        log.info("Test case : User attempts the Searched Practice Topic")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.search
    def test_search_test(self):
        log = self.getLogger()
        self.test_sign_in_password()
        SP = SearchPage(self.driver)
        SP.search_test_tab()
        log.info("Test case : User searches for Test in the search field")
        log.info("Test case : User attempts the Searched Test Topic")

    # @pytest.mark.usefixtures("setup", "log_on_failure")
    # @pytest.mark.search
    # def test_search_questions(self):
    #     self.test_sign_in_password()
    #     SP = SearchPage(self.driver)
    #     SP.search_questions_tab()


    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.home
    def test_practice_in_revision_list(self):
        log = self.getLogger()
        self.test_sign_in_password()
        UH = UserHome(self.driver)
        UH.practice_in_revision_list()
        log.info("Test case: User selects practice present in Revision List")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.revision
    def test_videos_in_revision_list(self):
        log = self.getLogger()
        self.test_sign_in_password()
        UH = UserHome(self.driver)
        UH.learn_in_revision_list()
        log.info("Test case: User watch Learn video present in Revision List")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.home
    def test_watch_past_live_class(self):
        log = self.getLogger()
        self.test_sign_in_password()
        UH = UserHome(self.driver)
        UH.watch_past_live_class()
        log.info("Test case: User watches Past Live Class")

    # @pytest.mark.usefixtures("setup", "log_on_failure")
    # @pytest.mark.books
    # def test_add_favourite_books(self):
    #     log = self.getLogger()
    #     self.test_sign_in_password()
    #     UH = UserHome(self.driver)
    #     UH.add_favourite_book()
    #     log.info("Test case: User add's favourite books")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.home
    def test_play_bookmark_videos(self):
        log = self.getLogger()
        self.test_sign_in_password()
        UH = UserHome(self.driver)
        UH.play_bookmark_video()
        log.info("Test case: User watches Bookmarked Videos")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.home
    def test_practice_bookmark_questions(self):
        log = self.getLogger()
        self.test_sign_in_password()
        UH = UserHome(self.driver)
        UH.practice_bookmark_question()
        log.info("Test case: User practices Bookmarked Questions")



    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.profile
    def test_update_profile(self):
        log = self.getLogger()
        self.test_sign_in_password()
        gep = GoalExamPage(self.driver)
        gep.edit_profile()
        log.info("Test case : User Updates Profile Name")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.profile
    def test_update_avatar(self):
        log = self.getLogger()
        self.test_sign_in_password()
        gep = GoalExamPage(self.driver)
        gep.edit_avatar()
        log.info("Test case : User Updates Profile avatar")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.monetisation
    def test_achieve_now(self):
        log = self.getLogger()
        self.test_sign_in_password()
        monet = EmbibeMonetisation(self.driver)
        monet.achieve_now_plan()
        log.info("Test case: User is able to select Achieve Now Plan")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.monetisation
    def test_achieve_sprint(self):
        log = self.getLogger()
        self.test_sign_in_password()
        monet = EmbibeMonetisation(self.driver)
        monet.achieve_sprint_plan()
        log.info("Test case: User is able to select Achieve Sprint Plan")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.monetisation
    def test_achieve_unlimited(self):
        log = self.getLogger()
        self.test_sign_in_password()
        monet = EmbibeMonetisation(self.driver)
        monet.achieve_unlimited_plan()
        log.info("Test case: User is able to select Achieve Unlimited Plan")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.deeplink
    def test_click_lens_card_deeplink(self):
        log = self.getLogger()
        self.test_sign_in_password()
        monet = EmbibeMonetisation(self.driver)
        monet.click_lens_button()
        log.info("Test case: User clicks on Lens Card Deeplink button present in the Simple MonetisationPage")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.deeplink
    def test_click_live_class_card_deeplink(self):
        log = self.getLogger()
        self.test_sign_in_password()
        monet = EmbibeMonetisation(self.driver)
        monet.click_live_class_button()
        log.info("Test case: User clicks on Live Class Card Deeplink button present in the Simple MonetisationPage")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.deeplink
    def test_click_plantale_card_deeplink(self):
        log = self.getLogger()
        self.test_sign_in_password()
        monet = EmbibeMonetisation(self.driver)
        monet.click_plantale_button()
        log.info("Test case: User clicks on Plantale Card Deeplink button present in the Simple MonetisationPage")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.deeplink
    def test_click_brainApse_card_deeplink(self):
        log = self.getLogger()
        self.test_sign_in_password()
        monet = EmbibeMonetisation(self.driver)
        monet.click_brainapse_button()
        log.info("Test case: User clicks on BrainApse Card Deeplink button present in the Simple MonetisationPage")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.deeplink
    def test_click_froggipedia_card_deeplink(self):
        log = self.getLogger()
        self.test_sign_in_password()
        monet = EmbibeMonetisation(self.driver)
        monet.click_froggipedia_button()
        log.info("Test case: User clicks on Froggipedia Card Deeplink button present in the Simple Monetisation Page")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.deeplink
    def test_click_learn_card_deeplink(self):
        log = self.getLogger()
        self.test_sign_in_password()
        monet = EmbibeMonetisation(self.driver)
        monet.click_learn_button()
        log.info("Test case: User clicks on Learn Card Deeplink button present in the Simple MonetisationPage")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.deeplink
    def test_click_achieve_card_deeplink(self):
        log = self.getLogger()
        self.test_sign_in_password()
        monet = EmbibeMonetisation(self.driver)
        monet.click_achieve_button()
        log.info("Test case: User clicks on Achieve Card Deeplink button present in the Simple Monetisation Page")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.deeplink
    def test_click_practice_card_deeplink(self):
        log = self.getLogger()
        self.test_sign_in_password()
        monet = EmbibeMonetisation(self.driver)
        monet.click_practice_button()
        log.info("Test case: User clicks on Practice Card Deeplink button present in the Simple Monetisation Page")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.deeplink
    def test_click_test_card_deeplink(self):
        log = self.getLogger()
        self.test_sign_in_password()
        monet = EmbibeMonetisation(self.driver)
        monet.click_test_button()
        log.info("Test case: User clicks on Test Card Deeplink button present in the Simple Monetisation Page")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.deeplink
    def test_click_revision_list_card_deeplink(self):
        log = self.getLogger()
        self.test_sign_in_password()
        monet = EmbibeMonetisation(self.driver)
        monet.click_revision_list_button()
        log.info("Test case: User clicks on Revision List Card Deeplink button present in the Simple Monetisation Page")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.deeplink
    def test_parent_app_card_deeplink(self):
        log = self.getLogger()
        self.test_sign_in_password()
        monet = EmbibeMonetisation(self.driver)
        monet.click_parent_app_button()
        log.info("Test case: User clicks on Parent App Card Deeplink button present in the Simple Monetisation Page")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.deeplink
    def test_click_doubt_resolution_deeplink(self):
        log = self.getLogger()
        self.test_sign_in_password()
        monet = EmbibeMonetisation(self.driver)
        monet.click_doubt_resolution()
        log.info("Test case: User clicks on Doubt Resolution Card Deeplink button present in the Simple Monetisation Page")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.achieve
    def test_create_diagnostic_test(self):
        log = self.getLogger()
        self.test_sign_in_password()
        achieve = achievehomepage(self.driver)
        achieve.create_diagnostic_test()
        log.info("Test case: User creates Diagnostic Test")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.achieve
    def test_achieve_i_will_take_the_test_later(self):
        log = self.getLogger()
        self.test_sign_in_password()
        achieve = achievehomepage(self.driver)
        achieve.i_will_start_test_later()
        time.sleep(10)
        log.info("Test case: User clicks on 'I will start test later' button")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.achieve
    def test_attempt_diagnostic_test_1(self):
        log = self.getLogger()
        self.test_sign_in_password()
        achieve = achievehomepage(self.driver)
        achieve.start_diagnostic_test1()
        time.sleep(10)
        log.info("Test case: User attempts Diagnostic Test - 1")


    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.achieve
    def test_attempt_diagnostic_test_2(self):
        log = self.getLogger()
        self.test_sign_in_password()
        achieve = achievehomepage(self.driver)
        achieve.start_diagnostic_test2()
        time.sleep(10)
        log.info("Test case: User attempts Diagnostic Test - 2")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.achieve
    def test_create_PAJ_journey(self):
        log = self.getLogger()
        self.test_sign_in_password()
        achieve = achievehomepage(self.driver)
        achieve.create_PAJ_journey()
        log.info("Test case: User creates PAJ Journey")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.achieve
    def test_click_explore_mastery(self):
        log = self.getLogger()
        self.test_sign_in_password()
        achieve = achievehomepage(self.driver)
        achieve.explore_mastery_tile()

        log.info("Test case: User clicks on Explore Mastery")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.profile
    def test_profile_edit_goal_exam(self):
        log = self.getLogger()
        self.test_sign_in_password()
        gep = GoalExamPage(self.driver)
        gep.edit_goal_exam()
        log.info("Test case: Edit Goal from the Profile Screen")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    @pytest.mark.profile
    def test_goal_exam_hi(self):
        log = self.getLogger()
        self.test_sign_in_password()
        gep = GoalExamPage(self.driver)
        gep.hero_banner_goal_exam_selection_hin()
        log.info("Test case: User is able to select Hindi Language")







