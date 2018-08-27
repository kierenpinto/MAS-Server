# Monash Air Sense Server
This is the server component of the AirSense particulate matter reporting system from Monash University.

## Setup Instructions
These instruction currently pertain to linux. I would recommend using linux, preferrably a debian derivative such as Ubuntu, or Mint for ease of use.
1. Install MySQL Server. On Ubuntu/Mint this is:
    ```
    sudo apt install mysql-server
    ```
2. Create an account for MySQL:
    ```
    sudo mysql
    > CREATE USER 'AirSense'@'localhost' identified by 'monashepa';
    ```
3. Create a new database:
    ```
    CREATE DATABASE emi;
    ```
4. Give the new user account permissions for this database:
    ```
    GRANT ALL ON emi.* TO 'AirSense'@'localhost';
    ```
Please note if you use different credentials during setup, please change them in mysql.py
Soon we will configure for environment variables. 
## Running everything:
Now you're ready to rock and roll. 
Make sure you have run `pipenv install` in the directory to set up the virtual environment. This is important to isolate dependancies in your python application from any others installed on your system. We also need to install our dependancies too! Make sure to jump into the environment (initiate it) by running `pipenv shell`. Finally you can run `python main.py` to get started. 