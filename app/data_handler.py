import pandas as pd
import os

class DataHandler:
    """ DataHandler class for managing project, image, about, and skills data stored in CSV files.
    """
    
    def __init__(self, projects_file='data/projects.csv', images_file='data/project_images.csv', about_file='data/about.csv', skills_file = 'data/skills.csv', tag_file = 'data/tags.csv'):
        """Initialize the DataHandler with file paths for projects, images, about, and skills data.
        
        Parameters:
        projects_file (str): Path to the projects CSV file.
        images_file (str): Path to the project images CSV file.
        about_file (str): Path to the about CSV file.
        skills_file (str): Path to the skills CSV file.
        """
        
        self.projects_file = projects_file
        self.images_file = images_file
        self.about_file = about_file
        self.skills_file = skills_file
        self.tag_file = tag_file
        self.create_initial_data()
        self.projects_data = self.load_projects_data()  # Ensure this is called after create_initial_data
        self.images_data = self.load_images_data()
        self.about_data = self.load_about_data()
        self.skills_data = self.load_skills_data()
        self.tag_data = self.load_tag_data()

    def load_projects_data(self):
        """Load projects data from the CSV file.
        
        Returns:
        pd.DataFrame: DataFrame containing projects data.
        """
        
        if os.path.exists(self.projects_file):
            return pd.read_csv(self.projects_file)
        else:
            # Initialize with empty DataFrame if the file doesn't exist
            return pd.DataFrame(columns=['id', 'title', 'description', 'image_path', 'background', 'artifacts', 'problem_statement', 
                                         'data_glossary', 'research', 'elicitation', 'interpretation', 'user_story', 'workflow', 
                                         'prototype', 'feedback', 'reflection'])

    def load_images_data(self):
        """ Load images data from the CSV file.
        
        Returns:
        pd.DataFrame: DataFrame containing images data.
        """
        
        if os.path.exists(self.images_file):
            return pd.read_csv(self.images_file)
        else:
            # Initialize with empty DataFrame if the file doesn't exist
            return pd.DataFrame(columns=['project_id', 'section', 'image_path'])
    
    def load_about_data(self):
        """Load about data from the CSV file.
        
        Returns:
        pd.DataFrame: DataFrame containing about data.
        """
        
        if os.path.exists(self.about_file):
            return pd.read_csv(self.about_file)
        else:
            # Initialize with empty DataFrame if the file doesn't exist
            return pd.DataFrame(columns=['title', 'description', 'image_path'])
        
    def load_skills_data(self):
        """Load skills data from the CSV file.
        
        Returns:
        pd.DataFrame: DataFrame containing skills data.
        """
        
        if os.path.exists(self.skills_file):
            return pd.read_csv(self.skills_file)
        else:
            # Initialize with empty DataFrame if the file doesn't exist
            return pd.DataFrame(columns=['skills', 'icon'])
        
    def load_tag_data(self):
        if os.path.exists(self.tag_file):
            return pd.read_csv(self.tag_file)
        else:
            # Initialize with empty DataFrame if the file doesn't exist
            return pd.DataFrame(columns=['project_id', 'tag', 'color'])
        

    def save_projects_data(self):
        """Save projects data to the CSV file.
        """
        
        self.projects_data.to_csv(self.projects_file, index=False)

    def save_images_data(self):
        """Save images data to the CSV file.
        """
        
        self.images_data.to_csv(self.images_file, index=False)
        
    def save_about_data(self):
        """Save about data to the CSV file.
        """
        
        self.about_data.to_csv(self.about_file, index=False)
        
    def save_skills_data(self):
        """Save skills data to the CSV file.
        """
        
        self.skills_data.to_csv(self.skills_file, index=False)
        
    def save_tag_data(self):
        """Save skills data to the CSV file.
        """
        
        self.tag_data.to_csv(self.tag_file, index=False)

    def add_project(self, id, title, description, image_path, background, artifacts, problem_statement,
                    data_glossary, research, elicitation, interpretation, user_story, workflow,
                    prototype, feedback, reflection):
        """Add a new project to the projects data.
        
        Parameters:
        id (int): Project ID.
        title (str): Project title.
        description (str): Project description.
        image_path (str): Path to the project's image.
        background (str): Project background text.
        artifacts (str): Project artifacts text.
        problem_statement (str): Project problem statement text.
        data_glossary (str): Project data glossary text.
        research (str): Project research text.
        elicitation (str): Project elicitation text.
        interpretation (str): Project interpretation text.
        user_story (str): Project user story text.
        workflow (str): Project workflow text.
        prototype (str): Project prototype text.
        feedback (str): Project feedback text.
        reflection (str): Project reflection text.
        """
        
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
        """Add a new image to the images data.
        
        Parameters:
        project_id (int): ID of the project to which the image belongs.
        section (str): Section of the project the image is related to.
        image_path (str): Path to the image.
        """
        
        new_image = {'project_id': project_id, 'section': section, 'image_path': image_path}
        self.images_data = self.images_data.append(new_image, ignore_index=True)
        self.save_images_data()
        
    def add_about(self, title, description, image_path):
        """Add a new about section.
        
        Parameters:
        title (str): Title of the about section.
        description (str): Description of the about section.
        image_path (str): Path to the about section's image.
        """
        
        new_section = {'title': title, 'text': description, 'image_path': image_path}
        self.about_data = self.about_data.append(new_section, ignore_index=True)
        self.save_about_data()

    def add_skills(self, skills, icon):
        """Add a new skill to the skills data.
        
        Parameters:
        skills (str): Skills description.
        icon (str): Path to the skill's icon.
        """
        
        new_skill = {'skills': skills, 'icon': icon}
        self.skills_data = self.skills_data.append(new_skill, ignore_index=True)
        self.save_skills_data()
        
    def add_tag(self, project_id, tag, color):
        new_tag = {'project_id': project_id, 'tag': tag, 'color': color}
        self.tag_data = self.tag_data.append(new_tag, ignore_index = True)
        self.save_tag_data()
        
    def get_projects(self):
        """Get all projects data.
        
        Returns:
        list: List of dictionaries containing projects data.
        """
        
        self.projects_data = self.projects_data.fillna('')
        return self.projects_data.to_dict(orient='records')

    def get_project(self, project_id):
        """Get a specific project's data by project ID.
        
        Parameters:
        project_id (int): ID of the project to retrieve.
        
        Returns:
        pd.Series or None: Series containing the project's data or None if not found.
        """

        project = self.projects_data[self.projects_data['id'] == project_id]
    
        if not project.empty:
            project_data = project.iloc[0].to_dict()

            # Fetch and format related tags
            project_tags = self.tag_data[self.tag_data['project_id'] == project_id]
            tags = project_tags[['tag', 'color']].to_dict(orient='records')

            # Attach tags to the project data
            project_data['tags'] = tags
            
            return project_data   
        else:
            return None
    
    def get_about(self):
        """Get about section data.
        
        Returns:
        list: List of dictionaries containing about section data.
        """
        
        self.about_data = self.about_data.fillna('')
        return self.about_data.to_dict(orient='records')
    
    def get_images_by_project_and_section(self, project_id, section):
        """Get images by project ID and section.
        
        Parameters:
        project_id (int): ID of the project to retrieve images for.
        section (str): Section of the project to retrieve images for.
        
        Returns:
        list: List of image paths.
        """
        
        images = self.images_data[(self.images_data['project_id'] == project_id) & (self.images_data['section'] == section)]
        return images['image_path'].tolist() if not images.empty else []
    
    
    def get_section_titles(self):
        """Get titles of the sections in the projects data.
        
        Returns:
        list: List of section titles.
        """
        
        return self.projects_data.columns[4:].tolist()  # Assuming the first four columns are not section titles
    
    def get_next_project(self, current_project_id):
        """Get the next project data by current project ID.
        
        Parameters:
        current_project_id (int): ID of the current project.
        
        Returns:
        dict or None: Dictionary containing the next project's data or None if not found.
        """
        
        projects = self.get_projects()
        current_index = next((index for (index, d) in enumerate(projects) if d["id"] == current_project_id), None)
        if current_index is not None and current_index + 1 < len(projects):
            return projects[current_index + 1]
        return None

    def get_prev_project(self, current_project_id):
        """Get the previous project data by current project ID.
        
        Parameters:
        current_project_id (int): ID of the current project.
        
        Returns:
        dict or None: Dictionary containing the previous project's data or None if not found.
        """
        
        projects = self.get_projects()
        current_index = next((index for (index, d) in enumerate(projects) if d["id"] == current_project_id), None)
        if current_index is not None and current_index > 0:
            return projects[current_index - 1]
        return None
    
    def get_skills(self):
        """Get all skills data.
        
        Returns:
        list: List of dictionaries containing skills data.
        """
        
        self.skills_data = self.skills_data.fillna('')
        return self.skills_data.to_dict(orient='records')
    
    def get_tag(self):
        self.tag_data = self.tag_data.fillna('')
        return self.tag_data.to_dict(orient='records')

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
                'section': ['background', 'artifacts', 'data_glossary', 'research', 'research', 'elicitation',
                            'interpretation', 'user_story', 'workflow', 'workflow', 'background', 'artifacts', 'data_glossary', 
                            'research', 'elicitation', 'elicitation','interpretation', 'user_story', 'workflow', 'workflow', 'workflow', 'workflow', 'workflow', 'workflow',
                            'background', 'background', 'artifacts', 'artifacts', 'problem_statement', 'data_glossary', 'research', 'research', 'elicitation', 'elicitation',
                            'interpretation', 'interpretation', 'interpretation', 'interpretation', 'interpretation','interpretation', 'user_story',
                            'workflow', 'prototype', 'prototype', 'background', 'artifacts', 'artifacts', 'workflow', 'workflow', 'workflow', 'workflow'],
                'image_path': ['imgs/1_bg.jpg', 'imgs/1_artifact.jpg', 'imgs/1_data.jpg', 'imgs/1.1_research.jpg', 'imgs/1.2_research.jpg', 'imgs/1.3_research.jpg', 'imgs/1.4_research.jpg',
                                'imgs/1_elicitation.jpg', 'imgs/1_interpretation.jpg', 'imgs/1_user_story.jpg', 'imgs/1.1_workflow.jpg', 
                                'imgs/1.2_workflow.jpg', 'imgs/2_bg.jpg', 'imgs/2_artifact.jpg', 'imgs/2_data.jpg', 'imgs/2_research.jpg', 
                                'imgs/2.1_elicitation.jpg', 'imgs/2.2_elicitation.jpg', 'imgs/2_interpretation.jpg', 'imgs/2_user_story.jpg', 'imgs/2.1_workflow.jpg', 
                                'imgs/2.2_workflow.jpg', 'imgs/2.3_workflow.jpg', 'imgs/2.4_workflow.jpg', 'imgs/2.5_workflow.jpg', 'imgs/2.6_workflow.jpg', 'imgs/3.1_bg.jpg', 'imgs/3.2_bg.jpg', 'imgs/3.1_artifact.jpg', 'imgs/3.2_artifact.jpg',
                                'imgs/3_problem_statement.jpg', 'imgs/3_data.jpg', 'imgs/3.1_research.jpg', 'imgs/3.2_research.jpg', 'imgs/3.1_elicitation.jpg', 'imgs/3.2_elicitation.jpg',
                                'imgs/3.1_interpretation.jpg', 'imgs/3.2_interpretation.jpg', 'imgs/3.3_interpretation.jpg', 'imgs/3.4_interpretation.jpg',
                                'imgs/3.5_interpretation.jpg', 'imgs/3.6_interpretation.jpg', 'imgs/3_user_story.jpg', 'imgs/3_workflow.jpg', 'imgs/3.1_prototype.jpg', 'imgs/3.2_prototype.jpg', 'imgs/6_bg.jpg',
                                'imgs/6.1_artifact.jpg', 'imgs/6.2_artifact.jpg', 'imgs/6.1_workflow.jpg','imgs/6.2_workflow.jpg','imgs/6.3_workflow.jpg', 'imgs/6.4_workflow.jpg']
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
            
        # Initialize skills data if not present
        if not os.path.exists(self.skills_file):
            skills_data = {
                'skills': ['skills'],
                'icon': ['imgs/figma.svg']
            }
            df_skills = pd.DataFrame(skills_data)
            df_skills.to_csv(self.skills_file, index=False)
            
        if not os.path.exists(self.tag_file):
            tag_data = {
                'project_id': ['1'],
                'tag': ['UX'],
                'color': ['#3776AB']
            }
            df_tag = pd.DataFrame(tag_data)
            df_tag.to_csv(self.tag_file, index=False)