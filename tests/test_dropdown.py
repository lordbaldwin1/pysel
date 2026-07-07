from config import BASE_URL
from pages.dropdown_page import DropdownPage

MLD_URL = BASE_URL + "multi-level-dropdown/"

def test_dropdown_e2e(dropdown_page: DropdownPage):
  dropdown_page.open()
  dropdown_page.open_nav_dropdown()

  expected_level_1_items = [
    (MLD_URL + "#undefined", "My Profile"),
    (MLD_URL + "#settings", "Settings"),
    (MLD_URL + "#animals", "🦧\nAnimals"),
  ]
  actual_level_1_items = dropdown_page.get_dropdown_menu_items_href_and_text()
  assert actual_level_1_items == expected_level_1_items

  dropdown_page.open_dropdown_submenu_by_text("Settings")
  expected_settings_items = [
    (MLD_URL + "#main", "My Tutorial"),
    (MLD_URL + "#!HTML", "HTML"),
    (MLD_URL + "#!CSS", "CSS"),
    (MLD_URL + "#!JavaScript", "JavaScript"),
    (MLD_URL + "#!Awesome", "Awesome!"),
  ]
  actual_settings_items = dropdown_page.get_dropdown_menu_items_href_and_text()
  assert actual_settings_items == expected_settings_items