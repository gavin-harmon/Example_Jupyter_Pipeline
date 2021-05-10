# Global Portfolio Monitoring pipeline runner
## Project Summary
This repository contains the GPM production scripts for running the Data Collection pipeline. Users can clone this repository to their local computer in order to run the pipeline and update or change GPM reporting suite raw data files. This project will also run data updates in any CI/CD environment once GPM has a data server solition.
    
## Data Collection Versions
    
- 2019.Q4 - unsupported, xlsx source file support needed.
- 2020.Q1 - In development, not tested.
- 2020.Q3 - In development, not tested.
- 2020.Q4 - In development, not tested.
- 2021.Q1 - Supported.

## Pipeline User guide

#### Source file location:
  
  "H:\Reporting\Data Collection\Production\20XX.QX\live_sources"

#### User interfaces

- run_control.ipynb 
  
    A papermill pipeline solution.

    Execute "jupyter notebook" from the terminal, while in the local version of the PyCharm project.
  
    Each step of the pipeline can be ran manually or executed sequentially as a notebook or a script.
  
    Your options for each run are explained at the top of this file. 
    
    This primary execution script can also be called from other programs and run in the background with defaults or passed parameters
  

- Pipeline Runner.xlsm

    "H:\Reporting\_Tools\GitHub\Production Repositories\Pipeline Runner\Pipeline Runner.xlsm"
   
    An Excel based GUI where the user can select options such as which BU specific dashboards to run.
        

#### Instances folder
  
  "H:\Reporting\Data Collection\Production\20XX.QX\live_sources" 
  
  Full notebook records for each time the process is run. Here you can see the code that was run and also summary output. 
                
#### Current Process (In development):

1. Pre-pipeline prep phase:
    - German Allocations
    - Swiss Transformations
    - Portuguese Transformation
    
2. Read data, make csv.
   - Appends all sources to one data frame and exports to a csv.
    - Summary info available in notebook and archived csvs in data collection folder.
3. Python data transformations.
    - Read csv from previous step.
    - Make required transformations in Python.
    - Output to a temp file.
4. R data transformations.
    - Read temp file from previous step.
    - Make all R Transformations
    - Overwrite to temp file.
5. Make final data files.
    - Read temp file from previous step.
    - Perform conversion to Euro with checks.
    - Create local currency data file.
    - Create Euro currency data file. - Archive previous
6. Create Travel Global Report.
7. Create selected BU local dashboards.

## Local installation

#### Prequisites

###### Required
Python - have a base installation of a 64 bit version of python.exe 3.8 or higher.
PyCharm - These instructions assume you ahve this IDE in order to create virtual environments for you. If you do not want to use PyCharm everything should work as long as you can create a viable project environment.
    
###### Optional
Github Desktop - This is not required, but reccomended for regular users of the enterprise github account.

#### Installation walkthrough

1. Create a new virtual environment in your local project folders and name it as you like.
2. Clone this repository into this new environment.
3. Open setup_venv.py in the PyCharm edit window.
4. Follow instructions in the file to setup a project interpreter.
5. Run the script from teh winow or th terminal (instructions in setup_venv.py)

    
## Open items
This project is in development and unreleased. Once launched, open bugs and new features will be listed here.

immediate items:
        
        update timestamps - done
            add link in file though
        
        Make summary report
        
        - 1 xls file,
            - View 1 
                All BUs and rolled up - Comparison Fin View vs UW view.
                All comments from BUs
            - View 2
                Euro conversion match

Connect xlsx pipeline runner

Coming soon
1. Pre-pipeline prep phase:
    - German Allocations
    - Swiss Transformations
    - Portuguese Transformation

In progress    
2. Read data, make csv. - complete

In progress   
3. Python data transformations.
    - Read csv from previous step.
    - Make required transformations in Python.
    - Output to a temp file.
    
Coming soon
4. R data transformations.
    - Read temp file from previous step.
    - Make all R Transformations
    - Overwrite to temp file.
    
Coming soon
5. Make final data files.
    - Read temp file from previous step.
    - Perform conversion to Euro with checks.
    - Create local currency data file.
    - Create Euro currency data file. - Archive previous
    
Coming soon
6. Create Travel Global Report.

Coming soon
7. Create selected BU local dashboards.
