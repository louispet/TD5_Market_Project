# TD5_Market_Project

this project is carried out as part of the finance course by Alexandra Nebout and Louis Peters.

__You can find 6 files__

## Dependencies and project

This file,__ README.md__ explain how we had built this project.

__requirements.txt__ contains the dependencies. It will be used to reload the dependencies in a new virtualenv.

__the gitignore__ file specifies intentionally untracked files that Git should ignore.
Files already tracked by Git are not affected.

Export dependencies with pip freeze >requirements.txt
 

## Bash file 

__run.sh__ create the virtualenv if it does not exists, and load the dependencies from the requirements.txt. After that, it activate the virtualenv if it exists and run the main.py Python.

## Python files

__main.py__ is the main program 

__book.py__ contains the Book and Order objects to obtain a result log showing for each insert call.
More particulary :
* the insert action details.
* the executed orders if any.
* the book state after insertion and execution.


