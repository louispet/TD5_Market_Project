# TD5_Market_Project

Export dependencies with pip freeze >requirements.txt

this project is carried out as part of the finance course by Alexandra Nebout and Louis Peters.

You can find 6 files. 

This file, README.md explain how we had built this project.

requirements.txt contains the dependencies. It will be used to reload the dependencies in a new virtualenv.

the gitignore file specifies intentionally untracked files that Git should ignore. 
Files already tracked by Git are not affected. 

run.sh create the virtualenv if it does not exists, and load the dependencies from the requirements.txt. After that, it activate the virtualenv if it exists and run the main.py Python.

main.py is the main program 

book.py contains the Book and Order objects to obtain a result log showing for each insert call.
More particulary :
 the insert action details,
 the executed orders if any,
 the book state after insertion and execution.


