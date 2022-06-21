import importlib
import sys

from pyteal_helpers import program

if __name__ == "__main__":
    mod = sys.argv[1]

    try:
        approval_out = sys.argv[2] # reads the two output file approval and clear
    except IndexError:
        approval_out = None

    try:
        clear_out = sys.argv[3] # reads the two output file approval and clear
    except IndexError:
        clear_out = None

    contract = importlib.import_module(mod) # reads into module

    if approval_out is None:
        print(program.application(contract.approval())) # calls approval fuction
    else:
        with open(approval_out, "w") as h:
            h.write(program.application(contract.approval())) # calls clear fuction

    if clear_out is not None:
        with open(clear_out, "w") as h:
            h.write(program.application(contract.clear()))
