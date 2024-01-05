# Web Scrapping
"""Web scraping is an automatic method to obtain large amounts of data from websites. Most of this data is unstructured data in an HTML format 
which is then converted into structured data in a spreadsheet or a database so that it can be used in various applications. There are many 
different ways to perform web scraping to obtain data from websites. These include using online services, particular API’s or even creating 
your code for web scraping from scratch. Many large websites, like Google, Twitter, Facebook, StackOverflow, etc. have API’s that allow you to
 access their data in a structured format."""
#Processing html in python
import lxml 
#For Web Scapping
from bs4 import BeautifulSoup
#For allowing http requests using python
import requests
#For working with Dataset
import pandas as pd
#Creating empty list for scraping name,price,description and reviews
product_names=[]
product_prices=[]
product_descriptions=[]
product_reviews=[]
#Loop for extracting multi page data
for i in range(1,10):
    #Website address from where we want to scrap
    url="https://www.flipkart.com/search?q=mobile+upto+20000&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_4_12_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_4_12_na_na_na&as-pos=4&as-type=RECENT&suggestionId=mobile+upto+20000&requestId=399d9814-4630-4a8e-b1c0-aa3210d2c3ab&as-searchtext=mobile+upto+20000&sort=price_desc&page=" + str(i)
    # Requesting website data
    r=requests.get(url)
    #Initializes a BeautifulSoup object (soup) using the HTML content from an HTTP response (r.text) and specifies the parser to be used ("lxml").
    soup=BeautifulSoup(r.text,"lxml")
    #Finding content in division element
    box=soup.find("div",class_="_1YokD2 _3Mn1Gg") 
    #Finding respective content like name,prices,description and review using division element and stored in a variable
    names=box.find_all("div",class_="_4rR01T")
    prices=box.find_all("div",class_="_30jeq3 _1_WHN1")
    descriptions=box.find_all("ul",class_="_1xgFaf")
    reviews=box.find_all("div",class_="_3LWZlK")
    #Extracting data from name,prices etc. variables and append in there respective list
    for i in names:
        name=i.text
        product_names.append(name)
    for i in prices:
        name=i.text
        product_prices.append(name)
    for i in descriptions:
        name=i.text
        product_descriptions.append(name)
    for i in reviews:
        name=i.text
        product_reviews.append(name)  
#Create data frame from these lists using pandas library
df=pd.DataFrame({"Product_Name":product_names,"Prices":product_prices,"Description":product_descriptions,"Reviews":product_reviews})
#print(len(product_reviews))
#print(df)
#Convering dataframe into csv file for further usage
df.to_csv("flipkart_mobiles_under_20000.csv")
