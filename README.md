Installation guide:
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip python3-venv libpq-dev python3-dev postgresql postgresql-contrib -y
sudo -i -u postgres psql
CREATE DATABASE dynamic_form_db;
CREATE USER dynamic_user WITH PASSWORD 'your_secure_password';
ALTER ROLE dynamic_user SET client_encoding TO 'utf8';
ALTER ROLE dynamic_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE dynamic_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE dynamic_form_db TO dynamic_user;
\q
git clone https://github.com
cd YOUR_REPO_NAME
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install django psycopg2-binary

Ensure settings.py contains this information:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dynamic_form_db',
        'USER': 'dynamic_user',
        'PASSWORD': 'your_secure_password', 
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

Then you can migrate and run:
python manage.py migrate
python manage.py runserver 0.0.0.0:8000

🎉 Success! Open your browser and navigate to http://localhost:8000/ (or your server's IP address) to access the application.

Screenshots:
<img width="877" height="491" alt="image" src="https://github.com/user-attachments/assets/bc9f7964-8635-476b-b923-e4f79206c2f6" />
<img width="877" height="493" alt="image" src="https://github.com/user-attachments/assets/e5c313a9-5bad-4447-8126-a0ceb9326a28" />
<img width="875" height="488" alt="image" src="https://github.com/user-attachments/assets/3d3fbcd4-c2ea-45e9-8bff-c0fd4f1c6b72" />
