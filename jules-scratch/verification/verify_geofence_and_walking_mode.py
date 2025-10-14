import re
from playwright.sync_api import Page, expect

def test_geofence_and_walking_mode(page: Page):
    print("Starting test...")
    # Go to the local development server
    page.goto("http://127.0.0.1:5002")
    print("Navigated to page.")

    # Wait for the app to load and company modal to appear
    expect(page.locator("#company-modal")).to_be_visible(timeout=30000)
    print("Company modal is visible.")

    # Join a company
    page.get_by_text("Join").first.click()
    print("Clicked 'Join' button.")

    # Wait for the main UI to appear
    expect(page.locator("#dispatch-ui")).to_be_visible(timeout=30000)
    print("Dispatch UI is visible.")

    # Verify Walking Mode UI
    walking_mode_button = page.locator("#walking-mode-btn")
    expect(walking_mode_button).to_be_visible()
    print("Walking mode button is visible.")
    walking_mode_button.click()
    print("Clicked walking mode button.")

    expect(page.locator("#trail-creation-panel")).to_be_visible()
    print("Trail creation panel is visible.")
    expect(page.locator("#saved-trails-panel")).to_be_visible()
    print("Saved trails panel is visible.")

    page.screenshot(path="jules-scratch/verification/walking_mode.png")
    print("Took walking mode screenshot.")

    # Exit walking mode
    walking_mode_button.click()
    print("Clicked walking mode button again.")

    # Verify Geofence UI
    expect(page.locator("#geofence-panel")).to_be_visible()
    print("Geofence panel is visible.")
    create_geofence_button = page.locator("#create-geofence-btn")
    expect(create_geofence_button).to_be_visible()
    print("Create geofence button is visible.")

    create_geofence_button.click()
    print("Clicked create geofence button.")

    expect(page.locator("#geofence-modal")).to_be_visible()
    print("Geofence modal is visible.")

    page.screenshot(path="jules-scratch/verification/geofence.png")
    print("Took geofence screenshot.")
    print("Test finished.")