# Flask Authentication App

## Project Description
This project is a simple user authentication system built using **Flask**.  
It allows users to register, log in, and access a protected dashboard page.  
User credentials are stored securely in a **SQLite database**, and passwords are hashed before being saved.

---

## Features
- User registration system  
- User login authentication  
- Password hashing for security  
- Protected dashboard page (accessible only after login)  
- Flash messages for error and success notifications  

---

## Tech Stack
- **Backend:** Flask  
- **Database:** SQLite  
- **ORM:** Flask-SQLAlchemy  
- **Password Security:** bcrypt  
- **Deployment:** Render  

---

## Project Structure
```
FlaskAuthAPP/
│
├── app.py
├── requirements.txt
├── Procfile
├── render.yaml
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
└── instance/
```

---

## Running the Project Locally

### 1. Clone the Repository
```bash
git clone <repository-link>
```

### 2. Navigate to the Project Folder
```bash
cd FlaskAuthAPP
```

### 3. Create a Virtual Environment
```bash
python -m venv venv
```

### 4. Activate the Virtual Environment (Windows)
```bash
venv\Scripts\activate
```

### 5. Install Dependencies
```bash
pip install -r requirements.txt
```

### 6. Run the Application
```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## Deployment
The application is deployed using **Render** with **Gunicorn** as the production server.

---

## Author
**Aanya Tyagi**
