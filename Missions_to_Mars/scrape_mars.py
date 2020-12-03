from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests
#from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def init_browser():
    #Create path to my chrome driver
    executable_path = {'executable_path': "C:\\Users\\juliasqueri\\.wdm\\drivers\\chromedriver"}
    return Browser('chrome', **executable_path, headless=False)

mars_dict = {}

def scrape():
    #NASA Mars News
    browser = init_browser()

    url = 'https://mars.nasa.gov/news'
    browser.visit(url)

    soup = bs(browser.html, 'html.parser')

    all_titles = soup.find_all(name='div', class_='content_title')
    news_title = all_titles[1].text.strip()

    all_paragraph = soup.find_all(name='div', class_='article_teaser_body')
    news_p = all_paragraph[0].text.strip()

    mars_dict['news_title']= news_title
    mars_dict['news_p']= news_p
    #mars_dict.append(news_title)
    #mars_dict.append(news_p)

    return mars_dict

print(mars_dict)