# Algorand Pyteal Workspace

## **Setting up Repository:**


### **STEP 01:**
Clone the sandbox repository:  
https://github.com/algorand/sandbox


Clone the Pyteal project Template:  
https://github.com/algorand-devrel/pyteal-course

### **STEP 02:**
Add your project path under values in sandbox/docker-compose.yaml  
```
volumes:
      - type: bind
        source: ../project
        target: /data
```

### **STEP 03:**
Install the virtual environment and download packages

```
cd project
python3 -m venv venv
source ./venv/bin/activate
pip3 install -r requirements.txt
```

### **STEP 04:**
Start your docker desktop


## **Commands:**

goto sandbox folder and run following commands
  
```
./sandbox up
./sandbox down
./sandbox reset
```

if you're using a linux system, you might need to use the above commands with sudo.




## **Potential ERRORS during SETUP:**
   

1.  `Invalid type in volume, it should be a string`

change the version from '3' to '3.2' in docker-compose.yaml

2. `Couldn't connect to Docker daemon at http+docker://localhost - is it running?`

Setup previlages
```
sudo chmod 666 /var/run/docker.sock
sudo service docker start
```



## **Topics:**

### **Lesson 01:** Creating First Smart Contract:
1. Each stateful smart contract consists of two bits of teal code approval and clear
2. build a contract using command
```
cd project
./build.sh contracts.counter.step_01
```
3. After building a contracts if smart contracts returns sigle solitory 1 then that smart contract is build. Otherwise all other will fail

### **Lesson 02:** Initializing Contract:
1. Smart contract have different life cycle
2. initialize -> update -> delete -> Opt in -> close -> op op
3. switch and if statement to detenct which type of transactions
4. In pyeal variables are called Identifiers

### **Lesson 03:** Deploying Contract on Sandbox:
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