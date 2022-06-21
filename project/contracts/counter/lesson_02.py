'''
1. Smart contract have different life cycle
2. initialize -> update -> delete -> Opt in -> close -> op op
3. switch and if statement to detenct which type of transactions
'''


from pyteal import *
from pyteal_helpers import program

def approval():
    global_counter = Bytes("counter") # identifier(basically variable) to be used in pyteal - it's name in pyteal is "counter"
    global_owner = Bytes("owner") # byte slice (address)
    return program.event( # seq() to perform multiple opearations
        init = Seq(
            App.globalPut(global_counter, Int(0)),
            App.globalPut(global_owner, Txn.sender()),
            Approve(),
        )
    )

def clear():
    return Approve()

