class Card(object):
    def __init__(self, cardID, passwd, money):
        self.cardID = cardID
        self.passwd = passwd
        self.money = money
        self.isLocked = False