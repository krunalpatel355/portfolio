from flask import Flask, render_template

app = Flask(__name__)

# Define routes for the portfolio
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/project')
def projects():
    return render_template('project.html')

@app.route('/project1')
def project_1():
    return render_template('project-1.html')

@app.route('/project2')
def project_2():
    return render_template('project-2.html')

@app.route('/project3')
def project_3():
    return render_template('project-3.html')

@app.route('/project4')
def project_4():
    return render_template('project-4.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True,host = "0.0.0.0",port = 5555)
