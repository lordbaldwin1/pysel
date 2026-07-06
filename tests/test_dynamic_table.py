import pytest
from pages.dynamic_table_page import DynamicTablePage


def test_table_header(dynamic_table_page: DynamicTablePage):
  dynamic_table_page.open()
  headers = dynamic_table_page.get_table_headers()
  assert headers == ["SUPERHERO", "STATUS", "REAL NAME"]
  assert len(headers) == 3

def test_table_row_count(dynamic_table_page: DynamicTablePage):
  dynamic_table_page.open()
  count = dynamic_table_page.get_table_row_count()
  assert count == 8

@pytest.mark.parametrize(
  "superhero, expected_real_name",
  [
    ("Spider-Man", "Peter Parker"),
    # ("Iron Man", "Anthony 'Tony' Stark"),
    # ("Deadpool", "Wade Wilson")
  ]
)
def test_superhero_real_names(
  dynamic_table_page: DynamicTablePage,
  superhero: str,
  expected_real_name: str,
):
  dynamic_table_page.open()
  actual = dynamic_table_page.get_real_name_text_by_superhero(superhero)
  assert actual == expected_real_name
