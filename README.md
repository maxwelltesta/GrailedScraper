# Grailed Scraper

Grailed is a website I have used for years at this point, but only on a surface level. I wanted to take a deep dive to see if I could discover some trends about listing prices, times, and more.

![Grailed page](https://i.imgur.com/JxZntzZ.png)

Some things to consider:

1. Grailed's item feed is located dynamically, which means we can't rely soley on Requests and BeautifulSoup to scrape and parse data. We will use a web driver like Selenium to carry out the physical loading of the page. 
2. Since it would be inefficient to load every item for each feed url, Grailed loads them dynamically. This means we have to determine how far to scroll down and subsequently scroll using our web driver. 
3. Although information like prices, age, and names can be found on the feed, more important information (to me) is found in the source code of the item pages. 













Used:
* Python (coding language)
* Selenium (web driver)
* Requests (http requests for BS)
* BeautifulSoup (data scraping and parsing)

*Disclaimer: this code is intended for recreational use only and is not meant to be distributed on a larger scale*
