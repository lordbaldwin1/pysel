from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class VerifyAccountPage(BasePage):
  HEADING = (By.ID, "title")
  HEADING_SUBTEXT = (By.ID, "msg")
  INFO = (By.CSS_SELECTOR, ".info:not(.success)")
  INFO_SUCCESS = (By.CSS_SELECTOR, ".info.success")
  CODE_INPUTS = (By.CLASS_NAME, "code")


  def open(self):
    self.goto("verify-account")

  def get_heading_text(self):
    header = self.wait_for_visible(self.HEADING)
    return header.text

  def get_heading_subtext_text(self):
    subtext = self.wait_for_visible(self.HEADING_SUBTEXT)
    return subtext.text

  def get_info_text(self):
    info = self.wait_for_visible(self.INFO)
    return info.text

  def get_info_success_text(self):
    info_success = self.wait_for_visible(self.INFO_SUCCESS)
    return info_success.text

  def get_code_inputs(self):
    inputs = self.wait_for_visibility_of_all_elements(self.CODE_INPUTS)
    return inputs

  def input_code(self, code: str):
    inputs = self.get_code_inputs()

    if len(inputs) != len(code):
      raise ValueError(
        f"Code length ({len(code)}) does not match number of inputs: ({len(inputs)})"
      )

    for i, input in enumerate(inputs):
      input.clear()
      input.send_keys(code[i])

  def parse_code_from_info(self):
    info_text = self.get_info_text()
    split = info_text.split(" ")[-1].split("-")
    code = "".join(split)
    if code.isdigit() == False:
      raise ValueError(
        f"Code is not valid: ({code})"
      )
    return code