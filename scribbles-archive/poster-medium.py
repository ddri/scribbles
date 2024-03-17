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
