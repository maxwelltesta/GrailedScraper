from selenium import webdriver
import math
import time
import json
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as BS

def scraper(url):
	driver = webdriver.Chrome(options=webdriver.ChromeOptions())
	driver.get(url)

	assert "Grailed" in driver.title

	# click somewhere that won't execute anything to bring up the sign-in box
	unclickable_h2= driver.find_element_by_xpath('//*[@id="shop"]/div/div/div[3]/div[2]/h2')
	unclickable_h2.click()

	# we must close the "Create an Account" button that prompts with signing in
	close_button = driver.find_element_by_xpath('//a[@class="close"]')
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
	for item in item_url_list:
		item_url = item
		req = Request(item_url, headers={'User-Agent': 'Mozilla/5.0'})
		webpage = urlopen(req)
		webpage_html = webpage.read()
		webpage_soup = BS(webpage_html, "html.parser")
		webpage.close()

		# info stored in json, find all scripts, then get select the one in the correct index (4)
		scripts = webpage_soup.find_all('script')
		for each in scripts:
			if 'window.CURRENT_LISTING =' in each.text:
				data_script = each

		json_data = json.loads(data_script.get_text()[27:].strip().replace(";", ""))

		item_brand = json_data['designer_names']
		item_name = json_data['title']
		item_post_date = json_data['created_at']
		item_followers = json_data['follower_count']

		print(item_brand)
		print(item_name)
		print(item_post_date)
		print(item_followers)
		print('----------------------------------------------------------')

if __name__ == '__main__':
	url = input("Enter a feed url: ")
	scraper(url)






