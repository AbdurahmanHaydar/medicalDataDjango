# Medical records management system using Django.

## Introduction
This is the backend for the medical records management system.

## Prerequisites
- Python 3.x
- pip
- Virtualenv (optional but recommended)

## Installation

1. **Clone the Repository**


git clone https://github.com/AbdurahmanHaydar/medicalDataDjango.git

cd medicalDataDjango

2. **Set up a Python Virtual Environment (Optional but recommended)**

python3 -m venv venv

source venv/bin/activate


3. **Install Dependencies**
pip install -r requirements.txt


4. **Set up Database (if applicable)**
python manage.py migrate


5. **Running the Server**

To run the server, execute:

python manage.py runserver



This will start the development server on http://127.0.0.1:8000/.

## Running Tests

To run tests with pytest, use the following commands:

$export DJANGO_SETTINGS_MODULE=medidata.settings

$pytest


## Additional Notes
