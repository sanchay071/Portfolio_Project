from flask import render_template
from app import app
from app.data_handler import DataHandler

data_handler = DataHandler()

@app.route('/')
def home():
    return render_template('about.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/my_works')
def my_works():
    projects = data_handler.get_projects()
    print(projects)  # Check what projects are being loaded
    return render_template('my_works.html', projects=projects)

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    project = data_handler.get_project(project_id)
    if project is not None:
        return render_template('project_detail.html', project=project)
    else:
        print("Project not found")
        return "Project not found", 404

@app.route('/contact')
def contact():
    return render_template('contact.html')
