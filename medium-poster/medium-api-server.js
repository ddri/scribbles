const express = require('express');
const app = express();
const fetch = require('node-fetch');
const fs = require('fs');

// Middleware to parse incoming request bodies
app.use(express.json());

app.post('/publish', async (req, res) => {
  const markdown = req.body.markdown; // Assuming the client sends the markdown content in the request body
  const accessToken = 'YOUR_ACCESS_TOKEN';
  const mediumUserId = 'YOUR_MEDIUM_USER_ID';

  const requestBody = {
    title: 'Your Post Title',
    contentFormat: 'markdown',
    content: markdown,
    publishStatus: 'draft'
  };

  try {
    const response = await fetch(`https://api.medium.com/v1/users/${mediumUserId}/posts`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${accessToken}`
      },
      body: JSON.stringify(requestBody)
    });

    const data = await response.json();
    res.json({ success: true, url: data.url });
  } catch (error) {
    console.error('Error publishing post:', error);
    res.status(500).json({ success: false, error: 'Failed to publish post' });
  }
});

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});