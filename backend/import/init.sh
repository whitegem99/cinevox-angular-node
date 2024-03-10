#! /bin/bash

apt-get update \
    && apt-get install python3-pip -y \
    && pip3 install mysql-connector-python \
    && pip3 install requests \
    && pip3 install python-slugify \
    && pip3 install python-dotenv

echo ===================================================================================================================================================================================================
echo -e "Start init.sh at :" && date
echo -e "___________________________________________________\n"

# cd /var/www/html/
echo -e "Start python script\n"
echo
python3 import.py
echo -e "___________________________________________________\n"
echo End
echo ===================================================================================================================================================================================================
