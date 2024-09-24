import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService, Service
from selenium.webdriver.chrome.options import Options

###POM implementation
#Add the parent directory
from login_orange_page import OrangeLoginPage

@pytest.fixture()
def browser():

    chromedriver_path = r"E:\Automation testing\chromedriver.exe"
    chrome_options = Options()
    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver

####Test case ID:TC_login_01
def test_orange_page(browser):
    orange_login_page = OrangeLoginPage(browser)
    browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Perform login actions
    orange_login_page.enter_username("Admin")
    orange_login_page.enter_password("admin123")
    orange_login_page.click_login_submit()

###Test case ID:TC_login_02
def test_orange_page(browser):
    orange_login_page = OrangeLoginPage(browser)
    browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    orange_login_page.enter_username("Admin")
    orange_login_page.enter_password("invalid password")
    #try & exception handling
    try:
        orange_login_page.click_login_submit()
    except:
        print("Invalid Credential")

###Test case ID:TC_PIM_01
def test_orange_page(browser):
    login_orange_page = OrangeLoginPage(browser)
    browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    login_orange_page.enter_username("Admin")
    login_orange_page.enter_password("admin123")
    login_orange_page.click_login_submit()
    login_orange_page.click_pim()
    login_orange_page.click_add()
    login_orange_page.enter_firstname("Bhavani")
    login_orange_page.enter_middlename("Kannan")
    login_orange_page.enter_lastname("K")
    login_orange_page.enter_employeeid("236")
    login_orange_page.click_save()
###Test case ID:TC_PIM_02
    login_orange_page.click_pim()
    login_orange_page.click_edit()
    login_orange_page.enter_otherid("XX23656")
    login_orange_page.enter_drivelicense("236gb45")
    login_orange_page.click_gender()
    login_orange_page.click_save2()
###Test case ID:TC_PIM_03
    login_orange_page.click_pim()
    login_orange_page.click_delete()
    login_orange_page.click_popup_link()

