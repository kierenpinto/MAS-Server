# Monash Air Sense Server
This is the server component of the AirSense particulate matter reporting system from Monash University.

## Setup Instructions
These instruction currently pertain to linux. I would recommend using linux, preferrably a debian derivative such as Ubuntu, or Mint for ease of use.
1. To be determined. 
* Instructions need to be updated for a new Amazon Web Services DynamoDB database system.

## Running everything:
Now you're ready to rock and roll. 
Make sure you have run `pipenv install` in the directory to set up the virtual environment. This is important to isolate dependancies in your python application from any others installed on your system. We also need to install our dependancies too! Make sure to jump into the environment (initiate it) by running `pipenv shell`. Finally you can run `python main.py` to get started. 