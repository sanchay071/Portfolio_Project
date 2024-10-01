import pandas as pd
import os

class DataHandler:
    def __init__(self, data_file='data/projects.csv'):
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            return pd.read_csv(self.data_file)
        else:
            return pd.DataFrame(columns=['title', 'description', 'image_path', 'details'])

    def save_data(self):
        self.data.to_csv(self.data_file, index=False)

    def add_project(self, title, description, image_path, details):
        new_project = {'title': title, 'description': description, 'image_path': image_path, 'details': details}
        self.data = self.data.append(new_project, ignore_index=True)
        self.save_data()

    def get_projects(self):
        return self.data

    def get_project(self, index):
        if index < len(self.data):
            return self.data.iloc[index]
        else:
            return None
