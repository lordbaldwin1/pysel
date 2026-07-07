from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DropdownPage(BasePage):
  OPEN_DROPDOWN_BUTTON = (By.CSS_SELECTOR, ".navbar-nav > li:last-child")
  DROPDOWN = (By.CLASS_NAME, "dropdown")
  MENU_ITEMS = (By.CSS_SELECTOR, ".menu-item")

  def open(self):
    self.goto("multi-level-dropdown")

  def open_nav_dropdown(self):
    open_button = self.wait_for_clickable(self.OPEN_DROPDOWN_BUTTON)
    open_button.click()

  def get_dropdown_menu_items_href_and_text(self):
    menu = self.wait_for_visible(self.DROPDOWN)

    items = menu.find_elements(By.CSS_SELECTOR, ".menu-item")
    res = []
    for item in items:
      href = item.get_attribute("href")
      if not href:
        raise ValueError(f"href missing for menu item: {item.text}")
      text = item.text
      res.append((href, text))
    return res

  def open_dropdown_submenu_by_text(self, text: str):
    menu = self.wait_for_visible(self.DROPDOWN)
    item = menu.find_element(By.XPATH, f".//a[contains(., '{text}')]")
    item.click()
    self.wait_for_menu_animation_complete()

  def wait_for_menu_animation_complete(self):
    def _condition(driver):
      div = driver.find_element(By.CSS_SELECTOR, ".dropdown > div")
      attribute = div.get_attribute("class")
      return "menu-primary-exit-active" not in attribute
    self.wait.until(_condition)

  