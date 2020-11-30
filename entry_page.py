from flask import Flask, render_template, flash, redirect, url_for
from my_form_module import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '9dc4531ba646fac185ff030e475d7130'

posts = [
    {
        'author': 'Manilal Kasera',
        'title': 'Blog 1',
        'content': 'First post content',
        'date': 'April 20, 2018'
    },
    {
        'author': 'Coreh Schafer',
        'title': 'Blog 2',
        'content': 'Second post content',
        'date': 'April 21, 2018'
    }
]


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html', posts = posts)

@app.route('/about')
def about():
    return render_template('about.html', title= 'About Page')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created {form.username.data}', 'success')
        return redirect(url_for('home_page'))
    return render_template('register.html', form = form, title = 'Registeration Page')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'mani@gmail.com' and form.password.data == '123':
            flash(f'Login success {form.email.data}', 'success')
            return redirect(url_for('home_page'))
        else:
            flash(f'Login failed', 'danger')
    return render_template('login.html', form = form, title = 'Login Page')


if __name__ == '__main__':
    app.run(debug=True)

