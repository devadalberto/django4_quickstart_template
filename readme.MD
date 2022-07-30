# django4_quickstart_template
## docker-compose version

### This is a "prod config" by default, however will show both ways to launch the containers as dev and as prod

#### remember you have to be on the "root" folder (where the app, database, nginx and pgadmin folders are) to run the docker-compose
---

### For both configs follow steps 1 to 6

1. django-admin startproject cityd --template https://github.com/devadalberto/django4_quickstart_template/archive/refs/heads/devdocker.zip
2. cd cityp/app
3. change the entrypoint.sh file and replace line 18
```text
{{project_name}} => for the actual app_name, in this case 'cityd'
````
4. cd ..
5. rename the .env and .dbenv files (remove the .sample from the name and make sure to update the contents)
    Most importan lines are 1 and 2, where {{project_name}}.. well, you know
6. make sure your entrypoints.*.sh files have exec permissions (sudo chmod a+x entrypoint.*)


#### PROD Configuration 

7. docker-compose up -d --build

This prod config runs on port 8844 (with an nginx as a reverse proxy) and django runs using gunicorn

---

### DEV configuration

7. docker-compose -f docker-compose.dev.yml up --build

This Dev config runs on port 9000 and django uses it's build in webserver
---

### ToDo

- [X] Doc for PROD deployment
- [X] Modify deployments so they use 2 files: .env & .dbenv files
- [X] Finish documentation for DEV deployment
- [ ] Fix code to uncomment the flake8 on the app/Dockerfile
- [ ] Optimize image size
- [ ] Check for Security
- [ ] Automate deployment
