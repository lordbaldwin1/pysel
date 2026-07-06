from pages.verify_account_page import VerifyAccountPage


def test_page_initial_state(verify_account_page: VerifyAccountPage):
  verify_account_page.open()

  header_text = verify_account_page.get_heading_text()
  assert header_text == "Verify Your Account"

  subtext_text = verify_account_page.get_heading_subtext_text()
  assert "We emailed you" in subtext_text

  info_text = verify_account_page.get_info_text()
  assert info_text == "The confirmation code is 9-9-9-9-9-9"

  inputs = verify_account_page.get_code_inputs()
  assert len(inputs) == 6

def test_successful_confirmation_code(verify_account_page: VerifyAccountPage):
  verify_account_page.open()
  code = verify_account_page.parse_code_from_info()
  verify_account_page.input_code(code)
  success_text = verify_account_page.get_info_success_text()
  assert "Success" in success_text

def test_unsuccessful_confirmation_code(verify_account_page: VerifyAccountPage):
  wrong_code = "123456"
  verify_account_page.open()
  verify_account_page.input_code(wrong_code)
  assert "confirmation code" in verify_account_page.get_info_text()
