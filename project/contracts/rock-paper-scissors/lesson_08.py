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

    @Subroutine(TealType.uint64)
    def is_empty(account: Expr):
        return Return(
            And(
                App.localGet(account, local_opponent) == Bytes(""),
                App.localGet(account, local_commitment) == Bytes(""),
                App.localGet(account, local_reveal) == Bytes(""),
                App.localGet(account, local_wager) == Int(0),
            )
        )

    @Subroutine(TealType.none)
    def create_challenge():
        return Seq(
            program.check_self(
                group_size=Int(2),
                group_index=Int(0), # the one calling this subroutine is me - Index[0]
            ),
            program.check_rekey_zero(2), # check for 2 transactions
            Assert(
                And( 
                    # check wager payment transaction
                    Gtxn[1].type_enum() == TxnType.Payment, # Gtxn -> group transaction, check if it's of type payment
                    Gtxn[1].receiver() == Global.current_application_address(), # check that payment is being made to me
                    Gtxn[1].close_remainder_to() == Global.zero_address(),

                    # check opponent is opted in/ joined the contract life cycle
                    App.optedIn(Txn.accounts[1], Global.current_application_id()),

                    # check ot make sure that both accounts are available to play
                    is_empty(Txn.sender()),
                    is_empty(Txn.accounts[1]),

                    # check for commitemnt argument
                    Txn.application_args.length() == Int(2),
                ),
            ),
            App.localPut(Txn.sender(), local_opponent, Txn.accounts[1]),
            App.localPut(Txn.sender(), local_wager, Gtxn[1].amount()), # wagers is that payment transaction amount
            App.localPut(Txn.sender(), local_commitment, Txn.application_args[1]), 
            Approve(),
        )

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
