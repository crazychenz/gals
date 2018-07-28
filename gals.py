#!/usr/bin/env python

import sys
import argparse
import yaml
import pprint
import uuid
import string

from Kiosk import Kiosk
from UserWebService import UserWebService
from Title import Title
from Inventory import Inventory
from Book import Book

from Admin import Admin
from Patron import Patron
from Employee import Employee

def inventory_import(invdb):
    pass
    #inv = Inventory()

    #for entry in invdb:
    #    title = Title(entry['isbn'], entry['title'], entry['author'])
    #    inv.add_title(title)
    #    for qr_code in entry['qr_codes']:
    #        # TODO: Add location
    #        book = Book(qr_code, title)
    #        title.add_book(book)

def main():

    # load the system state
    db = yaml.load(open("inventory.yaml").read())
    inventory_import(db['inventory'])
    #pprint.pprint(obj)

    # (System) Creates inventory
    inv = Inventory()

    # (System) Creates admin
    admin = Admin("Joe")

    # (System) Creates kiosk .. and adds it to the inventory
    kiosk = Kiosk('aacpl')
    Kiosk.add_kiosk(kiosk)

    # (Admin) Creates a title .. and adds it to the inventory
    title1 = Title(1234, "title1", "author1")
    Title.add_title(title1)

    # (Admin) Creates a book .. and associates it with a title and bearer
    Book.add_book(Book(4321, title1, admin))

    # *Admin sends book to kiosk for insertion*

    # (Employee) Inserts book into kiosk (via qr_code)
    kiosk.insert_book(4321)
    print "\nKiosk Title Availability: (Employee just inserted a book)"
    pprint.pprint(kiosk.available_books_by_title)
    pprint.pprint(kiosk.reserved_books_by_title)


    # (User) Searches for book
    userweb1 = UserWebService("user1")
    results = userweb1.search("title1")
    print "\nSearch Results: (User just searched for a title.)"
    pprint.pprint(results)

    # (User) Reserves A Book
    title_choice = results.items()[0][0]
    kiosk_choice = results.items()[0][1].keys()[0]
    userweb1.reserve_title(title_choice, kiosk_choice)
    print "\nKiosks Title Availability: (User just reserved a title)"
    pprint.pprint(kiosk.available_books_by_title)
    pprint.pprint(kiosk.reserved_books_by_title)

    # Another user tries for the same title, but must request
    userweb2 = UserWebService("user2")
    results = userweb2.search("title1")
    print "\nSearch Results: (User Searched For Unavailable Title)"
    pprint.pprint(results)

    # 2nd User Requests Title
    title_choice = results.items()[0][0]
    kiosk_choice = results.items()[0][1].keys()[0]
    userweb2.request_title(title_choice, kiosk_choice)
    print "\nKiosk Requests: (User just requested unavailable title.)"
    pprint.pprint(kiosk.requests)

    # First user picks up a book.
    kiosk.eject_reserved_book("user1", 4321)
    print "\nBook Bearer: ", Book.find_book(4321).bearer_uuid
    print "Kiosks Title Availability: (User just picked up a book)"
    pprint.pprint(kiosk.available_books_by_title)
    pprint.pprint(kiosk.reserved_books_by_title)

    # User returns book
    kiosk.insert_book(4321)
    print "\nBook Bearer: ", Book.find_book(4321).bearer_uuid
    print "Kiosks Title Availability: (User just returned a book)"
    pprint.pprint(kiosk.available_books_by_title)
    pprint.pprint(kiosk.reserved_books_by_title)

    # Second user picks up a book.
    kiosk.eject_reserved_book("user2", 4321)
    print "\nBook Bearer: ", Book.find_book(4321).bearer_uuid
    print "Kiosks Title Availability: (User just picked up a book)"
    pprint.pprint(kiosk.available_books_by_title)
    pprint.pprint(kiosk.reserved_books_by_title)

    # Second user returns book
    kiosk.insert_book(4321)
    print "\nBook Bearer: ", Book.find_book(4321).bearer_uuid
    print "Kiosks Title Availability: (User just returned a book)"
    pprint.pprint(kiosk.available_books_by_title)
    pprint.pprint(kiosk.reserved_books_by_title)

    #parser = argparse.ArgumentParser(description='GALS Prototyle System')
    #subparsers = parser.add_subparsers(help='sub-command help')
    #kiosk_parser = subparsers.add_parser('kiosk', help='kiosk commands')
    #kiosk_parser.add_argument('--checkout', help='checkout book')
    #userweb_parser = subparsers.add_parser('userweb', help='kiosk commands')
    #userweb_parser.add_argument('--search', help='checkout book')
    #print parser.parse_args(sys.argv[1:])

main()
