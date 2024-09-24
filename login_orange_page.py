from selenium.webdriver.common.by import By


class OrangeLoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.XPATH, '//input[@placeholder="Username"]')
        self.password_input = (By.XPATH, '//input[@placeholder="Password"]')
        self.login_submit = (By.XPATH, '//button[@type="submit"]')

        self.pim = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span')
        self.add = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button')
        self.firstname_input = (By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input')
        self.middlename_input = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input')
        self.lastname_input = (By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input')
        self.employeeid_input = (By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input')
        self.save = (By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]')

        self.edit = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[1]/i')
        self.otherid_input = (By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input')
        self.drivelicense_input = (By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input')
        self.gender = (By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/label')
        self.save2 = (By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button')

        self.delete = (By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[2]/i')
        self.popup_link = (By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]')

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login_submit(self):
        self.driver.find_element(*self.login_submit).click()

    def click_pim(self):
        self.driver.find_element(*self.pim).click()

    def click_add(self):
        self.driver.find_element(*self.add).click()

    def enter_firstname(self, firstname):
        self.driver.find_element(*self.firstname_input).send_keys(firstname)

    def enter_middlename(self, middlename):
        self.driver.find_element(*self.middlename_input).send_keys(middlename)

    def enter_lastname(self, lastname):
        self.driver.find_element(*self.lastname_input).send_keys(lastname)

    def enter_employeeid(self, employeeid):
        self.driver.find_element(*self.employeeid_input).send_keys(employeeid)

    def click_save(self):
        self.driver.find_element(*self.save).click()

    def click_edit(self):
        self.driver.find_element(*self.edit).click()

    def enter_otherid(self, otherid):
        self.driver.find_element(*self.otherid_input).send_keys(otherid)

    def enter_drivelicense(self, drivelicense):
        self.driver.find_element(*self.drivelicense_input).send_keys(drivelicense)

    def click_gender(self):
        self.driver.find_element(*self.gender).click()

    def click_save2(self):
        self.driver.find_element(*self.save2).click()

    def click_delete(self):
        self.driver.find_element(*self.delete).click()

    def click_popup_link(self):
        self.driver.find_element(*self.popup_link).click()
