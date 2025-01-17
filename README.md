# Create your own Portfolio
## Introduction
Welcome! This guide details the steps to create a portfolio website and the procedures to deploy them. The website is built using Python, Flask framework, and Pandas Dataframe. 
## Contents
- [Overview](#overview)
- [Database Setup and Folder Structure](#database-setup-and-folder-structure)
- [Prerequisites](#prerequisites)
- [Running the App](#running-the-app)
  
## Overview
The end-user of the website can be hiring managers, managers, experts in any field. The portfolio showcases your skills, projects, your personal journey. The navigation is divided into following:

- About - This section provides a brief decription about you and your journey. This can be snapshot of what to expect by skimming this application.
- My Works - This page details all the work and personal projects as in a card layout. Upong clicking each card, the viewer is taken to detailed section of each project. Hence project detail page is accessed via My Works. 
- Contact - This page provides a way for the viewer to contact via Linkedin and also connects your GitHub profile.

The code has been implemented in such a way that sections in About page and project detail page can be modified, and updated. New projects can be added as per your need and provides flexibility for CRUD operations. Here is a step-by-step by plan

- Project Structure: Set up the project folder structure.
- Initialize Flask App: Create a basic Flask app.
- Define Routes: Set up routes for the About, My Works, and Contact sections.
- Simulate Input: Hardcode project data and store it in a CSV file.
- Load and Display Data: Load the data from the CSV and display it on the My Works page.
- Template Structure: Create basic HTML templates for each page.

## Database Setup and Folder Structure
CSV files are used as the database for this project. These files should be placed in the `data/` folder and should be set up as follows with the following column headers:

### about.csv
**column header/keys**: `title`, `description`, `image_path`

### projects.csv
**column header/keys**: `id`, `title`, `description`, `image_path`, `section_titles`
Any number of section titles can be added to the csv file

### project_images.csv
**column header/keys**: `project_id`, `section`, `image_path`

### skills.csv
**column header/keys**: `skills`, `icon`

Whenever a row is updated, the results wont be dynamically reflected in the front-end. You need to restart the server to pull the latest changes. If you foresee that your portfolio will become large enough I'd recommend moving to SQLite or any database of your choice. 

- `app/`: Contains the core application files
- `templates/`: Holds the HTML templates for different pages
- `static/`: Stores CSS and images
- `data/`: Contains CSV files used as the database
- `data_handler.py` - This module serves as the **model** in the model-view-controller architecture. This file contains all the data handling operations to and from the database.
- Templates - The templates folder contains the `about.html`, `layout.html`, `my_works.html`, `contact.html`. `layout.html` serves as the base the template from which child templates extended using Jinja syntax.
- `__init.py__` - The init.py file is used to initialize your Flask application and set up the application package. This file is executed when the package is imported, and it typically contains the configuration settings and initial setup for the Flask app. This is where you create your Flask app instance and include any initial configuration or blueprints.
- `main.py` - This python files serves as the **controller** in the model-view-controller architecture. This file will contain the route definitions and updates the model and view functions for your Flask application.
- `run_app.py` - This file is the starter script that runs your Flask application. It imports the app instance from the app package and calls app.run()
- `skills.csv` defines the routes for .svg files. These files should be placed in the `imgs` folder as well.
-  Place all your project images in the `imgs` folder.![image](https://github.com/user-attachments/assets/868337ba-ffc3-4a40-a349-5d6cd36f251e)
 
## Prerequisites
I'd recommend either Visual Studio Code or PyCharm for IDEs. 

- Before proceeding to install dependencies, required csv files can be created inside the data folder. Or you can allow the `data_handler.py` to create the neccessary files for you. I have used `about.csv`, `projects.csv`, `projects_images.csv`, `skills.csv`. These files are read as **Dataframes** and are converted to **Dictonaries** to be operated by Jinja.
- The column headers (dictonary keys) in each .csv file is predefined and it can be updated as per your portfolio need. The naming conventions can be updated and deleted based on the type of portfolio you'd want and this needs to be updated in the `data_handler.py` module as well. But this is needed only if you want the data_handler class to create a database for you. Otherwise project sections, and subsections can be created, deleted, updated on the go. 
- Clone the project and open your command terminal or bash
- Set the current directory as your project directory and install all packages using `pip install -r requirements.txt`
- If you want to deploy your project in PythonAnyWhere, you can downgrade the python version to 3.10. This needs to be updated in the requirements.txt as well. PythonAnyWhere supports python versions upto 3.10. Refer to the image for an overview of the dependencies I have used

  ![image](https://github.com/user-attachments/assets/01ebb23d-ec5d-4f21-b627-4300199a90ee)

## Running the App

1. Clone the Project: Clone the project from your repository and navigate to the project directory.

`git clone https://github.com/yourusername/Portfolio_Project.git`

2. Install Dependencies: Install all necessary packages.

`pip install -r requirements.txt`

3. Run the Application: Execute the `run_app.py` script to start your Flask application.

`app/run_app.py`

4. Access the Website: Open a web browser and go to `http://127.0.0.1:5000/` to see your portfolio website in action.





