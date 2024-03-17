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
