from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
driver.get("https://www.accuweather.com/en/us/austin-tx/78701/hourly-weather-forecast/351193")
for a in soup.findAll('a',href=True, attrs={'class':'accordion-item hourly-forecast-card hour'}):
    print(a)

