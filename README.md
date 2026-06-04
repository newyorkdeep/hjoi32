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

Screenshots:
<img width="877" height="491" alt="image" src="https://github.com/user-attachments/assets/bc9f7964-8635-476b-b923-e4f79206c2f6" />
<img width="877" height="493" alt="image" src="https://github.com/user-attachments/assets/e5c313a9-5bad-4447-8126-a0ceb9326a28" />
<img width="875" height="488" alt="image" src="https://github.com/user-attachments/assets/3d3fbcd4-c2ea-45e9-8bff-c0fd4f1c6b72" />
