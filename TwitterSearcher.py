from selenium import webdriver
from bs4 import BeautifulSoup

driver_path = "C:\\Users\\Muhammd\\Desktop\\geckodriver.exe"
#webdriver.ChromeOptions.binary_location  = driver_path
browser = webdriver.Firefox(executable_path= driver_path)
#https://twitter.com/<twitter acount pseudoname>
browser.get("https://twitter.com/AAAA")
soup = BeautifulSoup(browser.page_source, 'html.parser')
tweets = [p.text for p in soup.findAll('p', class_ = 'tweet-text')]
words = tweets.splice(' ')
for i in words:
	print(i)
