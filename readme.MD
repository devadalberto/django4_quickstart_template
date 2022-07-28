# django4_quickstart_template
## docker-compose version

### This is a "prod config" by default, however will show both ways to launch the containers as dev and as prod

---

### PROD Configuration (default)

1. django-admin startproject cityp --template https://github.com/devadalberto/django4_quickstart_template/archive/refs/heads/devdocker.zip
2. cd cityp/app
3. change the entrypoint.sh file and replace line 18
```text
{{project_name}} => for the actual app_name, in this case 'cityp'
````
4. docker-compose up -d --build

---
### DEV configuration


1. django-admin startproject cityd --template https://github.com/devadalberto/django4_quickstart_template/archive/refs/heads/devdocker.zip
2. cd cityd
3. docker-compose up -f docker-compose.dev.yml -d --build
4. go to http://127.0.0.1:8000
    or http://127.0.0.1:1337  (update)


---

### ToDo

- [ ] Finish documentation
- [ ] Optimize image size
- [ ] Check for Security
- [ ] Automate deployment
