## Connect to server
Server address: http://54.213.7.56.xip.io/

## Connect to grader
Download and save "id_rsa"
ssh grader@54.213.7.56 -p 2200 -i <path to id_rsa file>

## Configuration steps
1. Create an instance in AWS Lightsail
2. Set up your SSH key      
3. Secure your server:
    - Update all currently installed packages
    - Change port 22 to port 2200
    - Setup UFW (Uncomplicated Firewall):
        Only allow incoming request from port 2200(SSH), port 80 (HTTP) and port 123 (NTP)
4. Create a new user called grader and give an access:
    - Run `sudo adduser grader` to create a new user called `grader`
    - Give `grader` the permission to `sudo`
    - Create an SSH key(s) for a `grader` user with `ssh-keygen` in your local machine
5. Prepare to deploy app:
    - Set up local time zone to UTC
    - Install Apache application and wsgi module:
            `sudo apt-get install apache2`
            `sudo apt-get install python-setuptools libapache2-mod-wsgi`
    - Install and configure PostgreSQL:
            `sudo apt-get install postgresql postgresql-contrib`
            create a new database user named `catalog`
    - Installing git:
             `sudo apt-get install git`
6. Deploy app
    - Clone app `https://github.com/mvdultseva/catalog_app.git` to the directory /var/www/catalog_app
    - Add catalog_app.wsgi file
    - Run `sudo nano catalog.wsgi`

## All installed software: 
    `requirements.txt`
## Third-Party resources used to complete this project
    - https://www.digitalocean.com/
    - https://www.sqlalchemy.org/
    - http://flask.pocoo.org/
    - https://modwsgi.readthedocs.io/en/develop/
    - https://stackoverflow.com/
    - https://www.postgresql.org/
