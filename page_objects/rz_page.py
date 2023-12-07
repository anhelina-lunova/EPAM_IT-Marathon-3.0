from playwright.sync_api import Playwright


class RZPage:
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()

        self.page = self.context.new_page()
        self.page.goto("https://bt.rozetka.com.ua/ua/washing_machines/c80124/")

    def check_grid_len(self):
        return len(self.page.query_selector("//rz-grid/ul").query_selector_all('xpath=child::*'))

    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()
