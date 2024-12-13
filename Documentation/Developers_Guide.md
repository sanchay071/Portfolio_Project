# Create your own Portfolio
## Introduction
This guide details the mvc architecture, functions, classes used and known issues. Current scope of the project and it's future scope is also discussed in detail
## Contents
- [Overview](#overview)
- [User Stories](#user-stories)
- [Specifications](#specifications)
- [Deployment](#deployment)
- [Interaction and Walkthrough](#interaction-and-walkthrough)
- [Jinja Templates](#jinja-templates)
- [OpenSeaDragon and Slick Carousel](#openseadragon-and-slick-carousel)
- [Pitfalls to Avoid](#pitfalls-to-avoid)
- [Known Issues](#known-issues)
- [Future Work and On-going Development](#future-work-and-on-going-development)
## Overview
This Flask-based portfolio project serves as a dynamic platform to showcase the user's works, including research projects, user experience designs, and more. It implements an MVC (Model-View-Controller) pattern where:

Model: The `DataHandler` class manages the project's data, which includes reading from and writing to CSV files (e.g., project data and images).

View: HTML templates in the `templates` folder (`about.html`, `my_works.html`, `project_detail.html`, and `contact.html`) are used for rendering content on the frontend. CSS styles for the pages are located in `static/style.css`.

Controller: The Flask routes in `main.py` handle user interactions and data fetching, processing the business logic and passing data to the views.

The app enables users to view a portfolio of projects, including detailed descriptions and images, and allows for the navigation between different pages (home, about, works, and contact).

## User Stories
### Story #1
As a user (hiring managers, professionals), I would like to view a brief description of
the person, their personally identifiable information
#### Acceptance Criteria
1. Show a brief description of the portfolio’s subject, with text right aligned to the
page.
2. Display a responsive portrait of the subject and left aligned to the document page.
3. Provide a widget showing the professional career as a timeline on the page’s main
body
4. The timeline should be ideally placed below the textual description
### Story #2
As a user, I would like to browse each project in detail so that I can form an
understanding of the project’s research questions and the context.
#### Acceptance Criteria
1. Provide a nav menu, “Projects” or “Works”. Clicking on this menu will take the user
to the projects menu and list all projects as grids.
2. Each project will be shown as cards. Each card will have the following data:
   1. Project image
   2. Project title (20 char max)
   3. Brief description (100 char max)
3. The Card container should have a border shadow and a hover state.
4. The container should be responsive to the viewport of the user.
5. Clicking on the container, a detailed project description is shown on a different
page.
   1. The project page can have many sections with images and descriptions.
   2. Provide a section navigation for the user to navigate to different page
sections
6. The container will have hover animations to indicate the feedback to the user
7. Provide a back button that returns the user to the previous steps. This allows user to
trace their steps back.

### Story #3
The Contact section of the page can have links to socials like linkedin. Optional
idea: Provide a form field for users to send an email.
Provide a forward/back button to shuffle between projects

  
## Specifications
From the initial spec, the following features are implemented:

- About Page: Displays a static description of the user, including a right-aligned text block and a left-aligned portrait. This layout is built using HTML and styled via CSS.
- My Works Page: Showcases a dynamic list of project cards with title, subtitle, and images. Clicking on a card navigates to the detailed project view.
- Project Detail Page: Displays the full details of a project when a card is clicked. Each project includes its title, subtitle, description, and related images.
- Contact Page: Displays contact information.
- Flask Backend: Routes are configured to manage navigation across pages and to handle the project data via the `DataHandler` class.

Features yet to be implemented might include adding a contact form or integrating a more complex backend storage solution (e.g., using a database instead of CSV files).

## Deployment
To ensure a smooth setup and deployment, the following steps should be taken:
1. Environment Setup:
   - Ensure Python 3.10 is installed (can be managed using pyenv or pienv for version management).
   - Create a virtual environment if not already set up:
    ```
    python -m venv .venv
    source .venv/bin/activate  # On Linux/Mac
    .\.venv\Scripts\activate  # On Windows
    ```
    - Install the required dependencies by running:
    ```
    pip install -r requirements.txt
    ```
2. CSV File Configuration:
   - If the `projects.csv` file does not exist, the `DataHandler` will automatically generate it upon the first app run. Make sure that `data_handler.create_initial_data()` works as expected to set up the initial data correctly.

3. Running the Flask App:
   - To run the app, use the following command: `python run_app.py`
   - By default, the Flask app will be in debug mode, which can be turned off by setting `debug=False` in the app.run() method if you deploy to production.

4. Deployment:
   - For production deployment, consider using a WSGI server like ***Gunicorn*** and setting up a reverse proxy (e.g., Nginx).
   - Ensure that any environment-specific configurations (e.g., database paths, server ports) are properly managed through environment variables or a config file.

### PythonAnyWhere

1. Sign Up / Log In: Go to [pythonanywhere](https://www.pythonanywhere.com/) and create an account or log in.
2. Create a New Web App:
   1. Go to the "Web" tab and click "Add a new web app".
   2. Choose "Manual configuration" and select "Flask" for the framework.
3. Open a Bash console and clone your repository `git clone https://github.com/yourusername/yourrepository.git`
4. Configure WSGI: Edit the WSGI configuration file (`/var/www/your_username_pythonanywhere_com_wsgi.py`) to point to your Flask app
   ```
   import sys
   import os
   project_home = '/home/your_username/path_to_your_project'
   if project_home not in sys.path:
   sys.path.append(project_home)
   # Import your Flask app
   from run_app import app as application
   ```
5. Open a console in PythonAnyWhere and Install required packages - `pip install -r /home/your_username/path_to_your_project/requirements.txt`
6. In the `data_handler` class, the file path should reference the path relative to PythonAnyWhere. ![image](https://github.com/user-attachments/assets/0c25df20-e37f-4dc2-ab79-34e3bf403b8b)

7. To pull the latest code from GitHub, use `git pull origin main`
8. Save the code changes, and click reload to launch your website ![image](https://github.com/user-attachments/assets/43be26cd-6628-4285-82a1-df1c666741d6)
     
## Interaction and Walkthrough
1. Homepage (`/`): The user sees a basic introduction (about the user) and navigates through the site using the links in the header.
   - View Involved: `about.html`, `layout.html`.
   - Controller: The route `@app.route('/')` renders `about.html`.
2. My Works Page (`/my_works`): Displays a list of project cards.
    - Each card contains the project image and title. Clicking a card redirects to the respective project detail page.
    - View Involved: `my_works.html`.
    - Controller: The route `@app.route('/my_works')` retrieves all projects via `data_handler.get_projects()` and renders them.
3. Project Detail Page (`/project/<int:project_id>`): Each project has its own detail page.
   - Displays the full project information such as title, subtitle, description, and associated images.
   - View Involved: project_detail.html.
   - Controller: The route `@app.route('/project/<int:project_id>')` fetches the project details using `data_handler.get_project(project_id)` and passes the data to the template.
4. Contact Page (`/contact`): Displays contact details.
   - View Involved: `contact.html`.
   - Controller: The route `@app.route('/contact')` renders the contact page.
  
## Jinja Templates

Each of the templates that extend `layout.html` follows a similar structure for maintaining consistency across the site. They extend the base template and define specific content inside the `block content`:

1. `about.html`:
   - The intro section displays a brief professional overview with images and descriptions.
   - The skills-section uses the Slick Carousel to display icons for various skills.
   - The loop for about_data assumes the data is correctly structured. If the data is missing or incorrectly formatted, it can lead to empty sections or errors when trying to access `section['title']` and `section['description']`.
   - The classes for images are set dynamically based on the loop index. Ensure that the right class (`left` or `right`) is applied correctly. Any misalignment of classes can lead to layout issues.

2. `my_works.html`:
   - The template lists projects in a grid-style card container. Each card links to the project details page.
   - The loop for projects uses `project['image_path']` and `project['title']`, so if any of the project data is missing or the structure is different, it can lead to broken images or incorrect display.
   - The `url_for` function is used for dynamically linking project details, so if there are issues with the Flask routes or project IDs, it could cause 404 errors.

3. `project_detail.html`:
   - This template is responsible for showing the full details of a single project. It includes navigation buttons (Previous and Next) to move between projects and utilizes OpenSeadragon for detailed image viewing.
   - The dynamic generation of section titles (`section_titles`) assumes that the project data contains these keys. If a project does not have all the necessary data for the sections, it may cause missing or incomplete sections to be displayed.
   - The `adjustButtonPosition` function adjusts the position of navigation buttons based on the page scroll. Ensure that the footer element is properly sized and positioned to avoid misalignment of buttons.
   - The hover-to-zoom feature (via OpenSeadragon) relies on images being loaded properly. If there are missing images or broken links, the viewer may not initialize correctly, leading to a broken user experience.

## OpenSeaDragon and Slick Carousel
In this project, OpenSeadragon and Slick Carousel are utilized for interactive image display and smooth navigation through project visuals.

#### OpenSeadragon
OpenSeadragon is integrated for interactive image zooming, allowing the user to zoom in and out on project images for better detail viewing. This is particularly useful when displaying high-resolution images or large project visuals.

Implementation: In the `project_detail.html` template, the OpenSeadragon viewer is used inside the project sections. For each image, a div with the class `openseadragon-viewer` is added, which initializes the zooming feature when the user hovers over an image. The `data-image` attribute points to the image path, which is dynamically loaded using Flask's `url_for` function.

Pitfalls: Ensure that the image paths are correct, especially in cases where the `image_path` might not be available or incorrectly set. OpenSeadragon requires images to be loaded with a specific format or may require optimization for performance on large images. The user should be aware of any browser compatibility issues or performance issues with heavy images, especially on mobile devices.

#### Slick Carousel
Slick Carousel is used for creating a scrollable and interactive set of images or skills, providing a smooth scrolling experience.

Implementation: In the `about.html` template, the `skills-container` uses Slick Carousel to display various skill icons. The carousel is initialized by the carousel class, which the user can navigate by swiping or clicking on arrows.

Pitfalls: Ensure the Slick Carousel is correctly initialized, and the necessary JavaScript libraries are included in the project. One common issue might be a lack of correct initialization or styling, leading to layout issues. Verify that the `slick-carousel` initialization code is running after the page loads and that the required CSS for the carousel is included.

## Pitfalls to Avoid
1. Dynamic Data Handling: The templates assume that all the data passed from the backend (such as `about_data`, `skills_data`, `projects`, etc.) is well-formed and available. If any required data is missing or improperly structured, this can lead to broken sections or visual elements. Ensure that the backend is correctly preparing and validating data before rendering.
2. JavaScript Initialization: Both OpenSeadragon and Slick Carousel rely on JavaScript for proper initialization. Any issues with JavaScript loading, such as missing libraries or incorrect order of execution, can lead to these features not functioning. Make sure that the necessary JavaScript libraries are loaded and that the initialization scripts are running after the page has fully loaded.
3. Layout Issues: Dynamic class assignment for elements like images (left vs. right alignment) and the carousel needs to be thoroughly tested to ensure they are applying correctly under all conditions. Incorrect application of styles might break the layout or cause elements to overlap.
4. Responsive Design: The site needs to be fully responsive across various screen sizes. Issues might arise with elements like the OpenSeadragon viewer or carousel, where large images or elements are not resizing correctly on smaller screens. Test these components on mobile devices to ensure they work smoothly.

## Known Issues
### Minor Issues
1. CSV File Parsing:
   - If the CSV file format changes or becomes corrupted, the DataHandler class may fail to parse it correctly. Consider adding better error handling to validate the format before processing the data.
2. Image Loading:
   - There might be some delay in loading images from the static folder if there are a large number of them. In a production environment, images could be served more efficiently via a CDN or image compression.

### Major Issues
1. Limited Scalability with CSV:
   - Using CSV files for storing project data is not scalable for larger datasets. In a real-world deployment, a database solution (e.g., SQLite, PostgreSQL) would be more efficient for handling large volumes of data.
2. No Form Handling on Contact Page:
   - The contact page currently does not include a form for users to send inquiries. Adding a form (e.g., using Flask-WTF for form handling) would be beneficial.

## Future Work and On-going Development
### Future Work
1. Adding a Contact Form:
   - Implement a form for users to send emails directly from the website. This could be achieved by integrating a service like Flask-Mail for email handling.
2. Database Integration:
   - Replace the CSV data storage with a relational database (e.g., SQLite or PostgreSQL) to improve scalability and allow for more complex queries.
3. Image Carousel on Project Detail Page:
   - Implement an image carousel for projects that have multiple images to improve the user experience.
4. User Authentication:
   - Add user authentication (using Flask-Login) to allow users to log in and manage their portfolio.

### Ongoing Deployment/Development
1. Unit Testing:
   - I'm implementing unit tests to validate the functionality of the DataHandler class and Flask routes. Tools like pytest will be used to test individual components.



