import inspect
import logging
import time

import pytest
#from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@pytest.mark.flaky(reruns=3)
@pytest.mark.usefixtures("failure", "setup")
class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        current_time = time.strftime("%Y-%m-%d")

        fileHandler = logging.FileHandler('..\\Logs\\logfile' + current_time + '.log')
        formatter = logging.Formatter("%(asctime)s - %(filename)s:%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)

        logger.setLevel(logging.DEBUG)
        return logger

    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    @staticmethod
    def scrollToTextByAndroidUIAutomator(self, driver, text):
        # Scroll to an element using text as a reference

        element = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, (
            "new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector("
            ").textContains(\"{}\"))".format(
                text)))
        element.click()

    @staticmethod
    def swipeUp(self, howManySwipes, driver):
        for i in range(0, howManySwipes):
            driver.swipe(514, 600, 514, 200, 1000)

    @staticmethod
    def swipeDown(self, howManySwipes, driver):
        for i in range(0, howManySwipes):
            driver.swipe(514, 200, 514, 600, 1000)

    @staticmethod
    def swipeLeft(self, howManySwipes, driver):
        for i in range(0, howManySwipes):
            driver.swipe(900, 600, 200, 600, 1000)

    @staticmethod
    def swipeRight(self, howManySwipes, driver):
        for i in range(0, howManySwipes):
            driver.swipe(200, 600, 900, 600, 1000)
