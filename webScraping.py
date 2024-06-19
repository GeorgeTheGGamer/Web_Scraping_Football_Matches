import requests 
#download the html of a page 

standings_url = "https://fbref.com/en/comps/9/Premier-League-Stats"

data = requests.get(standings_url)
#download the page, use the get method in the requests library
#makes request to the server and downloads the html from the page 

data.text
#prints the html text from the data that we have 
#web browsers change this into graph elements
#look at the page and find out what is wanted from the page 
#to parse the html is to use the inspector, like the source code

#parsing html links with beautiful soup

from bs4 import BeautifulSoup
#Very useful library for parsing in html links 

soup = BeautifulSoup(data.text)
#initialise soup class and the using the beatiful soup fuction parse in our html data 
#Object is called soup
#Next thing to do is to give our soup object something to select from the web page

#On the site, all of the information is under the stats table class so now using cod we can bring in the html

standings_table = soup.select('table.stats_table')[0]
#this is a css selector, you tyoe name of the tag then . then class name 
#only want the first one so choose 0

# print(standings_table)
#this prints the removed extra html and really narrows down to what we are looking at 

links = standings_table.find_all('a')
#Using findall instead of select, select using css selectors and find all only finds tags
#want to get the href property of each link
#The href attribute specifies the URL of the page the link goes to

#Make a list comprehension, remember from haskell
links = [l.get("href") for l in links]
#Now have the href for every links

#Now filter the links 
links = [l for l in links if '/squads/' in l]
#Another list comprehension
#this says if swuad is in the link if isnt then get rid of the link

#Now make them full urls

teams_urls = [f"https://fbref.com{l}" for l in links]
#this takes each of the links and adds this string to the beggining of the partial urls
#using a format string 
#relative vs absolute links, these are the absolute links 

#now can get the stats we want from the certain team urls
#now can check the first team url which is man city

team_url = teams_urls[0]
#assign to team_url

data = requests.get(team_url)
#download the page, use the get method in the requests library
#makes request to the server and downloads the html from the page 
#and can now import the data about the specific team url

# print(data.text)
#print and check the team url 

#next srep is to take the wholt table and put it all as a pandas dataframe
#pandas has a method that does this already

import pandas as pd
#pyphon data analysis library

matches = pd.read_html(data.text, match="Scores & Fixtures")
#scans all of the table tags and then looks for one that has the scorese & fistures text
#pandas will find the string and grab it fromt he site 

#print(matches)
#currently as a list

matches[0]
#this formats well as a pandas dataframe 
#now installed lxml so now this should work 
#and it does 

#get match shooting stats with requests and pandas
#Find the url of the shooting page 
#find all the links and keep the one that has shooting in it 
#once again utilise beautifulsoup

soup = BeautifulSoup(data.text)
links = soup.find_all('a')
links = [l.get("href") for l in links]
links = [l for l in links if l and 'all_comps/shooting/' in l]
#now grab the sepcific html

data = requests.get(f"https://fbref.com{links[0]}")
#this downlaods our data 
#shows very long string of html
#can pasrse once again with pandas

shooting = pd.read_html(data.text, match="shooting")[0]

#cleaning and merging scraped data with pandas

print(shooting.head())
#looks at the first 5 rows






