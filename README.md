# 🚀 Deployment & Setup Guide (Ubuntu)

Follow these steps to set up the environment, configure the PostgreSQL database, and run the Dynamic Form application on Ubuntu.

---

## 📋 Prerequisites
Ensure your system packages are up to date before starting:
```bash
sudo apt update && sudo apt upgrade -y
```

---

## 🛠️ Step 1: Install System Dependencies
Install Python, `pip`, virtual environment tools, and the required PostgreSQL system libraries:
```bash
sudo apt install python3 python3-pip python3-venv libpq-dev python3-dev postgresql postgresql-contrib -y
```

---

## 🗄️ Step 2: Configure PostgreSQL Database
1. **Log in** to the PostgreSQL prompt as the superuser:
   ```bash
   sudo -i -u postgres psql
   ```

2. **Run the following SQL commands** to create the database, dedicated user, and optimize connection settings (replace `'your_secure_password'` with an actual strong password):
   ```sql
   CREATE DATABASE dynamic_form_db;
   CREATE USER dynamic_user WITH PASSWORD 'your_secure_password';
   ALTER ROLE dynamic_user SET client_encoding TO 'utf8';
   ALTER ROLE dynamic_user SET default_transaction_isolation TO 'read committed';
   ALTER ROLE dynamic_user SET timezone TO 'UTC';
   GRANT ALL PRIVILEGES ON DATABASE dynamic_form_db TO dynamic_user;
   ```

3. **Exit** the database prompt:
   ```sql
   \q
   ```

---

## 💻 Step 3: Project Setup
1. **Clone the repository** and navigate into the project directory:
   ```bash
   git clone [https://github.com](https://github.com/newyorkdeep/hjoi32.git)
   cd hjoi32
   ```

2. **Create and activate** a Python virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the dependencies**:
   ```bash
   pip install --upgrade pip
   pip install django psycopg2-binary
   ```

---

## ⚙️ Step 4: Environment & Database Configuration
Ensure your `settings.py` file reflects the PostgreSQL credentials created in Step 2:

```python
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
```

---

## 🏃 Step 5: Initialize and Run
Apply the database migrations to generate your dynamic data tables and start the local development server:

```bash
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

🎉 **Success!** Open your browser and navigate to `http://localhost:8000/` (or your server's IP address) to access the application.

## If you want to make it work with nginx + gunicorn

### Step 1: Database & App Setup
1.  **Install dependencies**: `sudo apt install python3-pip python3-venv libpq-dev postgresql nginx -y`
2.  **Setup Database**: Create user/database in PostgreSQL.
3.  **Setup App**: Clone repo, create venv, and install requirements (`django`, `gunicorn`, `psycopg2-binary`).
4.  **Configure Settings**: Set `DEBUG = False` and `ALLOWED_HOSTS` in `settings.py`.
5.  **Prepare App**: Run `python manage.py migrate` and `collectstatic`.

### Step 2: Gunicorn Setup
Configure systemd for Gunicorn to manage the application process as a service. Detailed configuration steps for the socket and service files can be found in guide {Link: 1.3.2 https://serverstadium.com/knowledge-base/making-your-django-project-production-ready-on-ubuntu-22-04-gunicorn-and-nginx-setup/} and {Link: 1.3.4 https://dev.to/arctype/set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-20-04-74h}.

1.  **Create Socket**: `/etc/systemd/system/gunicorn.socket`
2.  **Create Service**: `/etc/systemd/system/gunicorn.service`
3.  **Start Services**: `sudo systemctl start gunicorn.socket` and `sudo systemctl enable gunicorn.socket`

### Step 3: Nginx Reverse Proxy Setup
Configure Nginx as a reverse proxy to handle static files and forward requests to Gunicorn.
1.  **Create Nginx Config**: `/etc/nginx/sites-available/your_project`
2.  **Enable Configuration**: Symlink to `sites-enabled` and restart Nginx.
3.  **Allow Traffic**: `sudo ufw allow 'Nginx Full'`

# Screenshots:

<img width="877" height="491" alt="image" src="https://github.com/user-attachments/assets/bc9f7964-8635-476b-b923-e4f79206c2f6" />
<img width="877" height="493" alt="image" src="https://github.com/user-attachments/assets/e5c313a9-5bad-4447-8126-a0ceb9326a28" />
<img width="875" height="488" alt="image" src="https://github.com/user-attachments/assets/3d3fbcd4-c2ea-45e9-8bff-c0fd4f1c6b72" />
