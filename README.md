# User Management System (Django REST + JWT + jQuery)

Auth (JWT), Profile management, and Notes CRUD with file upload. Swagger docs included.

## Features
- User Registration, Login, Logout (JWT with refresh blacklisting)
- Profile view/update; password change
- Notes CRUD (owner-only) with attachment upload
- Pagination (page size 10), search (title/description), ordering
- Minimal jQuery frontend
- Swagger UI at `/swagger/`

## Tech
- Django 4.2, DRF, SimpleJWT, drf-yasg
- SQLite by default
- CORS open for demo

## Setup

```bash
git clone <your-repo-url> user-mgmt
cd user-mgmt
python -m venv env
source env/bin/activate  # or .\env\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
# -User-Management-System
 User Management System
