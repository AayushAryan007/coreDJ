# 🍲 Recipe Manager

A modern, user-friendly Django web application for managing personal recipes. Share your culinary creations, organize your favorite dishes, and discover new recipes in a secure, personalized environment.

## ✨ Features

- **User Authentication**: Secure registration and login system
- **Personal Recipe Management**: Create, read, update, and delete your own recipes
- **Image Upload**: Add beautiful images to your recipes
- **Search Functionality**: Quickly find recipes by name
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **User Isolation**: Each user sees only their own recipes

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Django 5.2+
- SQLite (default) or PostgreSQL/MySQL

### Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd recipe-manager
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install django
   ```

4. **Run migrations**

   ```bash
   python manage.py migrate
   ```

5. **Start the development server**

   ```bash
   python manage.py runserver
   ```

6. **Open your browser**
   Navigate to `http://127.0.0.1:8000/`

## 📱 Usage

### User Registration

- Visit the registration page
- Fill in your details (first name, last name, username, password)
- Click "Register" to create your account

### Adding Recipes

- Log in to your account
- Click "Add Recipe" on the recipes page
- Fill in recipe name, description, and upload an image
- Save your recipe

### Managing Recipes

- View all your recipes on the main page
- Use the search bar to find specific recipes
- Edit or delete recipes using the action buttons

### Logging Out

- Click the "Logout" button to securely log out of your account

## 🏗️ Project Structure

```
recipe-manager/
├── core/                    # Main Django project settings
│   ├── settings.py         # Project configuration
│   ├── urls.py             # URL routing
│   └── wsgi.py             # WSGI configuration
├── vege/                    # Main app for recipes
│   ├── models.py           # Database models
│   ├── views.py            # View functions
│   ├── templates/          # HTML templates
│   └── migrations/         # Database migrations
├── accounts/                # User management app
├── home/                    # Home page app
├── media/                   # Uploaded images
├── static/                  # Static files (CSS, JS)
└── manage.py               # Django management script
```

## 🔧 Configuration

### Database

The project uses SQLite by default. To use a different database:

1. Install the appropriate database adapter (e.g., `pip install psycopg2` for PostgreSQL)
2. Update `core/settings.py` with your database configuration

### Media Files

Uploaded images are stored in the `media/` directory. In production, configure your web server to serve these files.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Django framework for the robust backend
- Built with love for food enthusiasts everywhere

---

**Happy cooking! 🍳**
