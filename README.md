# pysel

Selenium test automation for [QA Playground](https://qaplayground.dev/apps/) using pytest and the page object model.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Copy `.env` and set `BASE_URL` if needed. It defaults to `https://qaplayground.dev/apps/`.

## Run tests

```bash
pytest
```

Options:

- `--browser chrome|firefox` (default: chrome)
- `--headed` to show the browser window
- `--size 1440x900` to set window size

Failed tests save screenshots to `screenshots/`.
