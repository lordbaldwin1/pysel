import pytest

from pages.dynamic_table_page import DynamicTablePage
from pages.verify_account_page import VerifyAccountPage

@pytest.fixture
def dynamic_table_page(driver) -> DynamicTablePage:
  page = DynamicTablePage(driver)
  return page

@pytest.fixture
def verify_account_page(driver) -> VerifyAccountPage:
  page = VerifyAccountPage(driver)
  return page