import random
import time

from Pages.ContactPage import ContactPage
from Utilities.BaseClass import BaseClass
from appium.webdriver.webdriver import Keyboard


class TestAddContact(BaseClass):
    def test_contact(self):
        log = self.getLogger()

        contactPage = ContactPage(self.driver)

        log.info("clicking on add new contact button")
        contactPage.getNewContactButton().click()

        log.info("Entering Contact's first name")
        contactPage.getFirstName().send_keys("Test" + str(random.randint(0, 999)))

        log.info("Entering Contact's last name")
        contactPage.getLastName().send_keys(str(random.randint(0, 999)) + "Test" + str(random.randint(0, 999)))

        self.driver.hide_keyboard()
        # self.driver.press_keycode(4)

        log.info("Entering phone number")
        contactPage.getPhoneNumber().send_keys("0244444444")

        log.info("Saving Contact")
        contactPage.getSaveContact().click()

        self.driver.get_screenshot_as_file("..//Reports//screen.png")
