import pandas as pd
import os

class DataHandler:
    def __init__(self, projects_file='data/projects.csv', images_file='data/project_images.csv'):
        self.projects_file = projects_file
        self.images_file = images_file
        self.create_initial_data()
        self.projects_data = self.load_projects_data()  # Ensure this is called after create_initial_data
        self.images_data = self.load_images_data()

    def load_projects_data(self):
        if os.path.exists(self.projects_file):
            return pd.read_csv(self.projects_file)
        else:
            # Initialize with empty DataFrame if the file doesn't exist
            return pd.DataFrame(columns=['id', 'title', 'description', 'image_path', 'background', 'artifacts', 'problem_statement', 
                                         'data_glossary', 'research', 'elicitation', 'interpretation', 'user_story', 'workflow', 
                                         'prototype', 'feedback', 'reflection'])

    def load_images_data(self):
        if os.path.exists(self.images_file):
            return pd.read_csv(self.images_file)
        else:
            # Initialize with empty DataFrame if the file doesn't exist
            return pd.DataFrame(columns=['project_id', 'section', 'image_path'])

    def save_projects_data(self):
        self.projects_data.to_csv(self.projects_file, index=False)

    def save_images_data(self):
        self.images_data.to_csv(self.images_file, index=False)

    def add_project(self, id, title, description, image_path, background, artifacts, problem_statement,
                    data_glossary, research, elicitation, interpretation, user_story, workflow,
                    prototype, feedback, reflection):
        new_project = {
            'id': id, 'title': title, 'description': description, 'image_path': image_path,
            'background': background, 'artifacts': artifacts, 'problem_statement': problem_statement,
            'data_glossary': data_glossary, 'research': research, 'elicitation': elicitation,
            'interpretation': interpretation, 'user_story': user_story, 'workflow': workflow,
            'prototype': prototype, 'feedback': feedback, 'reflection': reflection
        }
        self.projects_data = self.projects_data.append(new_project, ignore_index=True)
        self.save_projects_data()

    def add_image(self, project_id, section, image_path):
        new_image = {'project_id': project_id, 'section': section, 'image_path': image_path}
        self.images_data = self.images_data.append(new_image, ignore_index=True)
        self.save_images_data()

    def get_projects(self):
        return self.projects_data.to_dict(orient='records')

    def get_project(self, project_id):
        project = self.projects_data[self.projects_data['id'] == project_id]
        if not project.empty:
            return project.iloc[0]
        else:
            return None
    
    def get_images_by_project_and_section(self, project_id, section):
        images = self.images_data[(self.images_data['project_id'] == project_id) & (self.images_data['section'] == section)]
        return images['image_path'].tolist() if not images.empty else []
    
    
    def get_section_titles(self):
        return self.projects_data.columns[4:].tolist()  # Assuming the first four columns are not section titles

    def create_initial_data(self):
        # Check if the data file exists and create it with sample data if it doesn't
        if not os.path.exists(self.projects_file):
            projects_data = {
                'id': [1, 2, 3, 4],
                'title': ['Project 1', 'Project 2', 'Project 3', 'Project 4'],
                'description': [
                    'Description of Project 1',
                    'Description of Project 2',
                    'Description of Project 3',
                    'Description of Project 4'
                ],
                'image_path': [
                    'imgs/image1.jpg',
                    'imgs/image2.jpg',
                    'imgs/image3.jpg',
                    'imgs/image4.jpg'
                ],
                'background': [
                    'Background text 1',
                    'Background text 2',
                    'Background text 3',
                    'Background text 4'
                ],
                'artifacts': [
                    'Artifact text 1',
                    'Artifact text 2',
                    'Artifact text 3',
                    'Artifact text 4'
                ],
                'problem_statement': [
                    'Problem statement text 1',
                    'Problem statement text 2',
                    'Problem statement text 3',
                    'Problem statement text 4'
                ],
                'data_glossary': [
                    'Data glossary text 1',
                    'Data glossary text 2',
                    'Data glossary text 3',
                    'Data glossary text 4'
                ],
                'research': [
                    'Research text 1',
                    'Research text 2',
                    'Research text 3',
                    'Research text 4'
                ],
                'elicitation': [
                    'Elicitation text 1',
                    'Elicitation text 2',
                    'Elicitation text 3',
                    'Elicitation text 4'
                ],
                'interpretation': [
                    'Interpretation text 1',
                    'Interpretation text 2',
                    'Interpretation text 3',
                    'Interpretation text 4'
                ],
                'user_story': [
                    'User story text 1',
                    'User story text 2',
                    'User story text 3',
                    'User story text 4'
                ],
                'workflow': [
                    'Workflow text 1',
                    'Workflow text 2',
                    'Workflow text 3',
                    'Workflow text 4'
                ],
                'prototype': [
                    'Prototype text 1',
                    'Prototype text 2',
                    'Prototype text 3',
                    'Prototype text 4'
                ],
                'feedback': [
                    'Feedback text 1',
                    'Feedback text 2',
                    'Feedback text 3',
                    'Feedback text 4'
                ],
                'reflection': [
                    'reflection text 1',
                    'reflection text 2',
                    'reflection text 3',
                    'reflection text 4'
                ]
            }

            df_projects = pd.DataFrame(projects_data)
            df_projects.to_csv(self.projects_file, index=False)

        if not os.path.exists(self.images_file):
            images_data = {
                'project_id': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                'section': ['background', 'artifacts', 'data_glossary', 'research', 'elicitation',
                            'interpretation', 'user_story', 'workflow', 'workflow', 'prototype'],
                'image_path': ['imgs/bg.jpg', 'imgs/artifact.jpg', 'imgs/data.jpg', 'imgs/research.jpg', 
                                'imgs/elicitation.jpg', 'imgs/interpretation.jpg', 'imgs/user_story.jpg', 'imgs/workflow1.jpg', 
                                'imgs/workflow2.jpg', 'imgs/prototyping.jpg']
            }
            df_images = pd.DataFrame(images_data)
            df_images.to_csv(self.images_file, index=False)
