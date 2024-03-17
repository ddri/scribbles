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
