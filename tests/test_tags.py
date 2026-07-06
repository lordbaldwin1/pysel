from pages.tags_page import TagsPage


def test_initial_page_content(tags_page: TagsPage):
  tags_page.open()
  heading_text = tags_page.get_heading_text()
  assert heading_text == "Tags"

  subtext_text = tags_page.get_subtext_text()
  assert "Press enter or add" in subtext_text

  remaining_text = tags_page.get_remaining_text()
  assert "8 tags" in remaining_text

  remove_all_button = tags_page.get_remove_all_button()
  assert remove_all_button.text == "Remove All"

  expected_initial_tags = ["node", "javascript"]
  tags_text_list = tags_page.get_tags_text()
  assert is_list_subset(tags_text_list, expected_initial_tags)

def test_remove_all_tags(tags_page: TagsPage):
  tags_page.open()
  tags_page.remove_all_tags()
  
  list_item_count = tags_page.get_list_item_count()
  assert list_item_count == 0

def test_add_tags(tags_page: TagsPage):
  tags_page.open()

  expected_tags = ["node", "javascript", "test1", "test2", "test3"]
  tags_to_add = "test1,test2,test3"

  tags_page.input_tags(tags_to_add)
  actual_tags = tags_page.get_tags_text()
  assert is_list_subset(actual_tags, expected_tags)

def test_add_and_remove_tags(tags_page: TagsPage):
  tags_page.open()

  expected_tags = ["javascript", "test2"]
  tags_to_add = "test1,test2,test3"
  tags_to_remove = ["node", "test1", "test3"]

  tags_page.input_tags(tags_to_add)
  tags_page.remove_tags_by_text(tags_to_remove)
  
  actual_tags = tags_page.get_tags_text()
  assert actual_tags == expected_tags

def is_list_subset(sub, main):
  for item in sub:
    if item not in main:
      return False
  return True