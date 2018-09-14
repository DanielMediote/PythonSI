from flask import Flask

app = Flask (__name__)

@app.route('/')
def index():
    return "<h1>Hello World</h1>"

@app.route('/hello')
def hello():
    return "Hello World"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return '<h1>ID do Post: %d</h1>' % post_id

if __name__ == '__main__'
    app.run();