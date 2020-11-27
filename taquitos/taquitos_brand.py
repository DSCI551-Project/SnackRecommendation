import requests
from bs4 import BeautifulSoup
import pandas as pd

originalURL = 'https://www.taquitos.net'
URL = 'https://www.taquitos.net/snack-brands'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
mainContent = soup.find(id='maincontent')
longList = mainContent.find(id='longlist' )
all_li = longList.find_all("li")
brandData = []
count = 1
for tag in all_li:
    brand = tag.find("a")
    nextLink = brand["href"]
    # print(brand['href'])
    # print("{0}: {1}".format(tag.name, tag.text))
    item = requests.get(originalURL+nextLink)
    itemSoup = BeautifulSoup(item.content,  'html.parser')
    # print(itemSoup.prettify())
    itemList = itemSoup.find(id='longlist')
    all_item = itemList.find_all("li")
    for item in all_item:
        info=[]
        info.append(tag.text)
        detail = item.find('a')
        itemName = item.text
        itemURL = detail['href']
        detail = requests.get(originalURL+itemURL)
        detailSoup = BeautifulSoup(detail.content, 'html.parser')
        all_review = detailSoup.find_all('p', class_="detail")
        amazonInfo = all_review[0].find('a')
        amazonLink = amazonInfo['href']
        info.append(itemName)
        info.append(originalURL+itemURL)
        info.append(all_review[1].text)
        info.append(all_review[3].text)
        info.append(amazonLink)
        brandData.append(info)
        print(count)
        print(info)
        count+=1

brandDataFrame = pd.DataFrame(brandData, columns = ["brand_name", "snack_name", "snack_url", "snack_taste_test","snack_smell_test", "amazon_link"])
brandDataFrame.to_csv("Taquitos_brand", index=False)




# print(listItem.prettify())

#by type
# for all category  in https://www.taquitos.net/snacks.php, get each type of snack in id="longlist" under id="maincontent" 
    #<a href="/snack_reviews/100_Calorie_Snack_Packs">100 calorie packs</a> sample format result for type of snack, we have an url and name of type
    # for each type of snack, get each item in id="longlist" under id="maincontent"
        #<a href="/candy/100-Calorie-Oreo-Dipped-Delight">100 Calorie Packs Oreo Dipped Delight Bars</a> sample format result of item, another url and name of snack
        #inside the item
        #id="maincontent" -> id="reviewtop"

#by brand
# for all category  in https://www.taquitos.net/snack-brands, get each brand <li> in <ul>  under id="maincontent" 
    #<a href="/snack_guide/3Ds">3D's</a> sample format result for type of snack, we have an url and name of brand
    # for each brand, get each item <li> in <ul> id="longlist" under id="maincontent"
        #<a href="/snacks.php?snack_code=240">Doritos 3D's Jalapeño &amp; Cheddar</a> sample format result of item, another url and name of snack
        #inside the item
        #id="maincontent" -> id="reviewtop"

#2900 -? url change
#endcode -> 9501
#https://www.taquitos.net/snacks.php?snack_code=9501
#name: id="reviewtop" the first h1