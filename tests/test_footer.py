import pytest
from playwright.sync_api import Page, expect


urls = [
    "https://only.digital/",
    "https://only.digital/projects",
    "https://only.digital/company",
]


@pytest.mark.parametrize("url", urls)
def test_footer_elements_present(page: Page, url: str):
    """
    Проверяет наличие футера и ключевых элементов на странице.
    """
    # Открываем страницу
    page.goto(url)
    
    # Находим элемент футера
    footer = page.locator("footer")
    
    # Проверяем, что футер видим
    expect(footer).to_be_visible()
    
    # Проверяем наличие текста "© 2014 - 2025"
    copyright_text = footer.get_by_text("© 2014 - 2025")
    expect(copyright_text).to_be_visible()
    
    # Проверяем наличие ссылки или текста "Политика конфиденциальности"
    privacy_policy = footer.get_by_text("Политика конфиденциальности")
    expect(privacy_policy).to_be_visible()
    

