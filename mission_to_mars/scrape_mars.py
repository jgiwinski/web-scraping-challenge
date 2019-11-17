#Imports & Dependencies
import pandas as pd
import time  
from splinter import Browser
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import lxml
import requests




def init_browser():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=True)

def news():
    url     = "https://mars.nasa.gov/news/"
    browser = init_browser()

    browser.visit(url)

    html            = browser.html
    soup            = bs(html, "html.parser")
    newest_title    = soup.find_all("div", class_="content_title")[0].text
    newest_teaser   = soup.find_all("div", class_="article_teaser_body")[0].text
    output          = [newest_title, newest_teaser]

    return output


def image(): 
    images_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    image_url  = "https://www.jpl.nasa.gov"
    browser    = init_browser()

    browser.visit(images_url)

    html = browser.html
    soup = bs(html, "html.parser")

    image_end           = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]
    
    featured_image_url  = image_url + image_end

    return featured_image_url

def weather():  
    tweet_url = 'https://twitter.com/marswxreport?lang=en'
    browser   = init_browser()

    browser.visit(tweet_url)

    html = browser.html
    soup = bs(html, "html.parser")
    
    mars_weather = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text  

    return mars_weather

def facts():  
    facts_url = "https://space-facts.com/mars/"
    browser   = init_browser()
    
    mars_df         = pd.read_html(facts_url)
    mars_df         = pd.DataFrame(mars_df[0])
    mars_df.columns = ["Parameter", "Values"]

    table_object    = mars_df.to_html(classes="table table-striped")
    table_object    = table_object.replace('\n', '')
    table_object
     
    return table_object

def hem(): 
    hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser         = init_browser()

    browser.visit(hemispheres_url)
    
    html            = browser.html
    soup            = bs(html, "html.parser")
    mars_hemisphere = []
    products        = soup.find("div", class_ = "result-list" )
    hemispheres     = products.find_all("div", class_="item")

    for hemisphere in hemispheres:
        title       = hemisphere.find("h3").text
        title       = title.replace("Enhanced", "")
        end_link    = hemisphere.find("a")["href"]
        image_link  = "https://astrogeology.usgs.gov/" + end_link    
        browser.visit(image_link)
        html        = browser.html
        soup        = bs(html, "html.parser")
        downloads   = soup.find("div", class_="downloads")
        image_url   = downloads.find("a")["href"]
        dictionary  = {"title": title, "img_url": image_url}

        mars_hemisphere.append(dictionary)

    return mars_hemisphere

def scrape():

    final_data = { 
        "mars_news" : news()[0], 
        "mars_paragraph" : news()[1], 
        "mars_image" : image(), 
        "mars_weather" : weather(),
        "mars_facts" : facts(), 
        "mars_hemisphere" : hem()
        } 
    return final_data