from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from config import BASE_URL
from pages.base_page import BasePage


class DynamicTablePage(BasePage):

  TABLE_HEADERS = (By.CSS_SELECTOR, "thead > tr > th")
  TABLE_BODY = (By.ID, "tbody")
  HEADING_SUPERHERO = (By.XPATH, "//th[normalize-space()='Superhero']")


  def open(self):
    self.goto("dynamic-table")

  def get_table_headers(self):
    headers = self.wait_for_visibility_of_all_elements(self.TABLE_HEADERS)
    return [header.text for header in headers]

  def get_table_row_count(self):
    tbody = self.wait_for_visible(self.TABLE_BODY)
    rows = tbody.find_elements(By.CSS_SELECTOR, "tr")
    return len(rows)

  def find_row_by_superhero(self, name: str):
    tbody = self.wait_for_visible(self.TABLE_BODY)
    row = tbody.find_element(By.XPATH, f".//tr[contains(., '{name}')]")
    return row

  def get_real_name_text_by_superhero(self, name: str):
    row = self.find_row_by_superhero(name)
    cell = row.find_element(By.CSS_SELECTOR, "td:last-child")
    return cell.text

