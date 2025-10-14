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

        # Wait for the main UI to appear
        page.locator("#dispatch-ui, #driver-ui").first.wait_for(timeout=30000)
        print("Main UI is visible.")

        # Open the settings modal
        page.locator("#settings-btn").click()
        print("Clicked settings button.")
        page.locator("#settings-modal").wait_for()
        print("Settings modal is visible.")

        # Enter and save the API key
        page.locator("#google-maps-api-key-input").fill("TEST_API_KEY")
        print("Filled API key.")
        page.locator("#save-api-key-btn").click()
        print("Clicked save API key.")

        # Verify the key was saved to local storage
        api_key = page.evaluate("() => localStorage.getItem('googleMapsApiKey')")
        print(f"API key from local storage: {api_key}")
        assert api_key == "TEST_API_KEY"

        # Take a screenshot
        page.screenshot(path="jules-scratch/verification/api_key_modal.png")
        print("Took screenshot.")
        print("Test finished.")
    finally:
        browser.close()

with sync_playwright() as playwright:
    run(playwright)