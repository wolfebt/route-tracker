from playwright.sync_api import sync_playwright, expect

def run_verification():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        try:
            # Go to the page. With no key in localStorage, it should show an error.
            page.goto("http://localhost:5000", timeout=60000)

            # Wait for the main loading overlay to disappear
            expect(page.locator("#loading-overlay")).to_be_hidden(timeout=60000)

            # Wait for the main application container to be visible.
            expect(page.locator("#app-container")).to_be_visible(timeout=30000)

            # Check that the map shows an API key error
            expect(page.locator("#map")).to_contain_text("API Key Error")
            expect(page.locator("#map")).to_contain_text("Please set your Google Maps API key in the settings menu")

            # Open the settings modal
            settings_button = page.locator("#settings-btn")
            expect(settings_button).to_be_visible()
            settings_button.click()

            # Wait for settings modal to be visible
            settings_modal = page.locator("#settings-modal")
            expect(settings_modal).to_be_visible()

            # Check for the correct Google Maps API Key input and label
            expect(settings_modal).to_contain_text("Google Maps API Key")
            google_maps_key_input = page.locator("#google-maps-api-key-input")
            expect(google_maps_key_input).to_be_visible()

            # Take screenshot showing the settings modal and the map error
            page.screenshot(path="jules-scratch/verification/verification.png")
            print("Screenshot taken successfully.")

        except Exception as e:
            print(f"An error occurred: {e}")
            page.screenshot(path="jules-scratch/verification/error.png")

        finally:
            context.close()
            browser.close()

if __name__ == "__main__":
    run_verification()