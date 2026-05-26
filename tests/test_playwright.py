from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False,
        slow_mo=100
    )

    page = browser.new_page()

    page.goto("https://www.avito.ru")

    print("TITLE:", page.title())
    print("URL:", page.url)

    input("Just observing...")

    browser.close()