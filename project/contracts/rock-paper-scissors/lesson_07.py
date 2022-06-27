from pyteal import *

from pyteal_helpers import program

def approval():
    # local variables
    local_opponent = Bytes("opponent") #byteslice - address
    local_wager  = Bytes("wager") # uint64
    local_commitment = Bytes("commitment") #byteslice - hash play
    local_reveal = Bytes("reveal") # byteslice - unhashed play
    
    # opearations/functions
    op_challenge = Bytes("challenge") # initiate the challenge
    op_accept = Bytes("accept") # accept the challenge
    op_reveal = Bytes("reveal") # reveal the challenge

    # subroutines
    @Subroutine(TealType.none) # define return type inside the subroutine decorator
    def reset(account: Expr):
        return Seq(
            App.localPut(account, local_opponent, Bytes("")),
            App.localPut(account, local_wager, Int(0)),
            App.localPut(account, local_commitment, Bytes("")),
            App.localPut(account, local_reveal, Bytes("")),
        )

    @Subroutine(TealType.none)
    def create_challenge():
        return Reject()

    @Subroutine(TealType.none)
    def accept_challenge():
        return Reject()

    @Subroutine(TealType.none)
    def reveal():
        return Reject()


    return program.event(
        init = Approve(), # since all the variables are in local we can directly approve it here
        opt_in = Seq(
            reset(Int(0)), # Int(0) is the sender account address
            Approve(),
        ),
        no_op=Seq(
            Cond(
                [Txn.application_args[0] == op_challenge, create_challenge()],
                [Txn.application_args[0] == op_accept, accept_challenge()],
                [Txn.application_args[0] == op_reveal, reveal()],
            ),
            Reject(),
        )
    )

def clear():
    return Approve()
