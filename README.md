# Expense Tracker API

A robust RESTful API built with **FastAPI** and **SQLAlchemy** for managing personal expenses. This API includes secure user authentication using JWT (JSON Web Tokens) and provides full CRUD (Create, Read, Update, Delete) capabilities for user-specific expense tracking.

## Features

* **User Authentication:** Secure registration and login functionality.
* **Password Hashing:** Passwords are encrypted using `bcrypt` before database storage.
* **JWT Authorization:** Bearer token-based protected routes.
* **Expense Management:** Users can view, create, update, and delete their expense entries.
* **Input Validation:** Strict payload validation using Pydantic schemas.
* **Database Integration:** Relational database management using SQLAlchemy ORM (MySQL).

## Tech Stack

* **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
* **ORM:** [SQLAlchemy](https://www.sqlalchemy.org/)
* **Database:** MySQL (via `pymysql`)
* **Data Validation:** Pydantic
* **Authentication:** `python-jose` (JWT), `bcrypt`
* **Server:** Uvicorn

## Project Structure

```text
├── main.py           # Application entry point and router inclusion
├── database.py       # SQLAlchemy engine and session management
├── models.py         # SQLAlchemy database models (Users, Expenses)
├── schemas.py        # Pydantic models for request/response validation
├── security.py       # Password hashing and JWT token utility functions
├── auth.py           # API router for authentication endpoints
├── expenses.py       # API router for expense CRUD endpoints
└── README.md         # Project documentation
```
## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/pratham636/Expense-Tracker-API.git
   cd expense-tracker
   ```
   2. **Set up virtual environment:**
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Mac/Linux:
   source venv/bin/activate
   ```
  3. **Install dependencies:**
   ```bash
   pip install fastapi uvicorn sqlalchemy pymysql pydantic python-jose[cryptography] passlib[bcrypt]
   ```
   4. **Run the application:**
   ```bash
   uvicorn main:app --reload
   ```
   ## 🚀 Usage & Docs

* **Swagger UI:** http://127.0.0.1:8000/docs
* **Authentication Flow:** 1. Register a new user via the `/register` endpoint.
  2. Login via `/token` to receive your JWT access token.
  3. Click the **Authorize** (lock icon) button in Swagger and paste the token to access protected expense routes.

> **Note:** Ensure your MySQL server is running and the database connection string in `database.py` is correctly configured before starting.
