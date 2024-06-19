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
