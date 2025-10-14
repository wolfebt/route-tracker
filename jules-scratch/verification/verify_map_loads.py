from playwright.sync_api import Page, expect

def test_map_loads_correctly(page: Page):
    """
    This test verifies that the main map element loads after the application starts.
    """
    # 1. Arrange: Go to the application's homepage.
    page.goto("http://localhost:5000")

    # 2. Assert: Wait for the map container to be visible and not show "Loading Map...".
    map_container = page.locator("#map")

    # Wait for the initial "Loading Map..." text to disappear.
    expect(map_container.get_by_text("Loading Map...")).to_have_count(0, timeout=15000)

    # Check that the map container has some content rendered by Google Maps,
    # for example, the div that holds the map tiles.
    # A simple check is to see if the container has any child elements.
    expect(map_container.locator("div")).to_be_visible()

    # 3. Screenshot: Capture the final result for visual verification.
    page.screenshot(path="jules-scratch/verification/verification.png")