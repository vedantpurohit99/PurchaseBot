from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import sys

ADIDAS_BASE = 'https://www.adidas.ca/en/'

def genURL(name, model, size):
    query = f'forceSelSize={model}_{int(530 + (float(size) - 4) * 20)}'
    return f'{ADIDAS_BASE}{name}/{model}.html?{query}'

if __name__ == '__main__':
    name = sys.argv[1]
    model = sys.argv[2]
    size = sys.argv[3]

    url = genURL(name, model, size)

    # ADD ITEM TO BAG
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get(url)
    cookie_close = driver.find_element_by_xpath("//button[@data-auto-id='glass-cookie-consent-close-button']")
    cookie_close.click()
    add_button = driver.find_element_by_xpath("//button[@title='Add To Bag']")
    add_button.click()