import requests
from item import Item
import urllib.request
import time
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup

#Scrape most traded items:
link = 'http://services.runescape.com/m=itemdb_oldschool/top100'
response = requests.get(link)
soup = BeautifulSoup(response.text, "html.parser")
itemlinks = soup.findAll('a', class_="table-item-link")
itemids = [itemlink['href'].split('obj=')[1] for itemlink in itemlinks] #top 100 most traded items' ids

#API Key: eb7ac7f38d3767f0ae8f1128be4429cf72327b8359a0719468500b20da6ad7e7
apiKey = 'eb7ac7f38d3767f0ae8f1128be4429cf72327b8359a0719468500b20da6ad7e7'
url = 'https://www.ge-tracker.com/api/items/multi/?itemIds='
url += str(itemids[0])
for itemid in itemids[1:]:
    url += ',' + str(itemid)
items = []
try:
    response = requests.get(
        url, 
        headers={
            'Authorization':'Bearer eb7ac7f38d3767f0ae8f1128be4429cf72327b8359a0719468500b20da6ad7e7',
            'Accept':'application/x.getracker.v1+json',
            }
    )
    jsonresponse = response.json()
    for i in jsonresponse['data']:
        if i['members']:
            items.append(Item(i['name'], i['buyLimit'], i['selling'], i['buying'], True))
        else:
            items.append(Item(i['name'], i['buyLimit'], i['selling'], i['buying'], False))


except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')  
except Exception as err:
    print(f'Other error occurred: {err}')  
else:
    pass

items.sort(key=lambda x: x.roi, reverse=True) #in place sort based on object attribute
for i in items:
    if(i.members == False):
        print(i.itemName, 'ROI:', i.roi, 'Profit', i.totalProfit)


