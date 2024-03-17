# scribbles
A little experiment in exploring the difference ways to collect and push content to various publishing APIs. A use case is a developer relations project, that wants to write and stage a campaign of content in one environment, and then be able to push that to many publishing destinations, and be able to track and review the performance of content. 



Here's a few methods I'm exploring. 

1. Pushing a blog post from localhost to Medium via the Medium API
2. Pushing a blog post from localhost to Harshnode via the Hashnode API
3. Creating a basic webapp to push to both Hashnode and Medium APIs
4. Creating or adapting VS Code plugins to push to the Medium API
5. Create a GitHub Action to push to the Medium API upon a successful commit


The other half of the exploration is how to source and combine the post statistics from multiple published instances. This is useful when cross-posting, or posting different versions of content for different audiences, but being relative to a campaign or topic. To keep it simple I'm focusing on:

1. Retreiving post statistics from the Medium API
2. Retreiving post statistics from the Hashnode API
3. Using non-AI tools where required (PhantomBuster or scraping)
4. UI for managing content and content campaigns across multiple endpoints

At this stage I'm not too concerned about the overall architecture, just checking how these methods work, and then thinking about how to logically combine the workflows. 


## Medium Poster

This script will read the content of our markdown file, create a new Medium post with the provided title and content, and set the publish status to either 'draft' or 'public'. The post URL will be logged to the console upon successful publication.

TODO: error handling, input validation.


## Medium Server

This server is a simple start to a web app listens for POST requests at /publish, receives the markdown content in the request body, and uses the same logic as before to publish the post to Medium. It then sends a response back to the client with the post URL or an error message.

On the client-side, we need to create a form or an interface for users to upload or paste their markdown files, and then send the data to the server using an HTTP request (e.g., fetch, axios, or XMLHttpRequest). We also need to handle the response from the server and display the post URL or any other relevant information to the user.

TODO: authentication, error handling, input validation, and styling.