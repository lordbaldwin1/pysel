from datetime import datetime
from pathlib import Path
from _pytest.pytester import pytest_plugins
import pytest
from selenium import webdriver

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

pytest_plugins = [
    "fixtures.fixtures"
]

SCREENSHOT_DIR = Path("screenshots")


def pytest_sessionstart(session):
    if SCREENSHOT_DIR.exists():
        for path in SCREENSHOT_DIR.glob("*.png"):
            path.unlink()
    else:
        SCREENSHOT_DIR.mkdir(exist_ok=True)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)

@pytest.fixture(autouse=True)
def screenshot_on_failure(request, driver):
    yield
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        SCREENSHOT_DIR.mkdir(exist_ok=True)
        path = SCREENSHOT_DIR / f"{request.node.name}_{datetime.now():%Y%m%d_%H%M%S}.png"
        driver.save_screenshot(str(path))
        print(f"\nScreenshot saved: {path}")

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        choices=["chrome", "firefox"],
        help="Browser to run tests with",
    )
    parser.addoption(
        "--size",
        action="store",
        default="1440x900",
        help="Browser window size as WIDTHxHEIGHT, e.g. 1440x900",
    )
    parser.addoption(
        "--headed",
        action="store_true",
        help="Run with a visible browser window instead of headless",
    )


def parse_size(size_str):
    try:
        width, height = size_str.lower().split("x")
        return int(width), int(height)
    except ValueError:
        raise pytest.UsageError(
            f"Invalid --size value: {size_str}. Expected format WIDTHxHEIGHT, e.g. 1440x900"
        )


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    width, height = parse_size(request.config.getoption("--size"))
    headed = request.config.getoption("--headed")

    if browser == "chrome":
        options = ChromeOptions()
        if not headed:
            options.add_argument("--headless=new")
        options.add_argument(f"--window-size={width},{height}")

        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options,
        )

    elif browser == "firefox":
        options = FirefoxOptions()
        if not headed:
            options.add_argument("-headless")

        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options,
        )
        driver.set_window_size(width, height)

    else:
        raise pytest.UsageError(f"Unsupported browser: {browser}")

    yield driver
    driver.quit()