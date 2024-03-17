
# Introduction

This is a worklog for a fun project exploring some APIs and content publishing methods. The following is a record of my approach and experimentation while exploring a range of tasks and wrapping them roughly in a web application.

------

# Requirements

- xcode
- Python
- Pip
- Flask


## Install xcode

```
xcode-select --install
```

## Install Python

The steps to install Python depend on your operating system. Here's how to install Python on different platforms:

**Windows**

1. Go to the official Python download page: https://www.python.org/downloads/
2. Download the latest Python 3 release for Windows.
3. Run the installer and follow the instructions.
4. During the installation, make sure to select the "Add Python to PATH" option so that you can run Python from the command line.
5. Once the installation is complete, open the command prompt and type `python` to verify that Python is installed.

**macOS**

1. macOS comes with a pre-installed version of Python. To check the version, open the Terminal and type `python --version`.
2. If you need a different version of Python, you can install it using Homebrew (https://brew.sh/). To install Homebrew, open the Terminal and type `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`.
3. Once Homebrew is installed, type `brew install python` to install the latest version of Python.

**Linux**

1. Open a terminal and type the following command to install Python:

   - On Ubuntu or Debian: `sudo apt-get install python3`
   - On Fedora or Red Hat: `sudo dnf install python3`
   - On CentOS or RHEL: `sudo yum install python3`

2. Once the installation is complete, type `python3` to start the Python interpreter.

-------

## Install pip


pip is the package installer for Python. If you have Python version 2.7.9 or later (or Python 3.4 or later), pip should already be installed on your system. You can check if pip is installed by running the following command in your terminal or command prompt:

```
pip --version
```

If you see a version number, pip is already installed. If you get an error message, you'll need to install pip.

Here's how to install pip:

**Windows**

1. Download the `get-pip.py` script from https://bootstrap.pypa.io/get-pip.py
2. Open the command prompt and navigate to the directory where you downloaded the `get-pip.py` script.
3. Run the command `python get-pip.py` to install pip.
4. Verify that pip is installed by running the command `pip --version`.

**macOS**

1. Open the Terminal and run the command `sudo easy_install pip`. This will install pip using the macOS built-in Python.
2. Verify that pip is installed by running the command `pip --version`.

**Linux**

1. Open a terminal and run the following command to install pip:

   - On Ubuntu or Debian: `sudo apt-get install python-pip`
   - On Fedora or Red Hat: `sudo dnf install python-pip`
   - On CentOS or RHEL: `sudo yum install python-pip`

2. Verify that pip is installed by running the command `pip --version`.

That's it! Once pip is installed, you can use it to install Python packages by running the command `pip install <package-name>`.


## Install Flask

Install Flask using pip:

```
pip install Flask
```

-------


# Create an API call for Medium


Medium has a public API that allows developers to programmatically interact with their platform, including creating and publishing posts. To publish a blog post to Medium via their API, you will need to:

- Obtain an access token from Medium by creating an application on their developer portal.
- Use the access token to authenticate your requests to the API.
- Create a post object with the title, content, and any other metadata for the post.
- Make a POST request to the Medium API's /posts endpoint with the post object in the request body.
- Medium's API documentation provides detailed instructions on how to use their API to publish posts, as well as examples in various programming languages.


## Obtain an access token

First, you'll need to create an account on Medium and create an application on their developer portal to obtain an access token.



## Use the access token to authenticate to the API

Once you have the access token, you can use the Requests library in Python to make API requests to Medium's API. Here's an example of how to create a new post on Medium using Python:


```python
import requests
import json

url = "https://api.medium.com/v1/users/<YOUR-USER-ID>/posts"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer <YOUR-ACCESS-TOKEN>"
}

data = {
    "title": "Your blog post title",
    "contentFormat": "html",
    "content": "Your blog post content in HTML format",
    "tags": ["tag1", "tag2"],
    "canonicalUrl": "https://yourblog.com/your-post-url"
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 201:
    print("Your blog post has been published on Medium!")
else:
    print("Something went wrong. Status code:", response.status_code)
```

In this example, you'll need to replace <YOUR-USER-ID> with your Medium user ID, <YOUR-ACCESS-TOKEN> with your Medium access token, and fill in the data dictionary with your blog post title, content, tags, and canonical URL.

Note that the content field should be in HTML format, so you may need to use an HTML parser library like Beautiful Soup to convert your blog post content to HTML.


------



# Create an application with Flask

To turn this code into a web application, you'll need to use a Python web framework like Flask or Django. Here's an example using Flask.

Create a new Flask app in a file named `app.py`:

```python
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/publish', methods=['POST'])
def publish():
    user_id = request.form['user_id']
    access_token = request.form['access_token']
    title = request.form['title']
    content = request.form['content']
    tags = request.form['tags']
    canonical_url = request.form['canonical_url']

    url = f"https://api.medium.com/v1/users/{user_id}/posts"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }
    data = {
        "title": title,
        "contentFormat": "html",
        "content": content,
        "tags": tags.split(','),
        "canonicalUrl": canonical_url
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        return "Your blog post has been published on Medium!"
    else:
        return f"Something went wrong. Status code: {response.status_code}"

if __name__ == '__main__':
    app.run(debug=True)
```

Create a new HTML template file named `index.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Publish to Medium</title>
</head>
<body>
    <h1>Publish to Medium</h1>
    <form method="post" action="/publish">
        <label>User ID:</label>
        <input type="text" name="user_id" required><br>
        <label>Access Token:</label>
        <input type="text" name="access_token" required><br>
        <label>Post Title:</label>
        <input type="text" name="title" required><br>
        <label>Post Content:</label>
        <textarea name="content" required></textarea><br>
        <label>Tags:</label>
        <input type="text" name="tags"><br>
        <label>Canonical URL:</label>
        <input type="text" name="canonical_url"><br>
        <input type="submit" value="Publish">
    </form>
</body>
</html>
```

Run the Flask app using the command:

```
python app.py
```

This will start a local web server at `http://localhost:5000/`. You can access the web app in your browser and fill out the form to publish blog posts to Medium.

Note that this is just a simple example. There is no errors handling and validating user input.



# Hosting on AWS

To host your Flask application on AWS, you can use Amazon Elastic Beanstalk, which is a fully-managed service that makes it easy to deploy and scale web applications.

Here's how you can deploy your Flask application to Elastic Beanstalk:

1. First, create a new Elastic Beanstalk environment using the AWS Management Console or the AWS CLI.

2. In your Flask app directory, create a file named `requirements.txt` that lists all of your Python dependencies. For example:

```
Flask==2.0.2
requests==2.26.0
```

3. Create a file named `.ebextensions/python.config` with the following contents:

```
option_settings:
  aws:elasticbeanstalk:container:python:
    WSGIPath: app.py
```

This tells Elastic Beanstalk that your Flask application is in `app.py`.

4. Create a ZIP file containing your Flask app and all of its dependencies, including `app.py`, `requirements.txt`, and the `.ebextensions` directory:

```
zip -r myapp.zip app.py requirements.txt .ebextensions
```

5. Upload the ZIP file to your Elastic Beanstalk environment using the AWS Management Console or the AWS CLI.

6. Once the upload is complete, Elastic Beanstalk will automatically create a new application version and deploy it to your environment. You can access your Flask app by going to the environment URL.

That's it! Elastic Beanstalk will handle all of the server infrastructure for you, including load balancing, auto-scaling, and security updates.



# Create a graphic interface

To create a graphical user interface (GUI) for your Flask application, you can use a web framework like Flask-Bootstrap or Flask-WTF. Flask-Bootstrap provides templates and helper functions for building responsive HTML and CSS interfaces, while Flask-WTF provides forms and validation functionality.

Here's an example using Flask-Bootstrap:

1. First, install Flask-Bootstrap using pip:

```
pip install Flask-Bootstrap
```

2. Import Flask-Bootstrap in your Flask app:

```python
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
```

3. Update your HTML template to use Bootstrap:

```html
{% extends "bootstrap/base.html" %}

{% block title %}Publish to Medium{% endblock %}

{% block content %}
<div class="container">
    <div class="row">
        <div class="col-md-6">
            <h1>Publish to Medium</h1>
            <form method="post" action="/publish">
                {{ form.hidden_tag() }}
                <div class="form-group">
                    {{ form.user_id.label }}
                    {{ form.user_id(class="form-control", required="required") }}
                </div>
                <div class="form-group">
                    {{ form.access_token.label }}
                    {{ form.access_token(class="form-control", required="required") }}
                </div>
                <div class="form-group">
                    {{ form.title.label }}
                    {{ form.title(class="form-control", required="required") }}
                </div>
                <div class="form-group">
                    {{ form.content.label }}
                    {{ form.content(class="form-control", required="required") }}
                </div>
                <div class="form-group">
                    {{ form.tags.label }}
                    {{ form.tags(class="form-control") }}
                </div>
                <div class="form-group">
                    {{ form.canonical_url.label }}
                    {{ form.canonical_url(class="form-control") }}
                </div>
                <button type="submit" class="btn btn-primary">Publish</button>
            </form>
        </div>
    </div>
</div>
{% endblock %}
```

4. Update your Flask app to use Flask-WTF and render the template:

```python
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    user_id = StringField('User ID', validators=[DataRequired()])
    access_token = StringField('Access Token', validators=[DataRequired()])
    title = StringField('Post Title', validators=[DataRequired()])
    content = TextAreaField('Post Content', validators=[DataRequired()])
    tags = StringField('Tags')
    canonical_url = StringField('Canonical URL')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = PostForm()

    if form.validate_on_submit():
        user_id = form.user_id.data
        access_token = form.access_token.data
        title = form.title.data
        content = form.content.data
        tags = form.tags.data
        canonical_url = form.canonical_url.data

        # Call Medium API to publish post

        return "Your blog post has been published on Medium!"

    return render_template('index.html', form=form)
```

Now, when you access the root URL of your Flask app, you'll see a form that allows you to enter the parameters for publishing a blog post to Medium.

Note that this is just a simple example to get you started. In a real web application, you would want to handle errors and validate user input to prevent security vulnerabilities.


# Set up a custom domain

To set a custom domain for your Flask application hosted on Elastic Beanstalk, you'll need to do the following:

1. In the AWS Management Console, go to the Route 53 service and create a new hosted zone for your domain.

2. In the hosted zone, create a new A record with the following settings:

   - Name: The subdomain you want to use (e.g. `www`)
   - Type: A - IPv4 address
   - Alias: Yes
   - Alias target: Select your Elastic Beanstalk environment from the dropdown list

   You can also create a CNAME record for the root domain (e.g. `example.com`) that points to the subdomain (e.g. `www.example.com`).

3. In your Flask app, add the custom domain to the `ALLOWED_HOSTS` setting in your app's configuration:

```python
app.config['SERVER_NAME'] = 'www.example.com'
app.config['ALLOWED_HOSTS'] = ['www.example.com']
```

This tells Flask to only accept requests for the custom domain.

4. Finally, go to the Elastic Beanstalk console and update the environment URL to use the custom domain:

   - In the left-hand navigation pane, click on "Configuration".
   - Under "Load Balancer", click on "Modify".
   - In the "Alternate Domain Names (CNAMEs)" field, enter your custom domain (e.g. `www.example.com`).
   - Click "Save".

   This will update the Elastic Beanstalk environment to use your custom domain.

Note that it may take some time for the DNS changes to propagate, so be patient. Once the changes have propagated, you should be able to access your Flask application using your custom domain.


# Create an API call for Hashnode

Yes, you can also publish to a Hashnode blog using their public API. Here's an example of how to publish a blog post to Hashnode using Python:

1. First, obtain an API key from Hashnode by going to your account settings and generating a new API key.

2. Install the Requests library using pip:

```
pip install requests
```

3. Use the following code to publish a new blog post to Hashnode:

```python
import requests

url = 'https://api.hashnode.com'
api_key = '<YOUR-API-KEY>'

# Step 1: Get user's blog ID
query = '''
query {
  user(username: "YOUR-USERNAME") {
    publication {
      _id
    }
  }
}
'''
response = requests.post(url, json={'query': query}, headers={'Authorization': api_key})
response.raise_for_status()
data = response.json()
blog_id = data['data']['user']['publication']['_id']

# Step 2: Publish a new post
mutation = '''
mutation ($input: CreateStoryInput!) {
  createStory(input: $input) {
    _id
  }
}
'''
variables = {
    'input': {
        'title': 'Your blog post title',
        'contentMarkdown': 'Your blog post content in Markdown format',
        'isRepublished': False,
        'publicationId': blog_id,
        'coverImage': {
            'type': 'UNSPLASH',
            'source': 'https://images.unsplash.com/photo-1569442008460-dfe9a6de03f6'
        }
    }
}
response = requests.post(url, json={'query': mutation, 'variables': variables}, headers={'Authorization': api_key})
response.raise_for_status()
data = response.json()
post_id = data['data']['createStory']['_id']

print(f'Your blog post has been published on Hashnode with ID {post_id}')
```

In this example, replace `<YOUR-API-KEY>` with your Hashnode API key and `'YOUR-USERNAME'` with your Hashnode username. You can also customize the blog post title, content, and cover image as needed.

Note that the `contentMarkdown` field should be in Markdown format, so you may need to use a library like `markdown` to convert your blog post content to Markdown.

I hope this helps you get started with publishing to Hashnode using Python!


---------

# Publishing to both

To allow a user to publish to both Medium and Hashnode, you could create a web form that accepts the blog post content, title, tags, and other metadata from the user. Then, you could use the APIs of both Medium and Hashnode to create and publish the blog post on both platforms.

Here's an example of how to modify the Flask application we created earlier to allow the user to publish to both Medium and Hashnode:

```python
from flask import Flask, render_template, request
import requests
import markdown

app = Flask(__name__)

MEDIUM_API_URL = "https://api.medium.com/v1/users/<YOUR-USER-ID>/posts"
HASHNODE_API_URL = "https://api.hashnode.com"
MEDIUM_HEADERS = {
    "Content-Type": "application/json",
    "Authorization": "Bearer <YOUR-ACCESS-TOKEN>"
}
HASHNODE_HEADERS = {
    "Authorization": "<YOUR-API-KEY>"
}

class PostForm(FlaskForm):
    title = StringField('Post Title', validators=[DataRequired()])
    content = TextAreaField('Post Content', validators=[DataRequired()])
    tags = StringField('Tags')
    canonical_url = StringField('Canonical URL')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = PostForm()

    if form.validate_on_submit():
        # Get form data
        title = form.title.data
        content = form.content.data
        tags = form.tags.data
        canonical_url = form.canonical_url.data

        # Publish to Medium
        medium_data = {
            "title": title,
            "contentFormat": "html",
            "content": content,
            "tags": tags.split(','),
            "canonicalUrl": canonical_url
        }
        response = requests.post(MEDIUM_API_URL, headers=MEDIUM_HEADERS, json=medium_data)

        if response.status_code == 201:
            print("Your blog post has been published on Medium!")
        else:
            print(f"Something went wrong with Medium. Status code: {response.status_code}")

        # Publish to Hashnode
        hashnode_data = {
            'title': title,
            'contentMarkdown': markdown.markdown(content),
            'isRepublished': False,
            'publicationId': '<YOUR-PUBLICATION-ID>',
            'coverImage': {
                'type': 'UNSPLASH',
                'source': 'https://images.unsplash.com/photo-1569442008460-dfe9a6de03f6'
            }
        }
        response = requests.post(HASHNODE_API_URL, json=hashnode_data, headers=HASHNODE_HEADERS)

        if response.status_code == 200:
            post_id = response.json()['data']['createStory']['_id']
            print(f'Your blog post has been published on Hashnode with ID {post_id}')
        else:
            print(f"Something went wrong with Hashnode. Status code: {response.status_code}")

        return "Your blog post has been published on both Medium and Hashnode!"

    return render_template('index.html', form=form)
```

In this example, you'll need to replace `<YOUR-USER-ID>`, `<YOUR-ACCESS-TOKEN>`, and `<YOUR-PUBLICATION-ID>` with your Medium user ID, access token, and Hashnode publication ID, respectively.

When the user submits the form, the Flask app will publish the blog post to both Medium and Hashnode using their respective APIs. Once the blog post has been published, the user will see a message indicating that the post has been published on both platforms.

Note that this is just a simple example to get you started. In a real web application, you would want to handle errors and validate user input to prevent security vulnerabilities.