# Authentication System in Django

This project implements an authentication system using the Django framework. It provides functionality for user login, logout, and registration, as well as email-based verification during user registration.

## Features

- **User Registration:** New users can sign up by providing a username, email, and password. Their information is saved in the database.
- **Email Verification:** Upon registration, users receive a confirmation email to verify their email address.
- **Login and Logout:** Registered users can log in and log out of their accounts securely.
- **Error Handling:** The system includes error handling for scenarios like invalid login credentials or duplicate user registration.

## Installation

### Prerequisites

Ensure you have the following installed on your system:

- Python (3.8 or higher)
- Django (4.0 or higher)
- A virtual environment tool (optional but recommended)

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/GHILENISABEUR/authentication_system_django.git
   cd authentication_system_django
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

6. Open your browser and navigate to:

   ```
   http://127.0.0.1:8000/
   ```

## Project Structure

```
.
├── authentication_system_django/
│   ├── settings.py       # Project settings
│   ├── urls.py           # URL routing
│   ├── wsgi.py           # WSGI configuration
│   └── asgi.py           # ASGI configuration
├── users/
│   ├── templates/        # HTML templates
│   ├── views.py          # View functions
│   ├── forms.py          # Django forms for user registration
│   └── models.py         # User models
├── static/               # Static files
├── templates/            # Project-wide templates
├── manage.py             # Django management script
├── db.sqlite3            # SQLite database
└── requirements.txt      # Python dependencies
```

## Configuration

1. **Email Settings:** Update the email backend settings in `settings.py` to enable email functionality. For example:

   ```python
   EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
   EMAIL_HOST = 'smtp.example.com'
   EMAIL_PORT = 587
   EMAIL_USE_TLS = True
   EMAIL_HOST_USER = 'your_email@example.com'
   EMAIL_HOST_PASSWORD = 'your_password'
   ```

2. **Database Configuration:** The default configuration uses SQLite. You can switch to a different database (e.g., PostgreSQL, MySQL) by updating the `DATABASES` setting in `settings.py`.

## Usage

- **Register a User:** Navigate to the registration page, fill in the details, and submit the form.
- **Verify Email:** Check your email for a verification link and click on it to activate your account.
- **Login:** Use your credentials to log in.
- **Logout:** Click on the logout button to end the session.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any questions or suggestions, feel free to reach out to Ghileni Saber at ghilenisaber191@gmail.com

---

Thank you for checking out this project! Feel free to star the repository if you find it useful.

README.md
Affichage de README.md en cours...
