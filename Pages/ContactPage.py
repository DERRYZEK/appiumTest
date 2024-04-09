from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By


class ContactPage:

    def __init__(self, driver):
        self.driver = driver

    newContactButton = (AppiumBy.ACCESSIBILITY_ID, "Create new contact")
    firstName = (By.XPATH, "//*[@text='First name']")
    lastName = (By.XPATH, "//*[@text='Last name']")
    phoneNumber = (By.XPATH, "//*[@text='Phone']")
    saveContact = (By.ID, "com.android.contacts:id/editor_menu_save_button")

    def getNewContactButton(self):
        return self.driver.find_element(*ContactPage.newContactButton)

    def getFirstName(self):
        return self.driver.find_element(*ContactPage.firstName)

    def getLastName(self):
        return self.driver.find_element(*ContactPage.lastName)

    def getPhoneNumber(self):
        return self.driver.find_element(*ContactPage.phoneNumber)

    def getSaveContact(self):
        return self.driver.find_element(*ContactPage.saveContact)
