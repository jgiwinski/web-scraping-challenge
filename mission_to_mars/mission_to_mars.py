#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import time  
from bs4 import BeautifulSoup as bs
from splinter import Browser


# In[2]:


get_ipython().system('which chromedriver')


# In[3]:


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# # NASA Mars News

# In[27]:


url = 'https://mars.nasa.gov/news/'
browser.visit(url) 
html = browser.html
soup = bs(html, "html.parser")


# In[30]:


article = soup.find("div", class_='list_text')
news_title = article.find("div", class_="content_title").text
news_p = article.find("div", class_ ="article_teaser_body").text
print(f" Title: {news_title}")
print(f" Article body: {news_p}")


# # JPL Mars Space Images - Featured Image

# In[6]:


image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(image_url)
html = browser.html
soup = bs(html, "html.parser")


# In[7]:


image = soup.find("img", class_="thumb")["src"]
featured_image_url = "https://www.jpl.nasa.gov" + image

featured_image_url


# # Mars Weather

# In[8]:


tweet_url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(tweet_url)
html = browser.html
soup = bs(html, "html.parser")


# In[9]:


mars_weather = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
print(mars_weather)


# # Mars Facts

# In[25]:


facts_url = "https://space-facts.com/mars/"
browser.visit(facts_url)
mars_df = pd.read_html(facts_url)
mars_df = pd.DataFrame(mars_df[0])
mars_df.columns = ["Parameter", "Values"]
mars_df


# In[24]:


mars_facts = mars_df.to_html(header = False, index = False)
print(mars_facts)


# # Mars Hemispheres

# In[22]:


hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(hemispheres_url)
html = browser.html
soup = bs(html, "html.parser")
mars_hemisphere = []

products = soup.find("div", class_ = "result-list" )
hemispheres = products.find_all("div", class_="item")

for hemisphere in hemispheres:
    title = hemisphere.find("h3").text
    title = title.replace("Enhanced", "")
    end_link = hemisphere.find("a")["href"]
    image_link = "https://astrogeology.usgs.gov/" + end_link    
    browser.visit(image_link)
    html = browser.html
    soup = bs(html, "html.parser")
    downloads = soup.find("div", class_="downloads")
    image_url = downloads.find("a")["href"]
    mars_hemisphere.append({"title": title, "img_url": image_url})
    
mars_hemisphere


# In[ ]:




