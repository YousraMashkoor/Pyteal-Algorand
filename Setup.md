
# Setting up Workspace

## **STEP 01:**
Clone the sandbox repository:  
https://github.com/algorand/sandbox


Clone the Pyteal project Template:  
https://github.com/algorand-devrel/pyteal-course

## **STEP 02:**
Add your project path under values in sandbox/docker-compose.yaml  
```
volumes:
      - type: bind
        source: ../project
        target: /data
```

## **STEP 03:**
Install the virtual environment and download packages

```
cd project
python3 -m venv venv
source ./venv/bin/activate
pip3 install -r requirements.txt
```

## **STEP 04:**
Start your docker desktop

<br />

> ### **Commands:**
_______________________________________________________________________________

goto sandbox folder and run following commands
  
```
./sandbox up
./sandbox down
./sandbox reset
```

if you're using a linux system, you might need to use the above commands with sudo.

<br />


> ### **Potential ERRORS during SETUP:**
_______________________________________________________________________________ 
   
     
1.  `Invalid type in volume, it should be a string`

change the version from '3' to '3.2' in docker-compose.yaml

2. `Couldn't connect to Docker daemon at http+docker://localhost - is it running?`

Setup previlages
```
sudo chmod 666 /var/run/docker.sock
sudo service docker start
```
