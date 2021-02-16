class Order():
    cpt=1
    # Définition des variables
    def __init__(self,quantity,price,buy=True):
        self.quantity=quantity
        self.price=price
        self.buy=buy
        self.id=Order.cpt
        Order.cpt+=1
    def __eq__(self,other):
        #return other and self.quantity == other.quantity and self.price==other.price
        return other and self.price==other.price
    def __lt__(self,other):
        return other and self.price<other.price
        # Affichage de l'ordre
    def __str__(self,hist=0):
        return ("ID %i -- %i stocks @ price %d  " %(self.id,self.quantity,self.price))
    def __del__(self):
        return 0


class Book(Order):
    def __init__(self,name):
        self.__name=name
        self.bookbuy=[]
        self.booksell=[]
    def insert_buy(self,quantity,price):
        insert=Order(quantity,price)
        self.bookbuy.append(insert)
        print ("-- INSERT BUY  -- " , insert)
        self.verif_ordre()
        print(self)
    def insert_sell(self,quantity,price,sell=False):
        insert=Order(quantity,price,False)
        self.booksell.append(insert)
        print("-- INSERT SELL -- " , insert)
        self.verif_ordre()
        print(self)
    def __str__(self):
        res=""
        for n in range(len(self.booksell)):
            res+= "SELL  -------- Id : %i ------ Quantity %s @ Price %s\n" %(self.booksell[n].id,self.booksell[n].quantity,self.booksell[n].price)
        for n in range(len(self.bookbuy)):
            res+= "BUY  --------- Id : %i ------ Quantity %s @ Price %s\n" %(self.bookbuy[n].id,self.bookbuy[n].quantity,self.bookbuy[n].price)
        return res
    def sort(self):
        self.bookbuy= sorted(self.bookbuy,key=lambda Order: Order.price, reverse=True)
        self.booksell=sorted(self.booksell,key=lambda Order: Order.price)
    def verif_ordre(self):
        self.sort()
        i=0
        if (len(self.bookbuy)!=0 and len(self.booksell)!=0):
            while True:
                if (self.bookbuy[i]==self.booksell[i] or self.bookbuy[i]>self.booksell[i]):
                    self.execute_order(i)
                else:
                    break
    def execute_order(self,i):
        if (self.bookbuy[i].quantity<self.booksell[i].quantity):
            print("Execute order to %i share in %d price" %(self.bookbuy[i].quantity,self.bookbuy[i].price))
            temp=self.bookbuy[i].quantity
            self.bookbuy[i].quantity-self.booksell[i].quantity
            self.booksell[i].quantity-=temp
            del(self.bookbuy[i])
            "On soustrait le caener de vente du nombre de quantité de carnet d'achat"
            "On doit détruie l'ordre indice 0"
        if (self.bookbuy[i].quantity>self.booksell[i].quantity):
            print("Execute order to %i share in %d price" %(self.booksell[i].quantity,self.booksell[i].price))
            temp=self.booksell[i].quantity
            self.booksell[i].quantity-self.bookbuy[i].quantity
            self.bookbuy[i].quantity-= temp
            del(self.booksell[i])
        if (self.bookbuy[i].quantity==self.booksell[i].quantity):
            print("Execute order to %i share in %d price" %(self.bookbuy[i].quantity,self.bookbuy[i].price))
            del(self.booksell[i])
            del(self.bookbuy[i])
