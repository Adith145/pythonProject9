from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given(u'launch the chrome browser')
def step_impl(self):
    self.driver = webdriver.Chrome(r"C:\seleniumwebdriver\chromedriver.exe")
    self.driver.get("https://www.amazon.in")
    self.driver.implicitly_wait(40)
    self.driver.maximize_window()
    # screenshot
    self.driver.get_screenshot_as_file(r"C:\Users\Admin\OneDrive\Desktop\screenschot\homepage.png")
    time.sleep(3)


@when(u'search the mobile less than 30000 oneplus mobile')
def step_impl(self):
    self.driver.find_element(by=By.XPATH, value=" //input[@id='twotabsearchtextbox']").send_keys(
        "oneplus Mobile under 30000")
    # screenshot
    self.driver.save_screenshot(r"C:\Users\Admin\OneDrive\Desktop\screenschot\homepage1.png")

    self.driver.find_element(by=By.XPATH, value=" //input[@id='nav-search-submit-button']").click()
    # screenshot
    self.driver.save_screenshot(r"C:\Users\Admin\OneDrive\Desktop\screenschot\homepage2.png")


@when(u'click on sort by option and select newest arrivals search')
def step_impl(self):
    self.driver.find_element(by=By.XPATH, value=" //span[contains(text(),'Featured')]").click()
    time.sleep(5)
    self.driver.find_element(by=By.XPATH, value=" //a[@id='s-result-sort-select_4']").click()

    # screenshot
    self.driver.save_screenshot(r"C:\Users\Admin\OneDrive\Desktop\screenschot\homepage3.png")

    time.sleep(5)
    self.driver.execute_script("alert('search successfully');")
    time.sleep(4)

    self.driver.switch_to.alert.dismiss()

    self.driver.refresh()
    time.sleep(8)


@then(u'i will redirect to home page verify the title')
def step_impl(self):
    self.driver.close()
