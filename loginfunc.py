from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def slow_typing(element, text):
    for character in text:
        element.send_keys(character)


def logIn(driver, username, password):
    try:
        sleep(2)
        username_in = driver.find_element(By.ID, "login-username")
        slow_typing(username_in, username)

        pass_in = driver.find_element(By.ID, "login-password")
        slow_typing(pass_in, password)

        pass_in.send_keys(Keys.ENTER)
        sleep(5)

    except NoSuchElementException:
        print("not logged in bruh")


def openLogin(driver, password, username):
    driver.get("https://www.reddit.com/")
    login = driver.find_element(By.LINK_TEXT, "Log In")
    login.click()

    logIn(driver, username, password)
