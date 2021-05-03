# Global Portfolio Monitoring pipeline runner


## Project Summary
This repository contains the GPM production scripts for running the Data Collection pipeline. Users can clone this repository to their local computer in order to run the pipeline and update or change GPM reporting suite raw data files. This project will also run data updates in any CI/CD environment once GPM has a data server solition.
    
    
## Open items
This project is in development and unreleased. Once launched, open bugs and new features will be listed here.


## Data Collection Versions
    
- 2019.Q4 - unssported, xlsx source file support needed.
- 2020.Q1 - In development, not tested.
- 2020.Q3 - In development, not tested.
- 2020.Q4 - In development, not tested.
- 2021.Q1 - Supported

## Pipeline User guide

    -Source file location:
        "H:\Reporting\Data Collection\Production\20XX.QX\live_sources"
    
    - User interfaces
        - run_control.ipynb
            A papermill pipeline solution. Each step of the pipeline can be ran manually or sequentially. Your options for each run are explained at the top of this file. This primary runner script can also be called from other programs and run in t background with defaults or passed parameters        
        
        - Pipeline Runner.xlsm
            - "H:\Reporting\_Tools\GitHub\Production Repositories\Pipeline Runner\Pipeline Runner.xlsm"
            - An Excel based GUI where the user can select options such as which BU specific dashboards to run.
        
     - instances folder
         


## Local installation

#### Prequisites
    
    Python- have a base installation of a 64 bit version of python.exe 3.8 or higher.
    Pycharm - These instructions assume you ahve this IDE in order to create virtual environments for you. If you do not want to use PyCharm everything should work as long as you can create a viable project environment.
    

Optional
    Github Desktop - This is not required, but reccomended for regular users of the enterprise github account.

#### Installation walkthrough

1. Create a new virtual environment in your local project folders and name it as you like.
2. Clone this repository into this new environment.
3. Open setup_venv.py in the PyCharm edit window.
4. Follow instructions in the file to setup a project interpreter.
5. Run the script from teh winow or th terminal (instructions in setup_venv.py)
