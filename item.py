class Item:
    def __init__(self, itemName, buyLimit, offerPrice, sellPrice, members):
        self.members = bool(members)
        self.itemName = itemName
        self.buyLimit = int(buyLimit)
        self.offerPrice = int(offerPrice)
        self.sellPrice = int(sellPrice)
        self.margin = self.offerPrice - self.sellPrice
        self.inputCost = self.buyLimit * self.offerPrice
        self.roi = (self.margin/self.offerPrice)*100
        self.totalProfit = self.margin * self.buyLimit


    
