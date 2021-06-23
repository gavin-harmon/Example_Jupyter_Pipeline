# Global Portfolio Monitoring Data Collection Pipeline
## Project Summary
This repository contains the GPM production scripts for running the Data Collection pipeline. Users can clone this repository to their local computer in order to run the pipeline and update or change GPM reporting suite raw data files. This project will also run data updates in any CI/CD environment once GPM has a data server solition.
    
## Data Collection Versions
    
- 2019.Q4 - Supported, not tested
- 2020.Q1 - Supported, not tested.
- 2020.Q3 - Supported, not tested.
- 2020.Q4 - Supported, not tested.
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

#### Jupyter
	Testing is needed of what the minimal local setup is.

###### Optional
Python - have a base installation of a 64 bit version of python.exe 3.8 or higher.
PyCharm - These instructions assume you have this IDE in order to create virtual environments for you. If you do not want to use PyCharm everything should work as long as you can create a viable project environment.
    
###### Optional
Github Desktop - This is not required, but reccomended for regular users of the enterprise github account.

###### Minimal Installation Setup
1. Ensure Jupyter can be launched from your desktop.
2. Run 'Jupyter Launch.bat' in this folder.

###### Developer Installation walkthrough

1. Create a new virtual environment in your local project folders and name it as you like.
2. Clone this repository into this new environment.
3. Open setup_venv.py in the PyCharm edit window.
4. Follow instructions in the file to setup a project interpreter.
5. Run the script from teh winow or th terminal (instructions in setup_venv.py)

    
## Open items
This project is in development and unreleased. Once launched, open bugs and new features will be listed here.

Last Touchpoint:
        
        update timestamps - completed
            add links in log file -  Open
        
        Make summary report  - completed
        
        - 1 xls file,
            - View 1 
                All BUs and rolled up - Comparison Fin View vs UW view.
                All comments from BUs
            - View 2
                Euro conversion match


Coming soon:
1. Pre-pipeline prep phase:
    - German Allocations
    - Swiss Transformations
    - Portuguese Transformation

<<<<<<< HEAD
2. Euro checks.

3. Connect xlsx pipeline runner

4. Create Travel Global Report.

5. Create selected BU local dashboards.
=======
2. Connect xlsx pipeline runner

3. Create Travel Global Report.

4. Create selected BU local dashboards.

5. Euro checks.
>>>>>>> 16739ffd78c82b19886099d0350318838d00c029

6. Optimize run logic

Recently completed - 

<<<<<<< HEAD

 Finance reporting in /reporting
 
 support for knitting

 process for json to parquet

 added to network and changed the instance archive process to be easier to navigate.

 Read data, make csv. - complete

=======
 Read data, make csv. - complete


>>>>>>> 16739ffd78c82b19886099d0350318838d00c029
 Make final data files.
    - Read temp file from previous step.
    - Perform conversion to Euro with checks. << Checks added to coming soon
    - Create local currency data file.
    - Create Euro currency data file. - Archive previous

 Python data transformations.
    - Read csv from previous step.
    - Make required transformations in Python.
    - Output to a temp file.

 R data transformations.
    - Read temp file from previous step.
    - Make all R Transformations
    - Overwrite to temp file. 
    
<<<<<<< HEAD
 
 
=======
>>>>>>> 16739ffd78c82b19886099d0350318838d00c029
