#Imports & Dependencies
import pandas as pd
import time  
from bs4 import BeautifulSoup as bs
from splinter import Browser


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)