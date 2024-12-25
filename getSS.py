from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def getSSfunc(driver, submission):
    url = "https://www.reddit.com{s}".format(s=submission.permalink)
    driver.get(url)
    titlepic = driver.find_element(By.XPATH, "/html/body/shreddit-app/div/div[1]/div/main/shreddit-post/h1")
    titleauthor = driver.find_element(By.XPATH,"/html/body/shreddit-app/div/div[1]/div/main/shreddit-post/div[1]")
    titlepic.screenshot('./screenshots/title_{s}.png'.format(s=submission.title[0:10]))
    titleauthor.screenshot('./screenshots/author_{s}.png'.format(s=submission.title[0:10]))