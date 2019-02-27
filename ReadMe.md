# Monash Air Sense Server
This is the server component of the AirSense particulate matter reporting system from Monash University.
##
Information about the project can be found on the [wiki](wiki), however continue reading for setup instructions.
## Setup Instructions
These instruction currently pertain to linux. I would recommend using linux, preferrably a debian derivative such as Ubuntu, or Mint for ease of use.

### Overview
There are several different configuration options available. Multiple databases can be used to store particulate matter readings. These have arisen due to experimentation and ultimately flexibility in the future. The first is DynamoDB, and the latter is MYSQL. Plans exist to implement time series databases such as openTSDB and Graphite. Ultimately this software should be able to connect to Grafana for more comprehensive graphing and analytics. 
#### DynamoDB
* Instructions need to be updated for a new Amazon Web Services DynamoDB database system.
1. In order to connect and authenticate with DynamoDB, the AWS CLI (command line interface) is required. To get this use:
    ```
    pip3 install awscli --upgrade --user
    ```
2. You need to add your credentials to the AWS CLI. To do this:
    * Use aws configure:
        ``` 
        aws configure 
        ```
    * Then follow the prompts. Further instruction can be found [here](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html)

#### MYSQL
* Instructions need to be updated for a new MYSQL database system.

### Setting up python environment:
1. Python 3.6 is required, however, this may not be the specific version you have. In order to work around this, `pyenv` is the tool required. Pyenv allows multiple versions of python to exist on the same computer, and works with pipenv. 
    * To install pyenv, run: 
        ```
        $ curl https://pyenv.run | bash 
        ``` 
    * [Documentation for pyenv](https://github.com/pyenv/pyenv-installer).
<br/>
2. Ensure pipenv is installed.
    * Use:
        ```
        pip install --user pipenv
        ```
    * This is important to isolate dependancies in your python application from any others installed on your system.
    * [General Documentation for pipenv](https://pipenv.readthedocs.io/en/latest/#)
        * [Installation](https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv)
3. Clone the repository
4. Once in the "./MAS-Server" directory, run `pipenv install` to set up the virtual environment. It installs all python dependancies for MAS-Server in an isolated container. Make sure to jump into the environment (initiate it) by running `pipenv shell`. 
<br/>

~~Finally you can run `python main.py` to get started.~~ Read the wiki's [Post Installation](wiki/Post-Installation---Getting-up-and-running) steps.Now you're ready to rock and roll. 