"""

Order book:

Bid Orders: 10, 20, 30, 40
Ask Orders: 70, 60, 50, 40

Bid - highest bid
Ask - lowest ask

- create bids
- create asks


Classes
- Order:
    - Price [float]
    - Type (Bid/Ask) [str]
    - Quantity [int]

- OrderBook:
    - Bids [list]
    - Asks [list]

    Functions:
    - Create Order
    - Get Highest Bid
    - Get Lowest Ask
    - MatchingEngine


1. quickly add / remove order
2. quickly get highest bid / lowest ask
3. quickly match orders

In order to do this, let's keep sorted list of bids and asks
Bids -> ascending order (highest bid at the end)
Asks -> descending order (lowest ask at the end)

Bid Orders: 10, 20, 30, 40
Ask Orders: 70, 60, 50, 40

1. to add/remove orders:
-> 0(nLogN) binary search to find the index to insert a new element / remove an element

2. quickly get highest bid / lowest ask:
O(1)
- Get highest bid -> Bids[-1]
- Get lowest ask -> Asks[-1]

3. quickly match orders:
- Match orders when bid >= ask
By getting the highest bid and lowest ask

"""


class Order:
    def __init__ (self, price, quantity, orderType):
        self.price = price
        self.quantity = quantity
        self.orderType = orderType
    
    def __repr__(self):
        return str(self.price) + ":" + str(self.quantity) + ":" + str(self.orderType)
        return str("Price: " + str(self.price) + " Quantity: " + str(self.quantity) + " OrderType: " + str(self.orderType))


class OrderBook:
    def __init__(self):
        
        self.bids = []
        self.asks = []
    
    #o(1) operation
    def get_highest_bid(self):
        if len(self.bids) != 0:
            return self.bids[-1]
        else:
            return None
            
    #o(1) operation
    def get_lowest_ask(self):
        if len(self.asks) != 0:
            return self.asks[-1]
        else:
            return None
    
    def add_order(self, order):
        print("adding order, ", order)
        if order.orderType == "bid":
            
           # Bid Orders: 10, 20, 30, 40
           #              0,  1, 2,  3
           
            if len(self.bids) == 0:
               self.bids.append(order)
               return
               
            l = 0
            r = len(self.bids)-1
            
            while l <= r:

                mid = (l + r) // 2
                mid_price = self.asks[mid].price
                if (order.price >= mid_price):
                    l = mid + 1
                else:
                    r = mid - 1

            self.bids.insert(l, order)
            
        elif order.orderType == "ask":
           
            if len(self.asks) == 0:
               self.asks.append(order)
               return
               
            l = 0
            r = len(self.asks)-1
            
            while l <= r:
                mid = (l + r) // 2
                mid_price = self.asks[mid].price
                if (order.price <= mid_price):
                    l = mid + 1
                else:
                    r = mid - 1

            self.asks.insert(l, order)


        print("new self.bids", self.bids)
        print("new self.asks", self.asks)

        self.match_orders()
                
    def match_orders(self):
        highest_bid = self.get_highest_bid()
        lowest_ask = self.get_lowest_ask()


        if highest_bid is None or lowest_ask is None:
            return
        
        while highest_bid.price >= lowest_ask.price:
            print("Matched Orders")
            print("Highest Bid: ", highest_bid)
            print("Lowest Ask: ", lowest_ask)


            if highest_bid.quantity > lowest_ask.quantity:
                highest_bid.quantity -= lowest_ask.quantity
                self.asks.pop()

            elif highest_bid.quantity < lowest_ask.quantity:
                lowest_ask.quantity -= highest_bid.quantity
                self.bids.pop()

            elif highest_bid.quantity == lowest_ask.quantity:
                self.bids.pop()
                self.asks.pop()


            highest_bid = self.get_highest_bid()
            lowest_ask = self.get_lowest_ask()

            if highest_bid is None or lowest_ask is None:
                return

        



orderBook = OrderBook()
# orderBook.add_order(Order(200.0, 4, "bid"))
# orderBook.add_order(Order(100.0, 5, "ask"))
# orderBook.add_order(Order(300.0, 4, "bid"))
# orderBook.add_order(Order(150.0, 5, "ask"))
# orderBook.add_order(Order(250.0, 5, "bid"))
# orderBook.add_order(Order(350.0, 5, "bid"))
# orderBook.add_order(Order(50.0, 5, "bid"))


orderBook.add_order(Order(100.0, 5, "ask"))
orderBook.add_order(Order(200.0, 5, "ask"))
orderBook.add_order(Order(50.0, 5, "ask"))
orderBook.add_order(Order(100.0, 5, "ask"))
orderBook.add_order(Order(101.0, 5, "ask"))
orderBook.add_order(Order(303.0, 5, "ask"))
orderBook.add_order(Order(21.0, 5, "ask"))
