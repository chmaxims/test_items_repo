from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_visibility_of_basket(browser):
    browser.get(url)
    book = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.btn-add-to-basket')), message="Кнопка добавления в корзину отсутствует")

    assert book is not None




