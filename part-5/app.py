"""
Part 5: Mini Project - Personal Website with Flask
===================================================
A complete personal website using everything learned in Parts 1-4.

How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Open browser: http://localhost:5000
"""

from flask import Flask, render_template


app = Flask(__name__)

# =============================================================================
# YOUR DATA - Customize this section with your own information!
# =============================================================================

PERSONAL_INFO = {
    'name': 'Dipika Nagargoje',
    'title': 'Computer Engineering Student',
    'bio': 'Third year computer engineering student to passionate about learning ,APIs,Flask,Deep learing.',
    'email': 'nagargojedipika@gmail.com',
    'github': 'https://github.com/nagargojedipika-a11y',
    'linkedin': 'https://www.linkedin.com/in/dipikanagargoje-3548a4328',
}

SKILLS = [
    {'name': 'Python', 'level': 80},
    {'name': 'HTML/CSS', 'level': 75},
    {'name': 'Java', 'level': 70},
    {'name': 'C++', 'level': 65},
    {'name': 'SQL', 'level': 70},
]

PROJECTS = [
    {'id': 1, 'name': 'Personal Website', 'description': 'A Flask-powered personal portfolio website.', 'tech': ['Python', 'Flask', 'HTML', 'CSS'], 'status': 'Completed'},
    {'id': 2, 'name': 'Smart Text Editor', 'description': 'some modifications are doing in simple text editor.', 'tech': ['Python', 'Flask','APIs'], 'status': 'Completed'},
    {'id': 3, 'name': 'Student Management System', 'description': 'A Student Management System (SMS) is a software application designed to store, manage, and retrieve student information efficiently..', 'tech': ['Python', 'tkinker', 'SQL'], 'status': 'Completed'},
]

# ✅ BLOG DATA (Exercise 5.2)
BLOG_POSTS = [
    {
        'id': 1,
        'title': 'Getting Started with Flask',
        'content': 'Flask is a lightweight Python web framework that is easy to learn.',
        'date': '2026-01-05'
    },
    {
        'id': 2,
        'title': 'Why Learn APIs?',
        'content': 'APIs allow applications to communicate and share data efficiently.',
        'date': '2026-01-06'
    },
    {
        'id': 3,
        'title': 'My Journey in Computer Engineering',
        'content': 'Sharing my learning experience and growth as a computer engineering student.',
        'date': '2026-01-07'
    },
]


# =============================================================================
# ROUTES
# =============================================================================

@app.route('/')
def home():
    return render_template('index.html', info=PERSONAL_INFO)


@app.route('/about')
def about():
    return render_template('about.html', info=PERSONAL_INFO, skills=SKILLS)


@app.route('/projects')
def projects():
    return render_template('projects.html', info=PERSONAL_INFO, projects=PROJECTS)


@app.route('/project/<int:project_id>')  # Dynamic route for individual project
def project_detail(project_id):
    project = None
    for p in PROJECTS:
        if p['id'] == project_id:
            project = p
            break
    return render_template('project_detail.html', info=PERSONAL_INFO, project=project, project_id=project_id)

# ✅ BLOG LIST PAGE
@app.route('/blog')
def blog():
    return render_template('blog.html', info=PERSONAL_INFO, posts=BLOG_POSTS)


# ✅ SINGLE BLOG POST PAGE
@app.route('/blog/<int:post_id>')
def blog_detail(post_id):
    post = next((p for p in BLOG_POSTS if p['id'] == post_id), None)
    return render_template('blog_detail.html', info=PERSONAL_INFO, post=post)

# ✅ SKILL DETAIL PAGE
@app.route('/skill/<skill_name>')
def skill_detail(skill_name):
    # Find projects that use the given skill
    matched_projects = []

    for project in PROJECTS:
        if skill_name.lower() in [tech.lower() for tech in project['tech']]:
            matched_projects.append(project)

    return render_template(
        'skill_detail.html',
        info=PERSONAL_INFO,
        skill_name=skill_name,
        projects=matched_projects
    )


@app.route('/contact')
def contact():
    return render_template('contact.html', info=PERSONAL_INFO)


if __name__ == '__main__':
    app.run(debug=True)


# =============================================================================
# PROJECT STRUCTURE:
# =============================================================================
#
# part-5/
# ├── app.py              <- You are here
# ├── static/
# │   └── style.css       <- CSS styles
# └── templates/
#     ├── base.html       <- Base template (inherited by all pages)
#     ├── index.html      <- Home page
#     ├── about.html      <- About page
#     ├── projects.html   <- Projects list
#     ├── project_detail.html <- Single project view
#     └── contact.html    <- Contact page
#
# =============================================================================

# =============================================================================
# EXERCISES:
# =============================================================================
#
# Exercise 5.1: Personalize your website
#   - Update PERSONAL_INFO with your real information
#   - Add your actual skills and projects
#
# Exercise 5.2: Add a new page
#   - Create a /blog route
#   - Add blog posts data structure
#   - Create blog.html template
#
# Exercise 5.3: Enhance the styling
#   - Modify static/style.css
#   - Add your own color scheme
#   - Make it responsive for mobile
#
# Exercise 5.4: Add more dynamic features
#   - Create a /skill/<skill_name> route
#   - Show projects that use that skill
#
# =============================================================================
