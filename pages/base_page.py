from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from config import BASE_URL

class BasePage:
  def __init__(self, driver, timeout=10):
    self.driver = driver
    self.wait = WebDriverWait(driver, timeout)

  def goto(self, url):
    self.driver.get(BASE_URL + url)

  def wait_for_visible(self, locator):
    return self.wait.until(expected_conditions.visibility_of_element_located(locator))

  def wait_for_clickable(self, locator):
    return self.wait.until(expected_conditions.element_to_be_clickable(locator))

  def wait_for_selected(self, locator):
    return self.wait.until(expected_conditions.element_to_be_selected(locator))

  def wait_for_text(self, locator, text):
    return self.wait.until(expected_conditions.text_to_be_present_in_element((locator, text)))

  def wait_for_visibility_of_all_elements(self, locator):
    return self.wait.until(expected_conditions.visibility_of_all_elements_located(locator))

    