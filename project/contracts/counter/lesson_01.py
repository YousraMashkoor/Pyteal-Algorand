'''
1. Each stateful smart contract consists of two bits of teal code approval and clear
2. these are 2 functions
3. after building a contracts if smart contracts returns sigle solitory 1 then that smart contract is build. Otherwise all other will fail

'''


from pyteal import *

def approval():
    return Approve() # approves all transactions in out contracts

def clear():
    return Approve()

