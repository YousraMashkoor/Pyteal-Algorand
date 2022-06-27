# Algorand Pyteal Workspace

## **Setup**
Follow this Guide to setup the repository with Sandbox  
[![Guide](https://img.shields.io/badge/guide-repository%20setup-green)](https://github.com/YousraMashkoor/Pyteal-Algorand/blob/master/Setup.md)


## **Topics:**
**Lesson 01:** [Creating First Smart Contract:](#lesson-01-creating-first-smart-contract)  
**Lesson 02:** [Initializing Contract:](#lesson-02-initializing-contract)  
**Lesson 03:** [Deploying Contract on Sandbox:](#lesson-03-deploying-contract-on-sandbox)  
**Lesson 04:** [Custom Opearations/Functions:](#lesson-04-custom-opearationsfunctions)  
**Lesson 05:** [Debugging:](#lesson-05-debugging)   
**Lesson 06:** [Scratch Variables and Constants:](#lesson-06-scratch-variables-and-constants)  
**Lesson 07:** [Storage and Subroutines:](#lesson-07-local-storage-and-subroutines)  

<br />
<br />

## **Lesson 01:** [Creating First Smart Contract:](https://github.com/YousraMashkoor/Pyteal-Algorand/blob/master/project/contracts/counter/lesson_01.py)
1. Each stateful smart contract consists of two bits of teal code approval and clear
2. build a contract using command
```
cd project
./build.sh contracts.counter.step_01
```
3. After building a contracts if smart contracts returns sigle solitory 1 then that smart contract is build. Otherwise all other will fail

## **Lesson 02:** [Initializing Contract:](https://github.com/YousraMashkoor/Pyteal-Algorand/blob/master/project/contracts/counter/lesson_02.py)
1. Smart contract have different life cycle
2. initialize -> update -> delete -> Opt in -> close -> op op
3. switch and if statement to detenct which type of transactions
4. In pyeal variables are called Identifiers

## **Lesson 03:** [Deploying Contract on Sandbox:](#lesson-03-deploying-contract-on-sandbox)
1. build a contract using command
```
cd project
./build.sh contracts.counter.lesson_02.py
```
2. checkout /build/approval.teal
3. Enter docker container
```
sudo ./sandbox enter algod
```
4. use following commands to check if the volume binding between docker and project is working
```
ls /data
```
5. get list of accounts and assign 1 to a variable
```
goal account list
ONE = [any account hash here]
```
6. Deploying contract
- --creator = owner/person deploying contract
- --approval-prog = path of approval.teal from docker
- --clear-prog = path of clear.teal from docker
- --global-byteslices = total number of global byteslices used in program
- --global-ints = total number of global ints used in program
- --local-byteslices = total number of local byteslices used in program
- --local-ints = total number of local ints used in program

```
goal app create --creator $ONE --approval-prog /data/build/approval.teal --clear-prog /data/build/clear.teal --global-byteslices 1 --global-ints 1 --local-byteslices 0 --local-ints 0
```
7. get deployed contract details
```
goal app info --app-id 1
```
8. read our smar contract storage
```
goal app read --global --app-id 1
```
format the output
```
goal app read --global --app-id 1 --guess-format
```

## **Lesson 04:** [Custom Opearations/Functions:](https://github.com/YousraMashkoor/Pyteal-Algorand/blob/master/project/contracts/counter/lesson_04.py)
1. no_op -> define own operations
2. Cond() is like a switch statement. If none of the condition run, thats an error and transaction will reject
3. Expressions needs to be defined separately like methods
4. Build and deploy contracts using steps in Lession_03
5. The command to call the smart contract is:
```
goal app call --app-id 1 --from $ONE --app-arg "str:inc"
```

## **Lesson 05:** [Debugging:](#lesson-05-debugging)

1. In order to debug we need to first create a transaction dump file
```
goal app call --app-id 2 --from $ONE --app-arg "str:dec" --dryrun-dup -o tx.dr
```
2. initialize debugger session, uses chrome debugger tool
```
tealdbg debug -d tx.dr --listen 0.0.0.0
```
3. Goto chrome://inspect/#devices
4. Goto configure and add **localhost:9392**
5. Goto Inspect
6. Add breakpoint and debug your opearation

## **Lesson 06:** [Scratch Variables and Constants:](https://github.com/YousraMashkoor/Pyteal-Algorand/blob/master/project/contracts/counter/lesson_06.py)
Scratch variables are temporary variables that is destroyed after transaction ends

## **Lesson 07:** [Local Storage and Subroutines:](https://github.com/YousraMashkoor/Pyteal-Algorand/blob/master/project/contracts/rock-paper-scissors/lesson_07.py)
1. Subroutines is a type of a method/function in Pyteal
2. Local storage is stored with every account and not the smart contract
3. We're not using global storage so if multiple users are playing the games they are not modifying each others results.
4. Smart Contract stores upto 4 accounts ids, where index(0) is the transaction/sender

Build and deploy the contract (see steps mentioned in lesson_03)
```
./build.sh contracts.rock-paper-scissors.lesson_07

goal app create --creator $ONE --approval-prog /data/build/approval.teal --clear-prog /data/build/clear.teal --global-byteslices 0 --global-ints 0 --local-byteslices 3 --local-ints 1

goal app optin --from $ONE --app-id 14

goal app read --local --from $ONE --app-id 14
```