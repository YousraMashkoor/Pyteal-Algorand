'''
1. Smart contract have different life cycle
2. initialize -> update -> delete -> Opt in -> close -> op op
3. switch and if statement to detenct which type of transactions
4. no_op -> define own operations
'''


from pyteal import *
from pyteal_helpers import program

UINT64_MAX = 0xffffffffffffffff

def approval():
    ## Variables
    global_counter = Bytes("counter") # identifier(basically variable) to be used in pyteal - it's name in pyteal is "counter"
    global_owner = Bytes("owner") # byte slice (address)

    ## Function
    op_increment = Bytes("inc") # declate oparations/functions
    op_decrement = Bytes("dec")


    ## Scartch Variables
    scratch_counter = ScratchVar(TealType.uint64)

    ## Expression
    increment = Seq(
        scratch_counter.store(App.globalGet(global_counter)),
        ## Detecting Overflow
        If(
            scratch_counter.load() < Int(UINT64_MAX)
        )
        .Then(
            App.globalPut(global_counter, scratch_counter.load() + Int(1)),
        ),
        Approve(),
    )

    decrement = Seq(
        scratch_counter.store(App.globalGet(global_counter)),
        ## Detecting Underflow
        If(
            scratch_counter.load() > Int(0)
        )
        .Then(
            App.globalPut(global_counter, scratch_counter.load() - Int(1)),
        ),
        Approve(),
    )

    return program.event(
        init = Seq(
            App.globalPut(global_counter, Int(0)),
            App.globalPut(global_owner, Txn.sender()),
            Approve(),
        ),
        no_op=Cond(
            [Txn.application_args[0] == op_increment, increment],
            [Txn.application_args[0] == op_decrement, decrement],
        ),
    )

def clear():
    return Approve()

