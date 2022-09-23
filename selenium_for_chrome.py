import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def page_yandex(driver, ):
    try:
        driver.get("https://passport.yandex.ru/auth/list")

        time.sleep(5)

        email_input = driver.find_element_by_id("passp-field-login")
        email_input.clear()
        login = 'Alexander.Filippov79'
        email_input.send_keys(login)

        time.sleep(5)

        password_input = driver.find_element_by_id('passp-field-passwd')
        password_input.clear()
        password = 'Mashenka7771'
        password_input.send_keys(password)
        return True
    except Exception as ex:
        print(ex)
        return False
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    page_yandex(driver)