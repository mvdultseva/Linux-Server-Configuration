## Installed software: 
   PostgreSQL==9.5.14
   Apache==2.4.18
   libapache2-mod-wsgi-py3
   git version 2.7.4
    
## Connect to server
Server address: http://54.213.7.56.xip.io/

Port: 2200

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
    - Create an Apache config file `/etc/apache2/sites-enabled/000-default.conf`. Add the following line at the end of the `<VirtualHost *:80>` block, right before the closing `</VirtualHost>` line: `WSGIScriptAlias / /var/www/catalog_app/catalog_app.wsgi`
    - Install and configure PostgreSQL:
            `sudo apt-get install postgresql postgresql-contrib`
            Create database named `catalog` for the user `catalog` 
    - Installing git:
             `sudo apt-get install git`
6. Deploy the app
    - Clone app `https://github.com/mvdultseva/catalog_app.git` to the directory /var/www/catalog_app
    - Add catalog_app.wsgi file. The configuration file can be seen on the `catalog_app.wsgi` file included in the repository 
    - In order to run application you have to create Python virtual environment and install all packages from the `requirements.txt`:
    
        a. Create virtual environment: `python3 -m venv catalog_app/venv3`
        
        b. Activate virtual environment: `source catalog_app/venv3/bin/activate`
        
        c. Install all dependencies: `pip install -r requirements.txt`
        
        d. Change the `engine` inside application: `engine = create_engine(postgresql://catalog:123@localhost/catalog)`
        
        e. Set up the DB with python `/var/www/catalog_app/catalog_app/database_setup.py`
        
7. Restart Apache:
    Run `sudo service apache2 restart`

## Third-Party resources used to complete this project
    - https://www.digitalocean.com/
    - https://www.sqlalchemy.org/
    - http://flask.pocoo.org/
    - https://modwsgi.readthedocs.io/en/develop/
    - https://stackoverflow.com/
    - https://www.postgresql.org/
