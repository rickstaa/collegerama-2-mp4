"""A small python script I used to download videos from collegerama so
I could watch them off-line.
"""

# Import Modules
import webbrowser
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup

# Get user input
print('-- Get lecture script --')
url_lec = input('Give url: ')

# Get rendered HTML
driver = webdriver.Chrome("/home/username/ChromeDriver/chrome‌​driver")
driver.set_window_position(-10000,0)
driver.get(url_lec)
sleep(4)
html = driver.page_source
driver.quit()

# Extract values with beautifulsoup
soup = BeautifulSoup(html, "html.parser")
print('')
print("The video stream urls are:")
url = []
for tags in soup.find_all('video'):
  url.append(tags.source['src'])
  print("-", tags.source['src'])

# Download video
webbrowser.open_new_tab(url[0])
webbrowser.open_new_tab(url[1])
