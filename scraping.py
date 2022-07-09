#!/usr/bin/env python
# coding: utf-8




#import splinter and beautiful soup

from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


#visit Mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
#optional delay for loading the page

browser.is_element_present_by_css('div.list_text', wait_time=1)


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


slide_elem.find('div', class_='content_title')


#use the parent element to find the first 'a' tag and save as 'news_title'

news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

article_teaser = slide_elem.find('div', class_='article_teaser_body').get_text()
article_teaser


# ### Featured Images

#visit url
url = 'https://spaceimages-mars.com'
browser.visit(url)


#find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


#parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df

df.to_html()

browser.quit()


# In[ ]:




