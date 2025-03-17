# Django JWT Authentication API

## Overview

This project provides user authentication using Django, Django Rest Framework (DRF), and JSON Web Tokens (JWT). It allows users to register, log in, and authenticate API requests securely.

## Features

- User registration
- User login with JWT token authentication
- Token refresh and verification
- Protected API endpoints

## Technologies Used

- **Python** (Django framework)
- **Django REST Framework (DRF)**
- **JWT (JSON Web Token) Authentication**
- **SQLite/Mysql** (Database)

## Installation

### Prerequisites

Ensure you have the following installed:

- Python (>=3.8)
- pip (Python package manager)
- Virtual environment (optional but recommended)

### Setup Steps

1. **Clone the repository**

```bash
git clone https://github.com/olivicegodwin467/User_Authentication.git
cd User_Authentication
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run database migrations**

```bash
python manage.py migrate
```

5. **Create a superuser (optional, for admin access)**

```bash
python manage.py createsuperuser
```

6. **Start the development server**

```bash
python manage.py runserver
```

## API Endpoints

### Authentication Endpoints

| Method | Endpoint       | Description             |
| ------ | -------------- | ----------------------- |
| POST   | /api/register/ | Register a new user     |
| POST   | /api/login/    | Login and get JWT token |
| GET   | /api/user/     | Successfully login      |
| POST   | /api/logout/   | Logout                  |

### Protected Endpoints (Require JWT Authentication)

| Method | Endpoint   | Description                    |
| ------ | ---------- | ------------------------------ |
| GET    | /api/user/ | Get authenticated user details |

## Usage

### **Register a User**

```bash
curl -X POST http://127.0.0.1:8000/api/register/ \
-H "Content-Type: application/json" \
-d '{"username": "testuser", "email": "test@example.com", "password": "password123"}'
```

### **Login and Get Token**

```bash
curl -X POST http://127.0.0.1:8000/api/login/ \
-H "Content-Type: application/json" \
-d '{"username": "testuser", "password": "password123"}'
```

Response:

```json
{
  "access": "your_jwt_access_token",
  "refresh": "your_jwt_refresh_token"
}
```

### **Access Protected Endpoint**

```bash
curl -X GET http://127.0.0.1:8000/api/user/ \
-H "Authorization: Bearer your_jwt_access_token"
```

## Environment Variables

Create a `.env` file and add the following environment variables:

```env
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=your_database_url
```

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## Contact

For any questions, reach out to: [orivicegodwin@gmail.com](mailto\:orivicegodwin@gmail.com) or github: @olivicegodwin467.

