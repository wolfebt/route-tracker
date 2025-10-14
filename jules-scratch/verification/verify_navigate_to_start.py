import re
from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    try:
        print("Starting test...")
        # Go to the local development server
        page.goto("http://127.0.0.1:5002")
        print("Navigated to page.")

        # Check if the company modal is visible
        if page.locator("#company-modal").is_visible():
            print("Company modal is visible.")
            # Join a company
            page.get_by_text("Join").first.click()
            print("Clicked 'Join' button.")

        # Wait for the main UI to appear
        page.locator("#driver-ui").wait_for(timeout=30000)
        print("Driver UI is visible.")

        # The rest of the test is not possible from the driver view
        print("Test finished.")
    finally:
        browser.close()

with sync_playwright() as playwright:
    run(playwright)