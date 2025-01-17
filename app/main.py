from flask import render_template
from app import app
from app.data_handler import DataHandler

data_handler = DataHandler()

@app.route('/')
def home():
    """Render the home page with about and skills data.
    
    Returns:
    HTML template for the home page with about_data and skills_data context.
    """
    
    about_data = data_handler.get_about()
    skills_data = data_handler.get_skills()
    return render_template('about.html', about_data=about_data, skills_data = skills_data)

@app.route('/about')
def about():
    """Render the about page with about and skills data.
    
    Returns:
    HTML template for the about page with about_data and skills_data context.
    """
    
    about_data = data_handler.get_about()
    skills_data = data_handler.get_skills()
    return render_template('about.html', about_data=about_data, skills_data = skills_data)

@app.route('/my_works')
def my_works():
    """Render the My Works page with all projects data.
    
    Returns:
    HTML template for the My Works page with projects context.
    """
    
    projects = data_handler.get_projects()


    for project in projects:
        detailed_project = data_handler.get_project(project['id'])
        if detailed_project:
            project['tags'] = detailed_project.get('tags', [])  # Attach tags to the project
    return render_template('my_works.html', projects=projects)

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    """Render the detailed project page for a specific project.
    
    Parameters:
    project_id (int): ID of the project to retrieve details for.
    
    Returns:
    HTML template for the project detail page with project, section_titles, data_handler,
    next_project_id, and prev_project_id context, or a 404 error if the project is not found.
    """
    
    project = data_handler.get_project(project_id)
    section_titles = data_handler.get_section_titles()
    
    # Determine the next project ID
    next_project = data_handler.get_next_project(project_id)
    next_project_id = next_project['id'] if next_project else None
    
    # Determine the previous project ID or if it's the "My Works" page
    prev_project = data_handler.get_prev_project(project_id)
    prev_project_id = prev_project['id'] if prev_project else 'my_works'
    if project is not None:
        return render_template('project_detail.html', project=project, section_titles=section_titles, data_handler=data_handler, next_project_id=next_project_id, prev_project_id=prev_project_id)
    else:
        print("Project not found")
        return "Project not found", 404

@app.route('/contact')
def contact():
    """Render the contact page.
    
    Returns:
    HTML template for the contact page.
    """

    return render_template('contact.html')
