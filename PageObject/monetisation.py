import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import Utilities
from Utilities.utility import utility


class EmbibeMonetisation:
    achieve_sprint = (By.XPATH, '//div[@order=1]/div[4]')

    achieve_unlimited = (By.XPATH, '//div[@order=2]/div[4]')
    achieve_now = (By.XPATH, '//div[@order=3]/div[4]')
    achieve_now_card_price = (By.XPATH, "//div[@order=3]/div[2]/div/span[2]")
    checkout_price = (By.XPATH, "//tr[@class='final-row']/td[2]")

    try_live_class = (By.XPATH, "//*[text()='Try Recorded Class']")
    try_lens = (By.XPATH, "//*[text()='Try Lens']")
    try_plantale = (By.XPATH, "//*[@type ='PLANTALE_AR_APP']/div[2]/button")
    try_brainapse = (By.XPATH, "//*[@type ='BRAINAPSE_AR_APP']/div[2]/button")
    try_froggipedia = (By.XPATH, "//*[@type ='FROGGIPEDIA_AR_APP']/div[2]/button")
    try_learn = (By.XPATH, "//*[@type ='LEARN']/div[2]/button")
    try_achieve = (By.XPATH, "//*[@type ='ACHIEVE']/div[2]/button")
    try_practice = (By.XPATH, "//*[@type ='PRACTICE']/div[2]/button")
    try_revision_list = (By.XPATH, "//*[@type ='REVISION_LIST']/div[2]/button")
    try_test = (By.XPATH, "//*[@type ='TEST']/div[2]/button")
    try_doubt_resolution = (By.XPATH, "//*[@type ='DOUBT_RESOLUTION']/div[2]/button")
    try_parent_app = (By.XPATH, "//*[@type ='PARENT']/div[2]/button")
    checkout_proceed_pay = (By.XPATH, "//span[text()='Proceed to pay']")
    razor_pay = (By.XPATH, "//span[@class='price-label svelte-1milfy7']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @staticmethod
    def clean_price(price):
        return float(price.replace('₹', '').replace(',', '').strip())

    def wait_for_visibility(self, locator):
        """Wait until an element is visible and return it."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator):
        """Wait until an element is clickable and return it."""
        return self.wait.until(EC.element_to_be_clickable(locator))

    url = utility.readConfig('Prod', 'monetisation_url')

    def achieve_now_plan(self):
        time.sleep(3)
        self.driver.get(self.url)
        # Click the "Achieve Now" button
        time.sleep(5)
        self.wait_for_clickable(EmbibeMonetisation.achieve_now).click()
        time.sleep(5)
        # Wait for checkout price and validate
        checkout_price = self.wait_for_visibility(EmbibeMonetisation.checkout_price).text
        # Proceed to payment
        self.wait_for_clickable(EmbibeMonetisation.checkout_proceed_pay).click()
        time.sleep(5)

        # Validate Razorpay price
        self.driver.switch_to.frame(self.wait_for_visibility((By.XPATH, "//iframe[contains(@src, 'razorpay')]")))
        razor_pay_price = self.wait_for_visibility(EmbibeMonetisation.razor_pay).text
        razor_pay_price_numeric = self.clean_price(razor_pay_price)
        checkout_price_numeric = self.clean_price(checkout_price)
        # Assertion
        assert razor_pay_price_numeric == checkout_price_numeric, "Checkout price mismatch in Razorpay"

    def achieve_sprint_plan(self):
        time.sleep(3)
        self.driver.get(self.url)
        time.sleep(5)

        # Click the "Achieve Now" button
        self.wait_for_clickable(EmbibeMonetisation.achieve_sprint).click()
        time.sleep(5)
        # Wait for checkout price and validate
        checkout_price = self.wait_for_visibility(EmbibeMonetisation.checkout_price).text
        # Proceed to payment
        self.wait_for_clickable(EmbibeMonetisation.checkout_proceed_pay).click()
        time.sleep(5)

        # Validate Razorpay price
        self.driver.switch_to.frame(self.wait_for_visibility((By.XPATH, "//iframe[contains(@src, 'razorpay')]")))
        razor_pay_price = self.wait_for_visibility(EmbibeMonetisation.razor_pay).text
        razor_pay_price_numeric = self.clean_price(razor_pay_price)
        checkout_price_numeric = self.clean_price(checkout_price)
        # Assertion
        assert razor_pay_price_numeric == checkout_price_numeric, "Checkout price mismatch in Razorpay"

    def achieve_unlimited_plan(self):
        time.sleep(3)
        self.driver.get(self.url)
        time.sleep(5)

        # Click the "Achieve Now" button
        self.wait_for_clickable(EmbibeMonetisation.achieve_unlimited).click()
        time.sleep(5)
        # Wait for checkout price and validate
        checkout_price = self.wait_for_visibility(EmbibeMonetisation.checkout_price).text
        time.sleep(5)
        # Proceed to payment
        self.wait_for_clickable(EmbibeMonetisation.checkout_proceed_pay).click()
        time.sleep(5)

        # Validate Razorpay price
        self.driver.switch_to.frame(self.wait_for_visibility((By.XPATH, "//iframe[contains(@src, 'razorpay')]")))
        razor_pay_price = self.wait_for_visibility(EmbibeMonetisation.razor_pay).text
        razor_pay_price_numeric = self.clean_price(razor_pay_price)
        checkout_price_numeric = self.clean_price(checkout_price)
        # Assertion
        assert razor_pay_price_numeric == checkout_price_numeric, "Checkout price mismatch in Razorpay"

    def click_live_class_button(self):
        time.sleep(3)
        self.driver.get(self.url)
        self.wait_for_visibility(EmbibeMonetisation.try_live_class).click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        self.wait_for_visibility((By.ID, 'embibe-live-classes')).is_displayed()

    def click_lens_button(self):
        self.driver.get(self.url)
        self.wait_for_visibility(EmbibeMonetisation.try_lens).click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        # self.wait_for_visibility((By.XPATH, "//*[contains(@src,'/EmbibeLens/embiLens.png')]")).is_displayed()

    def click_plantale_button(self):
        self.driver.get(self.url)
        self.wait_for_visibility(EmbibeMonetisation.try_plantale).click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        # self.wait_for_visibility((By.XPATH, "//div[@id='content-container']/div[1]")).is_displayed()

        #

    def click_brainapse_button(self):
        self.driver.get(self.url)
        self.wait_for_visibility(EmbibeMonetisation.try_brainapse).click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        # self.wait_for_visibility((By.XPATH, "//div[@id='content-container']/div[1]")).is_displayed()

    def click_froggipedia_button(self):
        self.driver.get(self.url)
        self.wait_for_visibility(EmbibeMonetisation.try_froggipedia).click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        # self.wait_for_visibility((By.XPATH, "//div[@id='content-container']/div[1]")).is_displayed()

    def click_learn_button(self):
        self.driver.get(self.url)
        self.driver.find_element(*EmbibeMonetisation.try_learn).click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        self.wait_for_visibility((By.XPATH,
                                  "//button[contains(@class,'eds-btn eds-btn--primary eds-btn--capsular eds-btn--md')]")).is_displayed()

    def click_achieve_button(self):
        self.driver.get(self.url)
        self.driver.find_element(*EmbibeMonetisation.try_achieve).click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        self.wait_for_visibility((By.XPATH, "//a[@href='/achieve/landing']")).is_displayed()

    def click_practice_button(self):
        self.driver.get(self.url)
        self.driver.find_element(*EmbibeMonetisation.try_practice).click()
        # windows = self.driver.window_handles

    def click_test_button(self):
        self.driver.get(self.url)
        self.driver.find_element(*EmbibeMonetisation.try_test).click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        assert self.driver.current_url == 'https://www.embibe.com/test/home'
        # self.wait_for_visibility((By.XPATH, "//button[@class='eds-btn eds-btn--primary eds-btn--capsular eds-btn--md']")).is_displayed()

    def click_revision_list_button(self):
        self.driver.get(self.url)
        self.driver.find_element(*EmbibeMonetisation.try_revision_list).click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        self.wait_for_visibility((By.XPATH, "//span[text()='Questions To Revise']")).is_displayed()

    def click_parent_app_button(self):
        self.driver.get(self.url)
        self.driver.find_element(*EmbibeMonetisation.try_parent_app).click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        # self.wait_for_visibility((By.XPATH, "//div[@class='download-btn-section ev_down_btn']/a[1]")).is_displayed()

    def click_doubt_resolution(self):
        self.driver.get(self.url)
        self.driver.find_element(*EmbibeMonetisation.try_doubt_resolution).click()
        time.sleep(3)
