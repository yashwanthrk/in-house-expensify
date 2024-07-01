# In-House Project

## Project Structure

```
in_house/
├── manage.py
├── in_house/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── expenses/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── requirements.txt
```

## Requirements

- Python 3.8+
- Django 3.2.14
- Django REST Framework 3.12.4
- OpenAI 0.27.0

## Setup

1. **Clone the Repository:**

   ```sh
   git clone <repository_url>
   cd in_house
   ```

2. **Create and Activate Virtual Environment:**

   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

## Running the Project

1. **Apply Migrations:**

   ```sh
   python manage.py migrate
   ```

2. **Run the Development Server:**

   ```sh
   python manage.py runserver
   ```

## Testing

To run tests:

```sh
python manage.py test
```

## Notes

Ensure that your `settings.py` is configured properly for your database and other settings.
