# machine_learning_project
This is my first machine learning project

##Software and Accounts Requirement
1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [Git cli](https://git-scm.com/downloads)


create conda environment
```
conda create -p venv python==3.7 -y
```

Activate conda environment
```
conda activate venv/
```
OR
```
conda activate venv
```

create new requirements.txt file and add python library that is to be installed

```
pip install requirements.txt
```

To Add files to git
```
git add .
```

OR
```
git add <file_name>
```

>Note: To ignore file or folder from git we can write name or file/folder in .gitignore

To check the git status
```
git status
```

To check all version by git
```
git log
```

To create version/commit all changes by git
```
git commit -m "messege"
```

To reset all the git command
```
git reset
```

global configuration for git bash

To set username
```
git config --global user.name "myusername"
```

To set email
```
git config --global user.email "myemailadress"
```

To set password
```
git config --global user.password "mypassword"
```

To send changes/version to github
```
git push origin main
```

To check remote url
```
git remote -v
```

To set up CI/CD pipeline in heroku we need 3 information
1. HEROKU EMAIL = ywaquar@gmail.com
2. HEROKU API_KEY = 6d3b06e3-0020-48e1-8cdd-42188dec4a46
3. HEROKU APP_NAME = 


BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```

> Note: Image name for docker must be lowercase

To list images
```
docker images
```

Run docker images
```
docker run -p 5000:5000 -e PORT=5000 <IMAGE ID>
```
>NOTE: IMAGE ID can be get by running 'docker images' command

To Check running container in docker
```
docker ps
```

Tp stop docker container
```
docker stop <container_id>
```