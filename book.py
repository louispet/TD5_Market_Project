#!/usr/bin/env python3
import pandas
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
        df1=pandas.DataFrame(columns=["Type","Price","Quantity"])
        df2=pandas.DataFrame(columns=["Type","Price","Quantity"])
        a=[]
        b=[]
        for n in range(len(self.booksell)):
            b.append(self.booksell[n].id)
            df2=df2.append({"Type":"SELL","Price":self.booksell[n].price,"Quantity":self.booksell[n].quantity},ignore_index=True)
        for n in range(len(self.bookbuy)):
           a.append(self.bookbuy[n].id)
           df1=df1.append({"Type":"BUY","Price":self.bookbuy[n].price,"Quantity":self.bookbuy[n].quantity},ignore_index=True)                                
        df1.index=a
        df2.index=b
        print(df1)
        print(df2)
        return ""
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
