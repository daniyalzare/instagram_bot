from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class Bot:
    def __int__(self, username, password, driver):
        self.driver = webdriver.Chrome()
        self.username = username
        self.password = password

    def Login(self):
        driver = webdriver.Chrome()
        driver.get('http://instagram.com/')
        waits = WebDriverWait(driver, 20)
        user = waits.until(EC.element_to_be_clickable((By.XPATH, '//input[@name="username"]'))).send_keys(username)
        pas = waits.until(EC.element_to_be_clickable((By.XPATH, '//input[@aria-label="Password"]'))).send_keys(password)
        login = waits.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))).click()
        notnow = waits.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="_a9-- _a9_0"]'))).click()
        story = waits.until(EC.element_to_be_clickable((By.XPATH, '//img[@crossorigin="anonymous"]'))).click()

    def Comment(self):
        driver = self.driver
        driver.get('https://www.instagram.com/juventus/')
        post = driver.find_element(By.CSS_SELECTOR, '/p/CBUalen0ib/').click()
        i = 1
        while i <= 5:
            waits = WebDriverWait(driver, 20)
            text = waits.until(EC.element_to_be_clickable((By.CLASS_NAME, 'Ypffh')))
            text.click()
            text = waits.until(EC.element_to_be_clickable((By.CLASS_NAME, 'Ypffh')))
            text.send_keys('Hello friends'+Keys.ENTER)
            time.time(3)
            next = driver.find_element(By.LINK_TEXT, 'Next').click()
            i += 1
        driver.get('https://www.instagram.com/juventus/')

    def Follower(self):
        driver = self.driver
        driver.get('https://www.instagram.com/juventus/')
        waits = WebDriverWait(driver, 20)
        flw = waits.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/juventus/followers/"]')))
        flw.click()
        time.time(3)
        for i in range(1,7):
            follow = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]/ul/div/li[{}]/div/div[2]/button'.format(i))
            follow.click()
            time.time(5)

username = "instagram username"
password = "instagram password"
test = Bot()
test.Login()
test.comment()
test.Follower()