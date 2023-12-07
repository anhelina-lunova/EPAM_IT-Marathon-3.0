from pytest import fixture
from playwright.sync_api import Playwright, sync_playwright, expect
from page_objects.rz_page import RZPage


@fixture
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture
def rz_wm_page(get_playwright):
    wmp = RZPage(get_playwright)
    yield wmp
    wmp.close()
