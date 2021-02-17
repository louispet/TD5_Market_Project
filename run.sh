
#!/bin/bash

#Create the virtualenv if it does not exists
if [[ ! -d .env ]]
then
	virtualenv -p python3 .env
fi

#Activate the virtualenv if it exists and load the dependencies from the requirements.txt.
if [[ -d .env ]]
then
	source "$(pwd)/.env/bin/activate"
	# Install any required pip packages
	[ -r "$(pwd)/requirements.txt" ] && pip install --requirement "$(pwd)/requirements.txt"
	python3 "$(pwd)/main.py"
	
fi


