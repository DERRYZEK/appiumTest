import allure
import pytest
from allure_commons.types import AttachmentType
from appium.options.android import UiAutomator2Options
from appium.options.common import AppiumOptions
from appium.webdriver.appium_service import AppiumService
from appium import webdriver


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="class")
def setup(request):
    global driver
    # Start the Appium server
    appium_service = AppiumService()
    appium_service.start()
    print(appium_service.is_running)
    print(appium_service.is_listening)

    # Create an instance of AppiumOptions
    appium_options = AppiumOptions()

    # Set the desired capabilities
    desired_capabilities = {
        "platformName": "Android",
        "appium:deviceName": "Derry",
        "appium:appPackage": "com.android.contacts",
        "appium:appActivity": ".activities.PeopleActivity",
        "appium:automationName": "UIAutomator2",
        "noReset": True
    }

    # Set the Appium server URL
    appium_url = 'http://localhost:4723'

    capabilities_options = appium_options.load_capabilities(desired_capabilities)
    # Start the Appium session
    driver = webdriver.Remote(appium_url, options=capabilities_options)

    driver.implicitly_wait(10)
    request.cls.driver = driver

    yield
    # Quit the session
    driver.quit()
    appium_service.stop()


@pytest.fixture()
def failure(request, setup):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
