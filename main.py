from selenium import webdriver
from selenium.webdriver.common.by import By

# make configuration of driver
driver = webdriver.Chrome(executable_path="/root/script/Automation/chromedriver")


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
