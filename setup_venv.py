"""
This script is meant to guide a user through making a new blank jupytr environment ready to run the GPM pipeline.

These instructions assume you are using the PyCharm IDE.

To start, create a new venv, add this file, and open it in the editor in order to add an interpretter.

Add a project interpreter of 3.8 or higher. At this time, 3.9 is preferred. Make sure it is not a 32bit interpreter,
that will not work.

Usable 64-bit interpreters will have names and paths like: Python\python.exe

Unusable 32-bit interpreters will have names and paths like: Python\Python38-32\python.exe

You can run the script from the editor or from the terminal.

Note, go off VPN to install packages.

Terminal instructions. Assuming you are in the working dir of this script.

enter : "python setup_venv.py"

"""
import os
import sys

resetdir = os.getcwd()
# Set variable as current working directory.
# When the process is finished installing packages in the executable directory, this will be called to return the
# variable to the user's previous working directory

os.chdir(os.path.dirname(sys.executable))
# find the project interpreter, make the path the working directory.

os.system("pip install jupyter")
#install jupyter
os.system("pip install papermill")

os.chdir(resetdir)

path = os.getcwd()

print(path)
# return working directory to starting dir.



