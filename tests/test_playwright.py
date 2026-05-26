from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False,
        slow_mo=100
    )

    page = browser.new_page()
    page.goto("https://www.avito.ru")

    page.goto(
    "https://www.avito.ru",
    wait_until="domcontentloaded",
    timeout=60000
    )

    page.wait_for_timeout(3000)

    print("TITLE:", page.title())

    # Пример работы с элементом
    login_button = page.locator("text=Вход и регистрация")

    print("Login button visible:", login_button.is_visible())

    input("Press Enter to close...")

    browser.close()