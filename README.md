# Flask Authentication App

## 1) Project Title
**Flask Authentication App**

## 2) Project Overview
This project is a beginner-friendly authentication system built with Flask and Flask-SQLAlchemy. It allows users to register, log in, and access a protected dashboard page. User data is stored in a SQLite database, and passwords are securely hashed before saving.

## 3) Features
- User registration and login flow
- Protected dashboard route (only accessible after login)
- Password hashing using `bcrypt`
- Server-side validation in the `/register` route:
  - Name cannot be empty
  - Email cannot be empty
  - Password cannot be empty
  - Password must be at least 6 characters
  - Email must be unique
- Flash messages to show validation errors and success messages
- SQLite database integration
- Ready for deployment on Render

## 4) Tech Stack Used
- **Backend:** Flask
- **Database ORM:** Flask-SQLAlchemy
- **Database:** SQLite
- **Password Security:** bcrypt
- **WSGI Server (Production):** Gunicorn
- **Deployment Platform:** Render

## 5) Installation Steps (Local Setup)
1. Clone the repository.
2. Move into the project folder.
3. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
4. Activate the virtual environment:
   - **Windows (PowerShell):**
     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 6) How to Run the Application
1. Start the Flask app:
   ```bash
   python app.py
   ```
2. Open your browser and visit:
   ```
   http://127.0.0.1:5000
   ```

## 7) Deployment Instructions (Render)
### Option A: Deploy as a Web Service
1. Push your project to GitHub.
2. In Render, click **New +** → **Web Service**.
3. Connect your repository.
4. Use these settings:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. Set environment variables:
   - `SECRET_KEY` (required)
   - `PYTHON_VERSION` = `3.11.11`
   - `DATABASE_URL` = `sqlite:////var/data/charlie.db`

### Option B: Deploy with `render.yaml` (Blueprint)
1. Keep `render.yaml` in the root folder.
2. In Render, click **New +** → **Blueprint**.
3. Select your repository and deploy.

### Important Note for SQLite on Render
SQLite is file-based. To keep your data after restarts, attach a persistent disk and mount it at `/var/data`.

## 8) Project Structure
```text
FlaskAuthAPP/
├── app.py
├── requirements.txt
├── Procfile
├── render.yaml
├── activate.bat
├── instance/
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
└── README.md
```

## 9) Screenshots
Add your screenshots here:
- Home Page
- Register Page
- Login Page
- Dashboard Page
- Flash Message Examples (validation errors/success)

## 10) Author
**Atul Singh**

If you want, add your GitHub and LinkedIn links here for your project portfolio.
