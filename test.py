from PIL import Image
import PIL.Image
import pyautogui
import pytesseract
import requests
import cv2
import time
import numpy as np
import beautifulsoup4

#tesseract didnt work on my PC so I had to manually install it from 
#https://github.com/UB-Mannheim/tesseract/wiki
#then just update the location below to the location on your own PC
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#The amount of money in our inventory

currentMoney = 0

def checkMoney():
    try:
        #Screenshots "Price of..."
        location = pyautogui.locateOnScreen('chatDownArrow.png')#returns a tuple left, top, width, height
        im = pyautogui.screenshot(region=(location[0] - 490, location[1], 450, 20))
        im.save(r"C:\Users\Nirav\Desktop\code\rsBot\moneyscreenshot.png")
        text = pytesseract.image_to_string(Image.open('moneyscreenshot.png'))
        text = text.replace(',', '')
        result = [int(i) for i in text.split() if i.isdigit()]
        currentMoney = result[0]
        print("Current Money =", currentMoney)

    except TypeError:
        print("Check Money")

def checkLastTrans():
    try:
        try:
            x, y = pyautogui.locateCenterOnScreen('history.png')
            pyautogui.moveTo(x, y, 2, pyautogui.easeOutQuad)
            time.sleep(.25)
            pyautogui.click()
            time.sleep(.55)
            bought = False
        except TypeError: 
            print("history")
        try:
            #Bought or Sold
            location = pyautogui.locateCenterOnScreen('exchange.png')
            im = pyautogui.screenshot(region=(location[0] + 5, location[1] + 30, 50, 20))
            im.save(r"C:\Users\Moin\Desktop\code\rsBot\trans.png")
            text = pytesseract.image_to_string(Image.open('trans.png'))
            if text != "Sate":
                bought = True
        except TypeError:
            print("exchange")
        try:
            #Get Coins
            location = pyautogui.locateCenterOnScreen('historyUpArrow.png')
            lastTrans = pyautogui.screenshot(region=(location[0] - 150, location[1]-5, 150, 20))
            lastTrans.save(r"C:\Users\Moin\Desktop\code\rsBot\lastTrans.png")
            text = pytesseract.image_to_string(Image.open('lastTrans.png'))
            text = text.replace(',', '')
            result = [int(i) for i in text.split() if i.isdigit()]
            coins = result[0]
        except TypeError:
            print("historyUpArrow")
        if bought == True:
            print("Bought for:", coins)
        else:
            print("Sold for:", coins)

    except TypeError:
        print("Error in checkLastTrans")

#Collects the items in the first buy/sell slot
def collectItemSlot1():
    x, y = pyautogui.locateCenterOnScreen('history.png')
    pyautogui.moveTo(x, y+100, 2.5)
    pyautogui.click()
    x1, y1 = pyautogui.locateCenterOnScreen('itemSlot1.png')
    pyautogui.moveTo(x1, y1+15, 1)
    time.sleep(.25)
    pyautogui.click()
    time.sleep(.25)

def collectItemSlot2():
    x, y = pyautogui.locateCenterOnScreen('itemSlot2.png')
    pyautogui.moveTo(x, y+15, .25)
    time.sleep(.25)
    pyautogui.click()

def checkMargin(fname):
    print("The name of the item is:", fname)
    x = 0
    y = 0
    #Buying Item 
    try:
        x, y = pyautogui.locateCenterOnScreen('history.png')
        #Buy Location Also Buys the item
        pyautogui.moveTo(x, y+100, 2.5)
        time.sleep(1)
        pyautogui.click()
        time.sleep(2)
        pyautogui.typewrite(fname, interval=.25)
        time.sleep(1)
        pyautogui.press('enter')
        x2, y2 = pyautogui.locateCenterOnScreen('raise5%.png')
        pyautogui.moveTo(x2, y2, 0.5, pyautogui.easeOutQuad)
        time.sleep(.25)
        pyautogui.click(clicks=5, interval=.25)
        time.sleep(1)
        x3, y3 = pyautogui.locateCenterOnScreen('confirm.png')
        pyautogui.moveTo(x3, y3, 0.3, pyautogui.easeOutQuad)
        pyautogui.click()
        collectItemSlot1()
        collectItemSlot2()
        #Need to finish implementing check last transaction in order to actually check the margin
        
        #Sells Item
        x, y = pyautogui.locateCenterOnScreen('history.png')
        #Sell Location for first Sell slot Also Buys the item
        pyautogui.moveTo(x+60, y+110, 2.5)
        time.sleep(1)
        pyautogui.click()
        x2, y2 = pyautogui.locateCenterOnScreen('inventoryBag.png')
        pyautogui.moveTo(x2-30, y2+40, 1.2)
        time.sleep(.25)
        pyautogui.click()
        x2, y2 = pyautogui.locateCenterOnScreen('lower5%.png')
        pyautogui.moveTo(x2, y2, 0.5, pyautogui.easeOutQuad)
        time.sleep(.25)
        pyautogui.click(clicks=5, interval=.25)
        x3, y3 = pyautogui.locateCenterOnScreen('confirm.png')
        pyautogui.moveTo(x3, y3, 0.3, pyautogui.easeOutQuad)
        pyautogui.click()
        collectItemSlot1()
        collectItemSlot2()
    except TypeError:
        print("buy slot not found")


#Documentation on GETracker API:https://documenter.getpostman.com/view/3756775/ge-tracker/RVnTkLh1?version=latest
#API Key: eb7ac7f38d3767f0ae8f1128be4429cf72327b8359a0719468500b20da6ad7e7
apiKey = 'eb7ac7f38d3767f0ae8f1128be4429cf72327b8359a0719468500b20da6ad7e7'
response = requests.get(
    'https://www.ge-tracker.com/api/items/377',
    headers={
        'Authorization':'Bearer eb7ac7f38d3767f0ae8f1128be4429cf72327b8359a0719468500b20da6ad7e7',
        'Accept':'application/x.getracker.v1+json',
        }
)
response_json = response.json()
#print(response_json['data']) #The entire json dictionary
print("Item Name:", response_json['data']['name'])
print("Buy Limit:", response_json['data']['buyLimit'])
print("Offer Price:", response_json['data']['selling'])
print("Sell Price:", response_json['data']['buying'])
print("Profit Per Sell", response_json['data']['buying']-response_json['data']['selling'])
print("Updated At:", response_json['data']['updatedAt'])

checkMoney()
#checkLastTrans()

#collectItems()
checkMargin(response_json['data']['name'])

location = pyautogui.locateCenterOnScreen('historyUpArrow.png')
lastTrans = pyautogui.screenshot(region=(location[0] - 155, location[1]+1.5, 140, 15))
lastTrans.save(r"C:\Users\Nirav\Desktop\code\rsBot\lastTrans.png")
text = pytesseract.image_to_string(Image.open('lastTrans.png'))
result = [int(i) for i in text.split() if i.isdigit()]
print(text)
