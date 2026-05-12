import json
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


def fetch_post_by_id(blog_posts, post_id):
    """
    Return the post dict whose 'id' matches post_id, or None if not found.

    return: dict – the matching post, or None if no post has the given id.
    """
    for post in blog_posts:
        if post['id'] == post_id:
            return post
    return None


@app.route('/')
def index():
    """
    Load all posts from the JSON store and render the main index page.

    return: Response – rendered index.html template with all blog posts.
    """
    with open('data/posts.json', 'r', encoding='utf-8') as f:
        blog_posts = json.load(f)

    return render_template('index.html', blog_posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """
    GET  – render the form for creating a new post.
    POST – read form data, append the new post to the JSON store, and redirect
           to the index.

    return: Response – rendered add.html on GET, or a redirect to
            index on POST.
    """
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        content = request.form['content']

        with open('data/posts.json', 'r', encoding='utf-8') as f:
            blog_posts = json.load(f)

        new_post = {
            'id': (max(post['id'] for post in blog_posts) + 1
                   if blog_posts else 1),
            'title': title,
            'author': author,
            'content': content
        }
        blog_posts.append(new_post)
        with open('data/posts.json', 'w', encoding='utf-8') as f:
            json.dump(blog_posts, f)

        return redirect(url_for('index'))
    return render_template('add.html')


@app.route('/delete/<int:post_id>')
def delete(post_id):
    """
    Remove the post with the given post_id from the JSON store
    and redirect to index.

    return: Response – redirect to the index page.
    """
    with open('data/posts.json', 'r', encoding='utf-8') as f:
        blog_posts = json.load(f)

    updated_blog_posts = [post for post in blog_posts if post['id'] != post_id]

    with open('data/posts.json', 'w', encoding='utf-8') as f:
        json.dump(updated_blog_posts, f)

    return redirect(url_for('index'))


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    """
    GET  – render the edit form pre-filled with the existing post data.
    POST – overwrite the post's fields in the JSON store and redirect to index.

    return: Response – rendered update_form.html on GET, redirect to
                       index on POST, or a 404 string response if the
                       post does not exist.
    """
    with open('data/posts.json', 'r', encoding='utf-8') as f:
        blog_posts = json.load(f)

    post = fetch_post_by_id(blog_posts, post_id)
    if post is None:
        # Post not found
        return "Post not found", 404

    if request.method == 'POST':
        updated_post = {
            'id': post['id'],
            'title': request.form['title'],
            'author': request.form['author'],
            'content': request.form['content']
        }

        for post in blog_posts:
            if post['id'] == updated_post['id']:
                post['title'] = updated_post['title']
                post['author'] = updated_post['author']
                post['content'] = updated_post['content']
                break

        with open('data/posts.json', 'w', encoding='utf-8') as f:
            json.dump(blog_posts, f)

        return redirect(url_for('index'))

    return render_template('update_form.html', post=post)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
