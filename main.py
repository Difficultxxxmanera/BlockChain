from binascii import unhexlify, hexlify 
from hashlib import sha256 
from main_block import Block_1

import random, time, datetime, json, hashlib, math, pprint

symbols_hash = '1234567890'
pas = ''
for x in  range(4): 
    pas = pas + random.choice(list(symbols_hash)) 


class Block:
    def __init__(self, data):
        self.next = None
        self.data = data
    def append(self, val):
        end = Block(val)
        n = self
        while (n.next):
            n = n.next
        n.next = end

    def __init__(self, prev_hash, transactor, amount):
        self.next = None
        self.__data = {
            "prev_hash": prev_hash,
            "time": datetime.datetime.now().time(),
            "transactor": transactor,
            "amount": amount,
            "hash": ''
        } 
    def make_hash(self):
       return self.__data["prev_hash"] + 1 
    
    def make_hash(self):
        return self.__data["prev_hash"] + int(int(self.__data["amount"])**1.5) + ord(self.__data["transactor"][-1]) 
    
    def __init__(self, prev_hash, transactor, amount):
        self.next = None
        self.__data = {
            "prev_hash": prev_hash,
            "time": datetime.datetime.now().time(),
            "transactor": transactor,
            "amount": amount,
            "hash": ""
        }
        self.__data["hash"] = self.make_hash() 

    def set_amount(self, amount):
        self.__data["amount"] = amount
        self.__data["hash"] = self.make_hash()
        temp = self
        while (temp.next):
           prev_hash = temp.__data["hash"]
           temp = temp.next
           temp.__update_hashes(prev_hash) 
    def set_amount(self, amount):
        self.__data["amount"] = amount
        self.__data["hash"] = self.make_hash() 
        temp = self
        while(temp.next): 
            def set_amount(self, amount):
                self.__data["amount"] = amount
                self.__data["hash"] = self.make_hash()
                temp = self
                while (temp.next):
                    prev_hash = temp.__data["hash"]
                    temp = temp.next
                    temp.__update_hashes(prev_hash) 
            def __update_hashes(self, new_prev):
                 self.__data["prev_hash"] = new_prev
                 self.__data["hash"] = self.make_hash() 
    def print_chain(chain):
        pp = pprint.PrettyPrinter(indent=4)
        node = chain
        pp.pprint(node.get_data())
        while node.next:
           node = node.next
           pp.pprint(node.get_data()) 
chain = Block(0, 'Tim', 120.00) 
chain.append('Jamil', 200.00)
chain.append('Carla', 123.45)
chain.append('Sarah', 450.00)
print(chain)