# Predicting Rainfall Using Machine Learning
## **Data source** is [here](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillUp/labs/ML-FinalAssignment/Weather_Data.csv)

## **Approach:**
* ### Project templates creation -
    create a folder structure for this project using **template.py** file.
* ### Reqirement installation & project set up -
    * create a virtual environment- 
        ```conda create -n mlproject python=3.8 -y ```  
        ``` conda activate mlproject ```
    * for requirement installation, 
        ``` pip install -r requirement.txt ```
* ### Notebook experiment
    - add jupyter notebook file in **research** directory
* ### Project Utility
    * set logging constructor file [here](./src/Predicting_rainfall_project/__init__.py) and the log file is [here](./log/running_log.log) 
    * Exception
    * Set Utility module in the [file](./src/Predicting_rainfall_project/utils/common.py)

* ### Workflows
    1. update config.yaml
    2. update schema.yaml
    3. update params.yaml
    4. update the entity 
    5. update the configuration manager in src config
    6. update the components
    7. update the pipeline
    8. update the main.py
    9. update the app.py

