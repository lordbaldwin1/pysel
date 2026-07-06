from selenium.webdriver import Keys
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class TagsPage(BasePage):
  HEADING = (By.CLASS_NAME, "title")
  CONTENT_CONTAINER = (By.CLASS_NAME, "content")
  SUBTEXT = (By.XPATH, "//p[contains(., 'enter or add')]")
  REMAINING = (By.CLASS_NAME, "details")
  REMOVE_ALL_BUTTON = (By.XPATH, "//button[normalize-space()='Remove All']")
  TAGS_LIST = (By.CSS_SELECTOR, ".content > ul")
  TAGS_INPUT = (By.XPATH, "//input[@type='text' and @spellcheck='false']")

  def open(self):
    self.goto("tags-input-box")

  def get_heading_text(self):
    heading = self.wait_for_visible(self.HEADING)
    return heading.text

  def get_subtext_text(self):
    subtext = self.wait_for_visible(self.SUBTEXT)
    return subtext.text
  
  def get_remaining_text(self):
    remaining = self.wait_for_visible(self.REMAINING)
    return remaining.text

  def get_remove_all_button(self):
    button = self.wait_for_clickable(self.REMOVE_ALL_BUTTON)
    return button

  def get_tags_text(self):
    content = self.wait_for_visible(self.CONTENT_CONTAINER)
    tags = content.find_elements(By.CSS_SELECTOR, "ul > li")
    return [tag.text.strip() for tag in tags]

  def get_list_item_count(self):
    list = self.wait_for_visible(self.TAGS_LIST)
    list_items = list.find_elements(By.CSS_SELECTOR, "li")
    return len(list_items)

  def input_tags(self, text: str):
    input = self.wait_for_clickable(self.TAGS_INPUT)
    input.send_keys(text)
    input.send_keys(Keys.ENTER)

  def remove_tags_by_text(self, tags_to_remove: list[str]):
    tags_list = self.wait_for_visible(self.TAGS_LIST)
    for tag in tags_to_remove:
      list_item_delete_button = tags_list.find_element(By.XPATH, f"//li[normalize-space()='{tag}']/i")
      list_item_delete_button.click()

  def remove_all_tags(self):
    button = self.get_remove_all_button()
    button.click()