from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Load blog data
with open('data/blogs.json') as f:
    blogs = json.load(f)

@app.route('/')
def home():
    latest_blog = blogs[0] if blogs else {}
    return render_template('home.html', blog=latest_blog)

@app.route('/blogs')
def blog_list():
    return render_template('blogs.html', blogs=blogs)

@app.route('/api/blogs')
def api_blogs():
    return jsonify(blogs)

if __name__ == '__main__':
    app.run(debug=True)
