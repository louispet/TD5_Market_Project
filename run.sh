
#!/bin/bash

if [[ ! -d .env ]]
then
	virtualenv -p python3 .env
fi
# Install any required pip packages
[ -r "$(pwd)/requirements.txt" ] && pip install --requirement "$(pwd)/requirements.txt"

if [[ -d .env ]]
then
	source /home/louis/Project/.env/bin/activate
	# Install any required pip packages
	[ -r "$(pwd)/requirements.txt" ] && pip install --requirement "$(pwd)/requirements.txt"
	python3 main.py
	
fi



