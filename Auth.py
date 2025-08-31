from selene import browser, have, be
from selene.support.shared import config
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def test_success_login():

    config.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    config.timeout = 20


from selene import browser, have, be
from selene.support.shared import config


def test_success_login():
    config.browser_name = 'chrome'
    config.timeout = 20
try:
        browser.open(
            'http://10.5.121.74/login?redirectTo=/commercialControl/billingStatements')
        browser.element('[id="normal_login_username"]').should(be.visible).type('predbill')
        browser.element('[id="normal_login_password"]').type('predbill')
        browser.element('.ant-btn.ant-btn-primary.w-100.mb-s').click()
        browser.element('.ant-menu-title-content').should(have.text('Коммерческий учет'))
        print("Тест пройден: успешный вход.")
    except Exception as e:
        print(f"Ошибка при выполнении теста: {e}")
        browser.save_screenshot('error_screenshot.png')
    finally:
        browser.quit()

