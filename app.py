from flask import Flask, render_template

app = Flask(__name__)

# Project data - this would typically come from a database
project_data = {
    1: {
        "id": 1,
        "title": "NLP Task",
        "description": "A natural language processing project that analyzes text sentiment and extracts key information. This project uses advanced ML algorithms to provide insights from unstructured text data.",
        "tools": ["NLP", "TENSORFLOW", "FLASK", "PYTHON"],
        "images": ["/static/use.jpeg", "/static/use.jpeg", "/static/use.jpeg"],
        "github_link": "https://github.com/krunalpatel355/nlp-project",
        "live_link": None
    },
    2: {
        "id": 2,
        "title": "Data Analytics Dashboard",
        "description": "Interactive dashboard for visualizing complex datasets, with real-time filtering and analysis capabilities.",
        "tools": ["Python", "Dash", "Plotly", "Pandas"],
        "images": ["/static/use.jpeg", "/static/use.jpeg", "/static/use.jpeg"],
        "github_link": "https://github.com/krunalpatel355/analytics-dashboard",
        "live_link": "https://dashboard-demo.example.com"
    },
    3: {
        "id": 3,
        "title": "Machine Learning Model",
        "description": "Predictive model using machine learning algorithms to forecast trends based on historical data.",
        "tools": ["Scikit-learn", "Python", "Jupyter", "Matplotlib"],
        "images": ["/static/use.jpeg", "/static/use.jpeg", "/static/use.jpeg"],
        "github_link": "https://github.com/krunalpatel355/ml-model",
        "live_link": None
    },
    4: {
        "id": 4,
        "title": "Portfolio Website",
        "description": "A personal portfolio website built with Flask and modern web technologies.",
        "tools": ["HTML", "CSS", "Python", "Flask"],
        "images": ["/static/use.jpeg", "/static/use.jpeg", "/static/use.jpeg"],
        "github_link": "https://github.com/krunalpatel355/portfolio",
        "live_link": "https://krunalpatel.com"
    }
}

# Define routes for the portfolio
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/project')
def projects():
    return render_template('project.html', projects=project_data)

@app.route('/project/<int:project_id>')
def project_details(project_id):
    project = project_data.get(project_id)
    if project:
        return render_template('project_details.html', project=project)
    else:
        # Handle case where project doesn't exist
        return "Project not found", 404

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True,host = "0.0.0.0",port = 8080)