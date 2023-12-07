from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()
    page.goto("https://bt.rozetka.com.ua/ua/washing_machines/c80124/")

    # Get the list of items from catalog_grid
    catalog_grid_len = len(page.query_selector("//rz-grid/ul").query_selector_all('xpath=child::*'))

    # Check if catalog_grid has at least one item
    # print(catalog_grid_len)
    assert (catalog_grid_len) >= 1

    # ---------------------
    page.close()
    context.close()
    browser.close()


def test_catalog_grid_has_elements():
    with sync_playwright() as playwright:
        run(playwright)