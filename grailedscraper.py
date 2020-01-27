from selenium import webdriver
import math
import time
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as BS

driver = webdriver.Chrome(options=webdriver.ChromeOptions())
driver.get("https://www.grailed.com/shop/Cy4WNVYvDg")

assert "Grailed" in driver.title

# click somewhere that won't execute anything to bring up the sign-in box
unclickable_h2= driver.find_element_by_xpath('//*[@id="shop"]/div/div/div[3]/div[2]/h2')
unclickable_h2.click()

# we must close the "Create an Account" button that prompts with signing in
close_button = driver.find_element_by_xpath('/html/body/div[53]/div/div/a')
close_button.click()

time.sleep(1)

# many times scrolling is required, so we will have to figure out how many "scrolls" are needed
num_items = driver.find_element_by_xpath('//*[@id="shop"]/div/div/div[1]/div[1]/div/span').get_attribute("innerHTML")
num_items = int(num_items.split(" ")[0].replace(",", ""))

scrolls = math.ceil(num_items/40)

# scroll 
for i in range(0, scrolls):
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
	time.sleep(1) 

# get the list of items 
items = driver.find_elements_by_xpath('//div[@class="feed-item"]')

# loop through list of items and store href
item_url_list = []
for item in items:
	item_url_list.append(item.find_element_by_xpath('./a').get_attribute('href'))

# we can close the driver now
driver.close()

# now we switch over to requests and BS



url = "https://www.grailed.com/shop/HbG3Y7fy6A"

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

webpage_html = BS(webpage, "html.parser")

items = webpage_html.findAll("div", {"class":"feed-item"})

