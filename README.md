# scribbles
A little experiment in exploring the difference ways to collect and push content to various publishing APIs. The idea is to think about my preferred workflow (especially with devrel content), and how best to both publish and maintain a library of content. Potentially with some data such as reader stats.

Here's a few methods I'm exploring. 

1. Pushing a blog post from localhost to Medium via the Medium API
2. Pushing a blog post from localhost to Harshnode via the Hashnode API
3. Creating a basic webapp to push to both Hashnode and Medium APIs
4. Creating or adapting VS Code plugins to push to the Medium API
5. Create a GitHub Action to push to the Medium API upon a successful commit


The other half of the exploration is how to source and combine the post statistics from multiple published instances. This is useful when cross-posting, or posting different versions of content for different audiences, but being relative to a campaign or topic. To keep it simple I'm focusing on:

1. Retreiving post statistics from the Medium API
2. Retreiving post statistics from the Hashnode API

At this stage I'm not too concerned about the overall architecture, just checking how these methods work, and then thinking about how to logically combine the workflows. 