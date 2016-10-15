# git_auto_deploy

This is a git_auto_deploy. It uses python and flask :D

Deployment instructions to a server: https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps

1. Run this on your server and it works out of port 5000.
2. Add the webhooks to GitHub
3. Make sure to add your repositories to the repository.json file
4. It will run a bash script file (do sudo chmod 777 <script>)
5. The script file is located in the root from the directory undergoing auto_deploy
