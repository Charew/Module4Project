CNIT-381
Brennan Kocovsky // Alec Pennings

# CHALLENGES
We ran into many challenges during this project, but got some great assistance from Jordan. Here were some of our issues:
1.	Cannot chmod 777 to the Vercel Python directory because it does not exist
2.	Cannot log in to Vercel in the terminal due to an Unexpected Token syntax error
3.	Cannot view or run our repository on Vercel online due to “The serverless function has crashed”

Here's how we fixed them:
1. Chmod ended up being unnecessary to perform, so this solved itself
2. Started a fresh VM, reinstalled NVM, opened a new terminal to activate NVM, install node.js, open a new terminal, install vercel
3. In index.py, we were missing a class handler to invoke the serverless function. You can view our code to see how we fixed this

# WHAT WE LEARNED
1. Vercel is a really cool way to run serverless code
2. Sometimes you need to open a new Linux terminal to see reflections from new packages
3. GitHub is nice for forking repositories so you can test ideas without hurting the master code

# BACKLOG ITEMS
1. Make the output more visually appealing
2. Return the output into another program to make it more useful, such as a network mapper

# DIFFERENT IP ADDRESS
The reason the IP address is different running on Vercel vs locally is that Vercel is running the code on their server, which has a different public IP.

# VERCEL URL
https://vercel.com/charlie-florences-projects/module4-project
https://module4-project-gamma.vercel.app/
