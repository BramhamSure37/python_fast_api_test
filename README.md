# python_fast_api_test
Full-stack application using React, FastAPI, PostgreSQL, and SQLAlchemy with RESTful CRUD APIs.
# FastAPI PostgreSQL CRUD Application

A full-stack web application built using **FastAPI, PostgreSQL, SQLAlchemy, and React**. This project demonstrates how to build RESTful APIs and perform CRUD (Create, Read, Update, Delete) operations using FastAPI with a PostgreSQL database.

## 🚀 Technologies Used

### Backend
- Python
- FastAPI
- Uvicorn
- SQLAlchemy
- PostgreSQL
- Psycopg
- Pydantic

### Frontend
- React
- JavaScript
- HTML
- CSS
- Vite

### Tools
- Git
- GitHub
- VS Code
- pgAdmin

## ✨ Features

- RESTful API development using FastAPI
- PostgreSQL database integration
- SQLAlchemy ORM for database operations
- CRUD operations for products
- API testing using FastAPI Swagger UI
- React frontend integration
- CORS configuration for frontend-backend communication
- Environment variables for database configuration
- Secure handling of sensitive database credentials

## 📂 Project Structure

```text
fast_api/
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── ...
│
├── main.py
├── database.py
├── database_models.py
├── model.py
├── requirements.txt
├── .gitignore
└── README.md


| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Check if the API is running |
| GET | `/products` | Get all products |
| GET | `/products/{id}` | Get a product by ID |
| POST | `/products` | Add a new product |
| PUT | `/products/{id}` | Update a product |
| DELETE | `/products/{id}` | Delete a product |

🗄️ Database
This project uses PostgreSQL as the database and SQLAlchemy as the ORM.
The main products table contains:
- id
- name
- description
- price
- quantity
⚙️ Installation and Setup
1. Clone the repository
git clone https://github.com/BramhamSure37/python_fast_api_test.git

2. Navigate to the project
cd python_fast_api_test

3. Create a virtual environment
python -m venv myenv

4. Activate the virtual environment
Windows:
myenv\Scripts\activate

5. Install dependencies
pip install -r requirements.txt

6. Configure environment variables
Create a .env file in the project root:
DATABASE_URL=postgresql+psycopg://postgres:YOUR_PASSWORD@localhost:5432/fast_api

Replace YOUR_PASSWORD with your PostgreSQL password.
Do not upload the .env file to GitHub.
7. Start the FastAPI server
uvicorn main:app --reload

The API will be available at:
http://127.0.0.1:8000

8. Open API documentation
FastAPI provides interactive Swagger documentation at:
http://127.0.0.1:8000/docs

🔐 Security
Sensitive information such as database passwords and environment variables are not stored directly in the source code.
The .env file is excluded using .gitignore.
🎯 Learning Objectives
This project was created to understand and practice:
- FastAPI fundamentals
- REST API development
- CRUD operations
- PostgreSQL database connectivity
- SQLAlchemy ORM
- Pydantic models
- API testing
- Frontend and backend integration
- Git and GitHub workflow
- Environment variable management
👨‍💻 Author
Bramham Sure
B.Tech Computer Science and Engineering (AI & ML) Student
GitHub:
https://github.com/BramhamSure37
