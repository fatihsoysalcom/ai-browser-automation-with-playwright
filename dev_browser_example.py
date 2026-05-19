from playwright.sync_api import sync_playwright

def run_ai_agent_task():
    # Initialize Playwright for Chromium browser
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False) # Set headless=False to see the browser actions
        page = browser.new_page()

        try:
            # Navigate to a sample website
            page.goto("https://www.example.com")
            print("Navigated to example.com")

            # AI Agent Action: Find and interact with an element
            # In a real AI agent, this would be determined by its logic
            # Here, we simulate finding a link and clicking it
            link_selector = "a"
            page.locator(link_selector).click()
            print(f"Clicked on the first link: {link_selector}")

            # AI Agent Action: Extract information from the page
            # Simulate extracting the page title
            page_title = page.title()
            print(f"Current page title: {page_title}")

            # Simulate filling a form (if the page had one)
            # For example.com, there isn't a form, so we'll skip this.
            # If there was an input field with id='myInput':
            # page.fill("#myInput", "AI generated text")
            # print("Simulated filling an input field.")

            # AI Agent Action: Wait for a specific condition (e.g., new content loaded)
            # page.wait_for_selector("#newContent")
            # print("Waited for new content.")

            # Keep the browser open for a few seconds to observe
            page.wait_for_timeout(5000) # Wait for 5 seconds

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            browser.close()
            print("Browser closed.")

if __name__ == "__main__":
    run_ai_agent_task()
