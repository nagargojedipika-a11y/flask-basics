"""
Part 6: Homework - Personal To-Do List App
==========================================
How to Run:
1. python app.py
2. Open browser: http://localhost:5000
"""

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ===============================
# SAMPLE DATA (LIST)
# ===============================
TASKS = [
    {'id': 1, 'title': 'Learn Flask', 'status': 'Completed', 'priority': 'High'},
    {'id': 2, 'title': 'Build To-Do App', 'status': 'Completed', 'priority': 'Medium'},
    {'id': 3, 'title': 'Push to GitHub', 'status': 'Pending', 'priority': 'Low'},
]

# ===============================
# HOME - SHOW TASKS
# ===============================
@app.route('/')
def home():
    return render_template('index.html', tasks=TASKS)

# ===============================
# ADD TASK
# ===============================
@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        new_id = TASKS[-1]['id'] + 1 if TASKS else 1

        TASKS.append({
            'id': new_id,
            'title': request.form['title'],
            'status': request.form['status'],
            'priority': request.form['priority']
        })

        return redirect(url_for('home'))

    return render_template('add.html')

# ===============================
# TASK DETAILS
# ===============================
@app.route('/task/<int:id>')
def task_detail(id):
    task = next((t for t in TASKS if t['id'] == id), None)
    return render_template('task.html', task=task)

# ===============================
# EDIT TASK (LIST BASED)
# ===============================
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_task(id):
    task = next((t for t in TASKS if t['id'] == id), None)

    if not task:
        return redirect(url_for('home'))

    if request.method == 'POST':
        task['title'] = request.form['title']
        task['status'] = request.form['status']
        task['priority'] = request.form['priority']
        return redirect(url_for('home'))

    return render_template('edit_task.html', task=task)

# ===============================
# DELETE TASK (LIST BASED)
# ===============================
@app.route('/delete/<int:id>', methods=['POST'])
def delete_task(id):
    global TASKS
    TASKS = [t for t in TASKS if t['id'] != id]
    return redirect(url_for('home'))

# ===============================
# ABOUT PAGE
# ===============================
@app.route('/about')
def about():
    return render_template('about.html')

# ===============================
# RUN APP
# ===============================
if __name__ == '__main__':
    app.run(debug=True)
