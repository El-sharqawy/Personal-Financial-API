# Peronsal Financial API

## Description

a RESTful API that takes user income and expenses data to generate personalized financial reports

## Features

- **Purpose**: Streamlines personal and business finance management.
- **Core Features**: Manage income, expenses, and generate financial reports.
- **User-Friendly Interface**: Simple and intuitive design that makes The API accessible for everyone.
- **Technology**: Built with Django, follows RESTful principles.
- **Security:** Token-based authentication (JWT), encryption, role-based access control.
- **Scalability:** Designed for performance and scalability.

## Status

- under development, ready as base API.

## Getting Started

### Prerequisites

- Python 3.x
- Django
- Django REST Framework

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/El-sharqawy/Personal-Financial-API
   cd Personal-Financial-API
   ```

3. **Local Setup**:

   - Create a virtual environment:

   ```bash
   python -m venv venv
   .\.venv\Scripts\activate  # On Linux use `source .venv/bin/activate`
   ```

   - Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

   - Set up your database and update the settings in `settings.py` to connect to your database.

   - Run migrations:

   ```bash
   python manage.py migrate
   ```

   - Start the development server:

   ```bash
   python manage.py runserver
   ```

   - Access the application at `http://127.0.0.1:8000/`.

4. **API Documentation**:
   - Access the API Documentation at `http://localhost:8000/swagger`.

## Usage

1. Create user and setup balance
2. Create Income / Expenses Categories and fill the data
3. Make transactions to Track your Income/Expenses

## Contact

For questions or feedback, please reach out to:

- **Osama El-sharqawy** : [Github](https://github.com/El-sharqawy) - [LinkedIn](https://www.linkedin.com/in/osama-elsharqawy) - [email](elsharqawy2@gmail.com)
