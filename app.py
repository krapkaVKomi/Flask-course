from flask import Flask, render_template



app = Flask(__name__)

# Simple data list for Dynamic Routing
users = [
    {"id": 1, "name": "Ivan"},
    {"id": 2, "name": "Oleh"},
    {"id": 3, "name": "Alex"}
]


# URL Building та роут для головної сторінки
@app.route('/')
def index():
    return "Hello world in Flask!"


# Templates та Render HTML
@app.route('/hi/<name>')
def hello_to_user(name):
    return render_template('greeting.html', name=name)


# Jinja2 and Template Inheritance
@app.route('/about')
def about():
    return render_template('about.html', title='About Us', content='This is the about page.')


@app.route('/user/<int:user_id>')
def user_profile(user_id):
    for user in users:
        if user['id'] == user_id:
            return f"User Profile: {user['name']}"
    return "User not found!"


if __name__ == "__main__":
    app.run(debug=True)
