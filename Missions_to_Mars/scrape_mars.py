from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def init_browser():
    #Create path to my chrome driver
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)


def scrape():

    #NASA Mars News
    browser = init_browser()
    
    #NOTE:If error occurs that "list index is out of range", try adding '/' to the end of this url here and in jupyter. For some reason, this URL keeps changing what is required

    url = 'https://mars.nasa.gov/news'
    browser.visit(url)

    soup = bs(browser.html, 'html.parser')

    all_titles = soup.find_all(name='div', class_='content_title')
    news_title = all_titles[1].text.strip()

    all_paragraph = soup.find_all(name='div', class_='article_teaser_body')
    news_p = all_paragraph[0].text.strip()

    #Featured Image
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    soup = bs(browser.html, 'html.parser')

    img_url = soup.find('article', class_='carousel_item')['style'].replace('background-image: url(','').replace(');','')[1:-1]

    main_url = 'https://www.jpl.nasa.gov'

    featured_image_url = (main_url + img_url)
    
    #Mars Facts
    url = 'https://space-facts.com/mars/'
    browser.visit(url)

    tables = pd.read_html(url)
    df = tables[0]
    df = df.set_index(0)
    df = df.rename(columns={0:"Description", 1: "Value"})

    mars_df = df.to_html(classes= 'dataframe')

    #Mars Hemispheres

    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    soup = bs(browser.html, 'html.parser')

    items = soup.find_all(name='div', class_='item')

    hempishere_image_urls = []

    main_url = 'https://astrogeology.usgs.gov'

    #Create loop
    for i in items:
        hem_dict = {}
        #Get titles
        title = i.find('h3').text
    
        #Get partial img url from main page
        partial_img_url = i.find('a', class_='itemLink product-item')['href']
    
        #Go to link that has the full image
        browser.visit(main_url + partial_img_url)
    
        #Create new soup
        soup = bs(browser.html, 'html.parser')
    
        #Get full image source
        img_url = main_url + soup.find('img', class_='wide-image')['src']

        hem_dict = {
        "titles": title,
        "img_url": img_url
        }
    
        #Append the img names and links to a list of dicts
        hempishere_image_urls.append(hem_dict)


    mars_dict = {
        'news_title': news_title,
        'news_p': news_p,
        'featured_image': featured_image_url,
        'mars_facts': mars_df,
        'hempishere_image_urls': hempishere_image_urls
    }

    browser.quit()
    
    return mars_dict
