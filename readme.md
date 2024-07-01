
## Project Structure

in_house/
├── manage.py
├── in_house/
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── expenses/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── serializers.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
└── requirements.txt


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
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
 
