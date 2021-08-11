# SNHU-CS-340-Client-Server-Development
This project contains a Python CRUD module and Plotly Dash application created in Jupyter Notebook. I imported data from the Austin Animal Shelter collection into MongoDB via terminal, created a CRUD module in python using PyMongo as my DB driver. I then created the Dash app that allows users to filter (re-query) their data using preset filters. A DataTable is automatically updated along with a histograph and map.

# Screencast
This short screencast is an example of the application’s functionality. The program itself is first shown to give my identification, and then the dashboard is shown along with the various filter buttons.
https://youtu.be/-76g_xdL9Rk

# aac_crud.py
Allows a connection to the MongoDB and simplifies CRUD functionality

# aac_script.ipynd
Jupyter Notebook script that tests aac_crud.py's functionality

# ProjectTwoDashboard.ipynd
Creates a Plotly Dash web app, which uses Pandas DataFrame, Leaflet, and Dash's Core Components

# CS 340 Final Project
Drew Townsend
08/10/21

# About the Project/Project Title
This project was developed for Grazioso Salvare and performs various tasks on the Austin Animal Shelter database. The dashboard utilizes the aac_crud.py module which enables a connection to the database, and provides Create, Read, Update, and Delete functionality. The dashboard utilizes Plotly’s Dash, which is a tool that offers a way for users to interact with and visualize data with their Data Table. We also utilize Plotly Express for graphs and Leaflet for the map. Lastly, Pandas is utilized to create the DataFrame that holds our data to be manipulated.

# Motivation
This project allows Grazioso Salvare to quickly filter through thousands of rows to assess whether there are dogs available for training. The dashboard also creates a graph of available animals as well as a map for the selected animal’s location. 

# Getting Started
PyMongo is the driver that allows a connection between MongoDB and the Python program. PyMongo is a lightweight tool that provides many functions that simplify the way this program works with MongoDB. To get a local copy running, you must download and import the AAC CRUD module. The program then creates an AnimalShelter object with the correct credentials and makes a “read” call to the AAC database. The query results are saved as a cursor in a Pandas DataFrame. Within the app object, the various html attributes can be edited as required, and the filter buttons may be renamed by changing their labels. The DataTable simply lists all queried rows, which happens when the app is ran. Within the callback section, the filters for the rescue types may be changed as required, by simply adding or removing breeds and other various attributes.

# Installation
You must have access to the MongoDB server with valid credentials. You then need to have Python and Jupyter Notebook installed to run the application. Download the aac_crud.py module and the ProjectTwoDashboard.ipynb script. You may need to edit the directories for aac_crud.py and the logo within the dashboard application.

# Usage
Functionality
To use the program, simply run the application and if everything connects properly, you should see a DataTable containing the AAC database rows. You should then be able to click on the various filter buttons, which will re-query the database with certain attributes. The map and graph should also change based on your filter.

# Contact:
Your name:
Your email: 

