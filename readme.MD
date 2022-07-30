# django4_quickstart_template
## docker-compose version

### This is a "prod config" by default, however will show both ways to launch the containers as dev and as prod

---

<!-- ### PROD Configuration (default)

1. django-admin startproject cityp --template https://github.com/devadalberto/django4_quickstart_template/archive/refs/heads/devdocker.zip
2. cd cityp/app
3. change the entrypoint.sh file and replace line 18
```text
{{project_name}} => for the actual app_name, in this case 'cityp'
````
4. cd ..
5. rename the .env and .dbenv files (remove the .sample from the name and make sure to update the contents)
#### make sure you are on the "root" folder, is where the app, database, nginx and pgadmin folders are
6. make sure your entrypoints.*.sh files have exec permissions (sudo chmod a+x entrypoint.*)
7. 
docker-compose up -d --build

--- -->
### DEV configuration


1. django-admin startproject cityd --template https://github.com/devadalberto/django4_quickstart_template/archive/refs/heads/devdocker.zip
2. cd cityp/app
3. change the entrypoint.sh file and replace line 18
```text
{{project_name}} => for the actual app_name, in this case 'cityd'
````
4. cd ..
5. rename the .env and .dbenv files (remove the .sample from the name and make sure to update the contents)
#### confirm you are on the "root" folder, is where the app, database, nginx and pgadmin folders are
6. make sure your entrypoints.*.sh files have exec permissions (sudo chmod a+x entrypoint.*)
7. docker-compose up -f docker-compose.dev.yml --build


---

### ToDo

- [ ] Doc for PROD deployment
- [ ] Modify deployments so they use 2 files: .env & .dbenv files
- [ ] Finish documentation for DEV deployment
- [ ] Fix code to uncomment the flake8 on the app/Dockerfile
- [ ] Optimize image size
- [ ] Check for Security
- [ ] Automate deployment
