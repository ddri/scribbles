javascript

const fs = require('fs');
const axios = require('axios');

// Replace with your Medium access token
const accessToken = 'your_medium_access_token';

// Replace with the path to your markdown file
const markdownFilePath = './path/to/your/markdown/file.md';

// Read the markdown file
fs.readFile(markdownFilePath, 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading markdown file:', err);
    return;
  }

  // Convert markdown to HTML
  const html = markdownToHtml(data);

  // Publish the post
  publishPost(html);
});

function markdownToHtml(markdown) {
  // Implement a markdown to HTML converter or use a library
  // For this example, we'll assume a simple implementation
  return markdown.replace('# ', '<h1>').replace('## ', '<h2>');
}

function publishPost(html) {
  const url = 'https://api.medium.com/v1/users/me/posts';
  const headers = {
    'Authorization': `Bearer ${accessToken}`,
    'Content-Type': 'application/json',
  };

  const data = {
    title: 'Your post title',
    content: html,
    publishStatus: 'draft',
  };

  axios.post(url, data, { headers })
    .then((response) => {
      console.log('Post published successfully!');
      console.log('Post ID:', response.data.id);
    })
    .catch((error) => {
      console.error('Error publishing post:', error.response.data.message);
    });
}
