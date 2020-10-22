#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies and Setup
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd


# In[2]:


# Set Executable Path & Initialize Chrome Browser
executable_path = {"executable_path": "./chromedriver.exe"}
browser = Browser("chrome", **executable_path)


# In[3]:


# Visit the NASA Mars News Site
url = "https://mars.nasa.gov/news/"
browser.visit(url)


# In[7]:


# Use splinter to navigate the site and find the image url for the current Featured Mars Image 
#and assign the url string to a variable called featured_image_url.
featured_image_url = {"executable_path": "./chromedriver.exe"}
browser = Browser("chrome", **executable_path)
url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url)

featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg'


# In[8]:


#MARS FACTS
# Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
mars_df = pd.read_html("https://space-facts.com/mars/")[0]
print(mars_df)
mars_df.columns=["Description", "Value"]
mars_df.set_index("Description", inplace=True)
mars_df


# In[16]:


# Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.
executable_path = {"executable_path": "./chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)
url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url)


# In[17]:


hemisphere_image_urls = []

# Get a List of All the Hemispheres
links = browser.find_by_css("a.product-item h3")
for item in range(len(links)):
    hemisphere = {}
    
    # Find Element on Each Loop to Avoid a Stale Element Exception
    browser.find_by_css("a.product-item h3")[item].click()
    
    # Find Sample Image Anchor Tag & Extract <href>
    sample_element = browser.find_link_by_text("Sample").first
    hemisphere["img_url"] = sample_element["href"]
    
    # Get Hemisphere Title
    hemisphere["title"] = browser.find_by_css("h2.title").text
    
    # Append Hemisphere Object to List
    hemisphere_image_urls.append(hemisphere)
    
    # Navigate Backwards
    browser.back()


# In[18]:


hemisphere_image_urls


# In[ ]:




