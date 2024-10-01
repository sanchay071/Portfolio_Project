import os
from flask import Flask
from app.data_handler import DataHandler  # Adjust this import based on your folder structure

app = Flask(__name__)

# Create an instance of DataHandler and initialize the CSV file
data_handler = DataHandler()

# Create the initial data if the CSV file does not exist
data_handler.create_initial_data()

# Import your main app logic (routes, etc.)
from app import main  # Adjust this import based on your folder structure

if __name__ == '__main__':
    app.run(debug=True)
