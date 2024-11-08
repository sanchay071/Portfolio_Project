from flask import render_template
from app import app
from app.data_handler import DataHandler

data_handler = DataHandler()

@app.route('/')
def home():
    return render_template('about.html')

@app.route('/about')
def about():
    about_data = data_handler.get_about()
    return render_template('about.html', about_data=about_data)

@app.route('/my_works')
def my_works():
    projects = data_handler.get_projects()
    print(projects)  # Check what projects are being loaded
    return render_template('my_works.html', projects=projects)

@app.route('/project/<int:project_id>')
def project_detail(project_id):
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
    return render_template('contact.html')
