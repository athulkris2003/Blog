# Django Blog CRUD Application

A beginner-friendly Django web application that implements full CRUD
(Create, Read, Update, Delete) functionality for blog posts.

This project is designed to understand Django fundamentals such as
models, views, templates, URLs, and database migrations.

---

## 🚀 Features

- Create new blog posts
- View all blog posts
- Edit existing blog posts
- Delete blog posts with confirmation
- Clean and simple UI using HTML & CSS
- CSRF protection enabled

---

## 🛠 Tech Stack

- Python 3
- Django
- SQLite (default database)
- HTML5
- CSS3
- Git & GitHub

---

## 📂 Project Structure

project-root/
│
├── manage.py
├── project_name/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── blog/
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── templates/
│
├── templates/
│ ├── index.html
│ ├── add_blog.html
│ ├── update_blog.html
│ └── delete_blog.html
│
├── .gitignore
├── requirements.txt
└── README.md

---

## ⚙️ How to Run the Project Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME

2️⃣ Create a Virtual Environment
python -m venv env


Activate it:

Windows

env\Scripts\activate


Mac / Linux

source env/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Database Migrations
python manage.py migrate

5️⃣ Start the Development Server
python manage.py runserver


Open your browser and visit:

http://127.0.0.1:8000/
```
