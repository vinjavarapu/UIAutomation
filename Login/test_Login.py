from selenium import webdriver
global webdriver
global driver


def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path="C:/UIAutomation/Drivers/chromedriver.exe")
    driver.get("https://accounts.staging.artemis.im/?origin=organizer")
    driver.implicitly_wait(10)
    driver.maximize_window()
def test_loginsite():
    driver.find_element_by_id("input-31").send_keys("vinjavarapu@gmail.com")
    driver.find_element_by_xpath('//*[@id="fawn-accounts"]/div/main/div/div/div[1]/div[2]/div/div[2]/div[5]/div[2]/button/span').click()
    driver.find_element_by_id("input-39").send_keys("Ravi@123")
    driver.find_element_by_xpath('//*[@id="fawn-accounts"]/div/main/div/div/div[1]/div[2]/div/div[2]/div[5]/div[2]/button[1]/span').click()
    driver.implicitly_wait(15)
def test_homepageTitle():
    print(driver.title)
    Homepage_title = driver.title
    assert Homepage_title == "Artemis Accounts Portal"
def test_teardown():
    driver.close()
    driver.quit()






