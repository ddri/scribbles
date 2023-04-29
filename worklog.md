
# Introduction

This is a worklog for a fun project exploring some APIs and content publishing methods. The following is a record of my approach and experimentation while exploring a range of tasks and wrapping them roughly in a web application.

------

# Requirements

- Python
- Pip
- Flask


# Install Python

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

That's it! Once you have Python installed, you can start writing Python code and running Python scripts.

-------

# Install pip



# Install Flask



Install Flask using pip:

```
pip install Flask
```



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

Note that this is just a simple example to get you started. In a real web application, you would want to handle errors and validate user input to prevent security vulnerabilities.