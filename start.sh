#!/bin/bash

      ##                         ##   ######                     #####           
  ### ##   #####     #####   ### ##  #######   #####    #####   #######   #####  
 #### ##  #######   ######  #### ##  ##       #######  #######  ##   ##  ####### 
 ##   ##  ##  ###  ###  ##  ##   ##  ######   ##   ##  ##  ###  ## ####  ##   ## 
 ##   ##  ##  ##   ##   ##  ##   ##  ##   ##  ##       ##  ##   ## ###   ##   ## 
 ######   ####     #######  ######   #######  ##       ####     ##       ####### 
  #####    #####    #####    #####    #####   ##        #####   ##        #####  

  
                                            #WaktuSolatv1 Project By Ikmal 2023   


# Exit early on errors
set -eu

# Python buffers stdout. Without this, you won't see what you "print" in the Activity Logs
export PYTHONUNBUFFERED=true

# Install Python 3 virtual env
VIRTUALENV=.data/venv

if [ ! -d $VIRTUALENV ]; then
  python3 -m venv $VIRTUALENV
fi

if [ ! -f $VIRTUALENV/bin/pip ]; then
  curl --silent --show-error --retry 5 https://bootstrap.pypa.io/get-pip.py | $VIRTUALENV/bin/python
fi

# Install the requirements
$VIRTUALENV/bin/pip install urllib3==1.26.6
# You can install all the package with this as well $VIRTUALENV/bin/pip3 install -r requirements.txt

# Run a glorious Python 3 server
$VIRTUALENV/bin/python3 app.py