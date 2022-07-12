from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# make configuration of driver
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("headless")
s = Service(executable_path="chromedriver")
driver = webdriver.Chrome(service=s, options=options)


def main():
    try:
        driver.get('https://inboxdata.top/pay/link.txt')
        # get url from script
        url = driver.find_element(By.TAG_NAME, value='pre').get_attribute("textContent")
        driver.get(url=url)
        driver.implicitly_wait(10)
        # click on button
        driver.find_element(By.CLASS_NAME, value='p-l-30').click()
        driver.implicitly_wait(10)
        # write to file new link from page
        with open('/var/www/inboxdata_to_usr/data/www/inboxdata.top/pay/url.txt', 'w') as file:
            file.write(driver.current_url)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    main()
