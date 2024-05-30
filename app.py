from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

from forms.cblaster_form import CblasterSearchForm

# The Flask instance
app = Flask(__name__)

# The users database // Add the users database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

# The secret key
app.config['SECRET_KEY'] = 'secret_key'  # This needs to be hidden better in deployment

# The users database // Initialize the users database
db = SQLAlchemy(app)


# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html')


# Invalid URL Error
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


# Home Page
@app.route('/')
def home():
    return render_template('index.html')


# Create Name page from the tutorial
@app.route('/dashboard', methods=['GET', 'POST'])
def name():
    job_title = "Test"
    form = CblasterSearchForm()
    # Validate Form
    if form.validate_on_submit():
        job_title = form.job_title.data
        form.job_title.data = ''
    return render_template('my_dashboard.html', job_title=job_title, form=form)


# Cblaster Page
@app.route('/cblaster', methods=['GET', 'POST'])
def cblaster_search_form():
    form = CblasterSearchForm()
    if request.method == 'POST' and form.validate_on_submit():
        # The code below is incomplete. It was written to integrate cblaster search form with the back-end
        # Process form data
        job_title = form.job_title.data
        institution_name = form.institution_name.data
        email_address = form.email_address.data

        # Clearing these variables to use them again in the future
        form.job_title.data = ''
        form.institution_name.data = ''
        form.email_address.data = ''

        # Call the function from run_cblaster.py
        # processed_data = process_cblaster_data(form_data)

        # Pass the processed data to a template for display
        return render_template('cblaster_form_info.html', form_data=form)

    return render_template('cblaster_search.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
