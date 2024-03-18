# scribbles

Scribbles is an open source publishing tool for content creators. The goal is to build a workflow for individuals or teams to stage content, publish to multiple publishing/content services, and manage the analytics and maintenance of that content. An ideal use case would be a developer relations team creating content to support a product release, and being able to push it to blogs, documentation, and other social services from one view. 

Think of Scribbles as "Buffer for long form content", with inspiration from the topic-based authoring movement, and a watchful eye on emerging patterns in AI-generated use content, which we feel will invariably need to conform to a shared team content strategy. 

# roadmap scope

- Medium content publisher for IDE
- Hashnode content publisher for IDE
- Web app version of content publisher
- Web app content management 

# technical notes

- Javascript application initially built for VSCode integration

# Components 

## Medium Poster

This script will read the content of our markdown file, create a new Medium post with the provided title and content, and set the publish status to either 'draft' or 'public'. The post URL will be logged to the console upon successful publication.

TODO: error handling, input validation.


## Medium Server

This server is a simple start to a web app listens for POST requests at /publish, receives the markdown content in the request body, and uses the same logic as before to publish the post to Medium. It then sends a response back to the client with the post URL or an error message.

On the client-side, we need to create a form or an interface for users to upload or paste their markdown files, and then send the data to the server using an HTTP request (e.g., fetch, axios, or XMLHttpRequest). We also need to handle the response from the server and display the post URL or any other relevant information to the user.

TODO: authentication, error handling, input validation, and styling.