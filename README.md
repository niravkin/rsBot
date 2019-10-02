# rsBot
Objective: The goal of this project is to create a bot that will generate in-game wealth for the game Old School RuneScape. 
We use "flipping" and certain mechanics of the in-game trading mechanism, the Grand Exchange, to make a profit.

DUE TO BOTTING BEING ILLEGAL IN RUNESCAPE, I WILL STRICLY POST MY CODE AND NOT ANY FURTHER REQURED FILES. 
OTHER SCREENSHOTS AND IMAGES ARE REQUIRED TO FULLY RUN THE CODE

The bot was simply made as an exercise, and is not intended to be used on a massive scale for profit. 

# Strategy
We use an third party API called GE Tracker to determine current prices of certain items.

We determine which items are best to trade at the current time by scraping the top 100 most traded items from an official RuneScape page, and using the GE Tracker API to fetch item information.

We sort the top 100 items to determine which will likely be the most profitable.

We use pyautogui/pytesseract to automate buying and selling of the most promising items.

