import json
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    with open('data/posts.json', 'r') as f:
        blog_posts = json.load(f)

    return render_template('index.html', blog_posts=blog_posts)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        content = request.form['content']

        with open('data/posts.json', 'r') as f:
            blog_posts = json.load(f)

        new_post = {
            'id': len(blog_posts) + 1,
            'title': title,
            'author': author,
            'content': content
            }
        blog_posts.append(new_post)
        with open('data/posts.json', 'w') as f:
            json.dump(blog_posts, f)

        return redirect(url_for('index'))
    return render_template('add.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)