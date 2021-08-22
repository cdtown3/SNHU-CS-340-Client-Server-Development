# Author: Drew Townsend
# Date: 08/22/21

# SNHU-CS-340-Client-Server-Development
This project contains a Python CRUD module and Plotly Dash application created in Jupyter Notebook. I imported data from the Austin Animal Shelter collection into MongoDB via terminal, created a CRUD module in python using PyMongo as my DB driver. I then created the Dash app that allows users to filter (re-query) their data using preset filters. A DataTable is automatically updated along with a histograph and map.

# How do you write programs that are maintainable, readable, and adaptable? Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?
First and foremost, adding comments throughout my code ensures I and others can quickly understand what each variable holds and what each function does. This increases readability. I then try to not copy code where it isn't necessary. I prevent this by creating functions to increase maintainability and adaptability. Lastly, I try to prevent unnecessary dependencies so that when I update code in one area other functions aren't broken. The CRUD module is lightweight, and can be implemented easily in any program that requires access to the Austin Animal Shelter DB.

# How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?
Although the textbook was helpful, I relied heavily on the documentation given by MongoDB, Leaflet, and Plotly. As a computer scientist, I had to gather the requirements from the company and plan out my software logistically. When having access to so much data, automating the collection of documents is a necessity.

# What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?
To put it simply, computer scientists work to solve real-world issues in the most efficient manner, by planning and designing software. In this specific case, instead of requiring someone to search row by row for the best dogs for the job, I was able to implement a user-friendly dashboard that got all of that data and more in a matter of seconds. This also helps to prevent errors, like overlooking dogs that may have worked for the role.
