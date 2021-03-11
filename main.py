#!/usr/bin/env python3
from book import Book

def main():
    """
    Main function of this project. Here we create a book object and we add several orders inside.
    At each step, book will be print
    """
    book=Book("TEST")
    book.insert_buy(10,10.0)
    book.insert_sell(120,12.0)
    book.insert_buy(5,10.0)
    book.insert_buy(2,11.0)
    book.insert_sell(1,10.0)
    book.insert_sell(10,10.0)
                                   
if __name__=="__main__":
    main()
                                                
