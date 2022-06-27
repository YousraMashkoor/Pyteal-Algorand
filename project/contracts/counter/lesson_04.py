'''
1. Smart contract have different life cycle
2. initialize -> update -> delete -> Opt in -> close -> op op
3. switch and if statement to detenct which type of transactions
4. no_op -> define own operations
'''


from pyteal import *
from pyteal_helpers import program

def approval():
    ## Variables
    global_counter = Bytes("counter") # identifier(basically variable) to be used in pyteal - it's name in pyteal is "counter"
    global_owner = Bytes("owner") # byte slice (address)

    ## Function
    op_increment = Bytes("inc") # declate oparations/functions
    op_decrement = Bytes("dec")

    ## Expression
    increment = Seq(
        App.globalPut(global_counter, App.globalGet(global_counter) + Int(1)),
        Approve(),
    )

    decrement = Seq(
        App.globalPut(global_counter, App.globalGet(global_counter) - Int(1)),
        Approve(),
    )

    return program.event( # seq() to perform multiple opearations
        init = Seq(
            App.globalPut(global_counter, Int(0)),
            App.globalPut(global_owner, Txn.sender()),
            Approve(),
        ),
        ## conditional is like a switch statement
        # of none of the condition run, thats an error and transaction will reject
        no_op=Cond(
            [Txn.application_args[0] == op_increment, increment], # if function is this use increment expression
            [Txn.application_args[0] == op_decrement, decrement],
        ),
    )

def clear():
    return Approve()

