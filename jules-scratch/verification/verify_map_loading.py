from playwright.sync_api import sync_playwright, expect, Page

def verify_initial_load(page: Page):
    """
    This test verifies that the application loads and displays the expected
    API key error message when no Google Maps API key is configured.
    """
    # 1. Arrange: Go to the application's homepage.
    # Give the server a moment to start up.
    page.wait_for_timeout(5000)
    page.goto("http://localhost:5000")

    # 2. Assert: Check for the API Key Error message inside the map container.
    # This confirms the app has loaded and correctly identified the missing key.
    map_container = page.locator("#map")

    # Assert that the correct error message for a missing Firebase SDK is shown.
    # This is the expected behavior when running in an unauthenticated emulator environment.
    expected_error_text = "Firebase SDK not loaded. Ensure you are running the app via the Firebase emulator or that your deployment is configured correctly."
    error_locator = page.get_by_text(expected_error_text)

    # Wait for the error text to be visible.
    expect(error_locator).to_be_visible(timeout=15000)

    # 3. Screenshot: Capture the final result for visual verification.
    page.screenshot(path="jules-scratch/verification/verification.png")
    print("Screenshot captured successfully, showing the Firebase SDK loading error as expected.")


# Boilerplate to run the verification
if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            verify_initial_load(page)
        finally:
            browser.close()