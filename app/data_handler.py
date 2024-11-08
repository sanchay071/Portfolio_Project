import pandas as pd
import os

class DataHandler:
    def __init__(self, projects_file='data/projects.csv', images_file='data/project_images.csv', about_file='data/about.csv'):
        self.projects_file = projects_file
        self.images_file = images_file
        self.about_file = about_file
        self.create_initial_data()
        self.projects_data = self.load_projects_data()  # Ensure this is called after create_initial_data
        self.images_data = self.load_images_data()
        self.about_data = self.load_about_data()

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
    
    def load_about_data(self):
        if os.path.exists(self.about_file):
            return pd.read_csv(self.about_file)
        else:
            # Initialize with empty DataFrame if the file doesn't exist
            return pd.DataFrame(columns=['title', 'description', 'image_path'])

    def save_projects_data(self):
        self.projects_data.to_csv(self.projects_file, index=False)

    def save_images_data(self):
        self.images_data.to_csv(self.images_file, index=False)
        
    def save_about_data(self):
        self.about_data.to_csv(self.about_file, index=False)

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
        
    def add_about(self, title, description, image_path):
        new_section = {'title': title, 'text': description, 'image_path': image_path}
        self.about_data = self.about_data.append(new_section, ignore_index=True)
        self.save_about_data()

    def get_projects(self):
        self.projects_data = self.projects_data.fillna('')
        return self.projects_data.to_dict(orient='records')

    def get_project(self, project_id):
        project = self.projects_data[self.projects_data['id'] == project_id]
        if not project.empty:
            return project.iloc[0]
        else:
            return None
    
    def get_about(self):
        self.about_data = self.about_data.fillna('')
        return self.about_data.to_dict(orient='records')
    
    def get_images_by_project_and_section(self, project_id, section):
        images = self.images_data[(self.images_data['project_id'] == project_id) & (self.images_data['section'] == section)]
        return images['image_path'].tolist() if not images.empty else []
    
    
    def get_section_titles(self):
        return self.projects_data.columns[4:].tolist()  # Assuming the first four columns are not section titles
    
    def get_next_project(self, current_project_id):
        projects = self.get_projects()
        current_index = next((index for (index, d) in enumerate(projects) if d["id"] == current_project_id), None)
        if current_index is not None and current_index + 1 < len(projects):
            return projects[current_index + 1]
        return None

    def get_prev_project(self, current_project_id):
        projects = self.get_projects()
        current_index = next((index for (index, d) in enumerate(projects) if d["id"] == current_project_id), None)
        if current_index is not None and current_index > 0:
            return projects[current_index - 1]
        return None

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
                    'imgs/1_cover.jpg',
                    'imgs/2_cover.jpg',
                    'imgs/3_cover.jpg',
                    'imgs/4_cover.jpg'
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
                'project_id': [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
                'section': ['background', 'artifacts', 'data_glossary', 'research', 'elicitation',
                            'interpretation', 'user_story', 'workflow', 'workflow', 'background', 'artifacts', 'data_glossary', 
                            'research', 'elicitation', 'elicitation','interpretation', 'user_story', 'workflow', 'workflow', 'workflow', 'workflow',
                            'background', 'artifacts', 'artifacts', 'problem_statement', 'data_glossary', 'research', 'research', 'elicitation', 'elicitation',
                            'interpretation', 'interpretation', 'interpretation', 'interpretation', 'interpretation','interpretation', 'user-story',
                            'workflow'],
                'image_path': ['imgs/1_bg.jpg', 'imgs/1_artifact.jpg', 'imgs/1_data.jpg', 'imgs/1_research.jpg', 
                                'imgs/1_elicitation.jpg', 'imgs/1_interpretation.jpg', 'imgs/1_user_story.jpg', 'imgs/1.1_workflow.jpg', 
                                'imgs/1.2_workflow.jpg', 'imgs/2_bg.jpg', 'imgs/2_artifact.jpg', 'imgs/2_data.jpg', 'imgs/2_research.jpg', 
                                'imgs/2.1_elicitation.jpg', 'imgs/2.2_elicitation.jpg', 'imgs/2_interpretation.jpg', 'imgs/2_user_story.jpg', 'imgs/2.1_workflow.jpg', 
                                'imgs/2.2_workflow.jpg', 'imgs/2.3_workflow.jpg', 'imgs/2.4_workflow.jpg', 'imgs/3_bg.jpg', 'imgs/3.1_artifact.jpg', 'imgs/3.2_artifact.jpg',
                                'imgs/3_problem_statement.jpg', 'imgs/3_data.jpg', 'imgs/3.1_research.jpg', 'imgs/3.2_research.jpg', 'imgs/3.1_elicitation.jpg', 'imgs/3.2_elicitation.jpg',
                                'imgs/3.1_interpretation.jpg', 'imgs/3.2_interpretation.jpg', 'imgs/3.3_interpretation.jpg', 'imgs/3.4_interpretation.jpg',
                                'imgs/3.5_interpretation.jpg', 'imgs/3.6_interpretation.jpg', 'imgs/3_user_story.jpg', 'imgs/3_workflow.jpg']
            }
            
            df_images = pd.DataFrame(images_data)
            df_images.to_csv(self.images_file, index=False)
            
         # Initialize about data if not present
        if not os.path.exists(self.about_file):
            about_data = {
                'title': ['About Me'],
                'description': ['This is a description about me and my work.'],
                'image_path': ['imgs/selfie.jpg']
            }
            df_about = pd.DataFrame(about_data)
            df_about.to_csv(self.about_file, index=False)