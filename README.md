# 🚀 DRF-Practice-API

**Django REST Framework Practice Project** - Learn RESTful APIs, CRUD operations, and Token Authentication with a complete working example.

## 📋 Table of Contents

- [About](#about)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [API Endpoints](#api-endpoints)
- [Usage Examples](#usage-examples)
- [Authentication](#authentication)
- [Contributing](#contributing)

## 🎯 About

This is a comprehensive Django REST Framework practice project designed to help you learn:
- **RESTful API Development**
- **CRUD Operations** (Create, Read, Update, Delete)
- **Token Authentication**
- **Serializers and Viewsets**
- **Database Models and Migrations**
- **Professional Project Structure**

Perfect for beginners and intermediate developers who want to master Django REST Framework!

## ✨ Features

- 🔐 **Token Authentication** - Secure API access
- 📝 **CRUD Operations** - Full Create, Read, Update, Delete functionality
- 🎯 **Two Django Apps** - `webapp` and `webapp2` for different use cases
- 📊 **SQLite Database** - Easy to set up and use
- 🔧 **Professional Structure** - Industry-standard project organization
- 📚 **Well Documented** - Clear code comments and examples

## 🛠 Tech Stack

- **Backend Framework:** Django 5.2.3
- **API Framework:** Django REST Framework 3.16.0
- **Database:** SQLite3
- **Authentication:** Token Authentication
- **Language:** Python 3.x

## 📁 Project Structure

```
DRF-Practice-API/
├── base/                          # Main Django Project
│   ├── base/                      # Django Settings
│   │   ├── __init__.py
│   │   ├── settings.py            # Project settings
│   │   ├── urls.py               # Main URL configuration
│   │   ├── asgi.py
│   │   └── wsgi.py
│   ├── webapp/                    # First Django App
│   │   ├── models.py             # Database models
│   │   ├── views.py              # API views
│   │   ├── serializers.py        # Data serialization
│   │   ├── urls.py               # App URL patterns
│   │   ├── admin.py              # Admin interface
│   │   └── migrations/           # Database migrations
│   ├── webapp2/                   # Second Django App
│   │   ├── models.py             # Additional models
│   │   ├── views.py              # More API views
│   │   ├── serializers.py        # Additional serializers
│   │   ├── urls.py               # App URL patterns
│   │   └── migrations/           # Database migrations
│   ├── manage.py                  # Django management script
│   └── db.sqlite3                # SQLite database
├── .gitignore                     # Git ignore rules
└── README.md                      # This file
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Step 1: Clone the Repository
```bash
git clone https://github.com/Sani-Yadav/DRF-Practice-API.git
cd DRF-Practice-API
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv myenv
myenv\Scripts\activate

# macOS/Linux
python3 -m venv myenv
source myenv/bin/activate
```

### Step 3: Install Dependencies
```bash
cd base
pip install django djangorestframework
```

### Step 4: Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### Step 6: Run the Server
```bash
python manage.py runserver
```

🎉 **Your API is now running at:** `http://127.0.0.1:8000/`
---
http://127.0.0.1:8000/snippet-list/
---

## 📡 API Endpoints

### Authentication
- `POST /api/token/` - Get authentication token
- `POST /api/token/refresh/` - Refresh token

### WebApp Endpoints
- `GET /api/webapp/` - List all items
- `POST /api/webapp/` - Create new item
- `GET /api/webapp/{id}/` - Get specific item
- `PUT /api/webapp/{id}/` - Update item
- `DELETE /api/webapp/{id}/` - Delete item

### WebApp2 Endpoints
- `GET /api/webapp2/` - List all items
- `POST /api/webapp2/` - Create new item
- `GET /api/webapp2/{id}/` - Get specific item
- `PUT /api/webapp2/{id}/` - Update item
- `DELETE /api/webapp2/{id}/` - Delete item

## 💡 Usage Examples

### 1. Get Authentication Token
```bash
curl -X POST http://127.0.0.1:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "your_username", "password": "your_password"}'
```

### 2. Create New Item (with token)
```bash
curl -X POST http://127.0.0.1:8000/api/webapp/ \
  -H "Authorization: Token your_token_here" \
  -H "Content-Type: application/json" \
  -d '{"name": "Test Item", "description": "This is a test item"}'
```

### 3. Get All Items
```bash
curl -X GET http://127.0.0.1:8000/api/webapp/ \
  -H "Authorization: Token your_token_here"
```

### 4. Update Item
```bash
curl -X PUT http://127.0.0.1:8000/api/webapp/1/ \
  -H "Authorization: Token your_token_here" \
  -H "Content-Type: application/json" \
  -d '{"name": "Updated Item", "description": "Updated description"}'
```

## 🔐 Authentication

This project uses **Token Authentication** for secure API access:

1. **Get Token:** Send POST request to `/api/token/` with username and password
2. **Use Token:** Include token in Authorization header: `Authorization: Token your_token_here`
3. **Refresh Token:** Use `/api/token/refresh/` to get new token

### Example Authentication Flow:
```python
import requests

# Step 1: Get token
response = requests.post('http://127.0.0.1:8000/api/token/', {
    'username': 'your_username',
    'password': 'your_password'
})
token = response.json()['access']

# Step 2: Use token for API calls
headers = {'Authorization': f'Token {token}'}
response = requests.get('http://127.0.0.1:8000/api/webapp/', headers=headers)
```

## 🎓 Learning Path

### For Beginners:
1. **Start with Models** - Understand database structure in `models.py`
2. **Learn Serializers** - See how data is formatted in `serializers.py`
3. **Study Views** - Understand API logic in `views.py`
4. **Explore URLs** - Learn routing in `urls.py`
5. **Test APIs** - Use the examples above to test endpoints

### For Intermediate Developers:
1. **Customize Models** - Add new fields and relationships
2. **Extend Serializers** - Add validation and custom methods
3. **Create New Views** - Implement custom business logic
4. **Add Authentication** - Implement custom authentication
5. **Optimize Performance** - Add caching and database optimization

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch:** `git checkout -b feature/amazing-feature`
3. **Commit your changes:** `git commit -m 'Add amazing feature'`
4. **Push to the branch:** `git push origin feature/amazing-feature`
5. **Open a Pull Request**

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Django REST Framework team for the amazing framework
- Django community for excellent documentation
- All contributors who help improve this project

## 📞 Support

If you have any questions or need help:
- Create an [Issue](https://github.com/Sani-Yadav/DRF-Practice-API/issues)
- Check the [Django REST Framework documentation](https://www.django-rest-framework.org/)
- Join the [Django community](https://www.djangoproject.com/community/)

---

**Happy Coding! 🚀**

*Made with ❤️ for the Django community*
