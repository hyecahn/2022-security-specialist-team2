# Team 2, 2022-Security Specialist

## Prerequisites
Python 3.10+ (tested against 3.10)

## Step 1
Make python env
```
$ python -m venv team2 
$ cd team2/Script
$ activate // (for vscode)
```

## Step 2 
Install PIP requirements
```
$ cd OpenAlpr\studio
$ pip install -r .\requirement.txt 
```

## Step 3
Install openAlpr for python
```
$ cd .\openalpr64-sdk-4.1.1\python\
$ python .\setup.py install
```

## Step 4
Migiration DB
```
$ cd studio\webapp
$ python .\manage.py makemigrations
(select option 1 and input any text after that.)

$ python .\manage.py migrate   
```

## Setup 5
Setting Django server
```
If you want to make your PC as a Django Webserver in Windows OS, you should modify hosts file to support https.
Windows OS Host file path: C:\Windows\System32\drivers\etc\hosts

Add {{ALPR IP ADDRESS}} ahnlab2.lge.com to C:\Windows\System32\drivers\etc\hosts

e.g) your  IP address is 10.58.7.138, change host file like below. 
      
    10.58.7.138 ahnlab2.lge.com
```    
```
$ cd webapp
$ change IPADDRESS = '10.58.7.138' to correct ipaddress in settings.py

$ cd
$ python .\manage.py makemigrations
$ python .\manage.py migrate   
```

## Setup 6
Register cerficication to your browser


## Start Server
```
$ cd stduio/webapp/
$ python .\manage.py runsslserver 0.0.0.0:8000 --certificate ahnlab2.com.crt --key ahnlab2.com.key
```

## Execute Plate lookup server 
```
$ cd plateServer
$ run setup.bat
$ cd x64/Release
$ run loaddb.exe
$ run server.exe
```

## Login
We already made user id for team 3
ID : your gmail ID (Exclude @gmail.com)
Password : lge1234

You can change your password.
