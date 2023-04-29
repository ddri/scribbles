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
