# Vieira Tech Console Backend

## Overview

Vieira Tech Console Backend is a Django-based web application designed to manage customers, devices, and printers. The project follows a modular architecture with three main apps: `customers`, `devices`, and `printers`. It uses PostgreSQL as the database (via Docker) and is styled with Bootstrap for a modern, AWS Console-inspired UI.

---

## Table of Contents
1. [Project Structure](#project-structure)
2. [Setup & Installation](#setup--installation)
3. [Configuration](#configuration)
4. [Apps & Features](#apps--features)
    - [Customers](#customers)
    - [Devices](#devices)
    - [Printers](#printers)
5. [Models](#models)
6. [Views & URLs](#views--urls)
7. [Templates & UI](#templates--ui)
8. [Database & Docker](#database--docker)
9. [Testing](#testing)
10. [Contributing](#contributing)
11. [License](#license)

---

## 1. Project Structure

```
wsBackend-Fabrica25.2/
├── customers/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations/
│   ├── models.py
│   ├── templates/
│   │   └── customers/
│   │       ├── base.html
│   │       ├── customer_confirm_delete.html
│   │       ├── customer_detail.html
│   │       ├── customer_form.html
│   │       └── customer_list.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── devices/
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── printers/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── __init__.py
├── docker-compose.yml
├── manage.py
├── pyproject.toml
├── README.md
└── uv.lock
```

---

## 2. Setup & Installation

### Prerequisites
- Python >= 3.10
- Docker (for PostgreSQL)
- pip

### Install Dependencies
```sh
pip install -r requirements.txt
```
Or, if using `pyproject.toml`:
```sh
pip install django psycopg[binary] requests
```

### Database Setup (Docker)
Start PostgreSQL with Docker:
```sh
docker-compose up -d
```

### Django Migrations
```sh
python manage.py migrate
```

### Run the Development Server
```sh
python manage.py runserver
```

---

## 3. Configuration

- **Settings:** All main settings are in `printers/settings.py`.
- **Database:** PostgreSQL, configured via Docker Compose.
- **Installed Apps:** `customers`, `devices`, Django core apps.
- **Templates:** Uses Django templates with Bootstrap CDN.

---

## 4. Apps & Features

### Customers
- CRUD for customer records
- Fields: CNPJ, company name, phone, email, timestamps
- Bootstrap-styled forms and lists

### Devices
- Device management (under construction)
- Placeholder in sidebar with construction icon

### Printers
- Printer management (under construction)
- Placeholder in sidebar with construction icon

---

## 5. Models

### Example: Customer Model (`customers/models.py`)
```python
class Customer(models.Model):
    cnpj = models.CharField(max_length=18)
    company_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

---

## 6. Views & URLs

- **Class-based views** for CRUD operations (ListView, CreateView, DetailView, UpdateView, DeleteView)
- **URLs** defined in each app (`urls.py`)
- Example (`customers/urls.py`):
```python
urlpatterns = [
    path('', CustomerListView.as_view(), name='customer_list'),
    path('add/', CustomerCreateView.as_view(), name='customer_add'),
    path('<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),
    path('<int:pk>/edit/', CustomerUpdateView.as_view(), name='customer_edit'),
    path('<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer_delete'),
]
```

---

## 7. Templates & UI

- All templates use Bootstrap via CDN for styling
- Main layout in `base.html` (sidebar, navbar, AWS Console style)
- Customer templates:
    - `customer_list.html`: Table of customers, Add button
    - `customer_detail.html`: Details view
    - `customer_form.html`: Add/Edit form
    - `customer_confirm_delete.html`: Delete confirmation
- Sidebar icons indicate sections under construction

---

## 8. Database & Docker

- **Database:** PostgreSQL
- **Docker Compose:**
```yaml
services:
  db:
    image: postgres
    environment:
      POSTGRES_PASSWORD: postgres
      POSTGRES_USER: postgres
      POSTGRES_DB: printers
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data
volumes:
  pgdata:
```

---

## 9. Testing

- Unit tests in each app (`tests.py`)
- Run all tests:
```sh
python manage.py test
```

---

## 10. Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Commit with semantic messages (e.g., `feat: add customer CRUD`)
5. Push and create a pull request

---

## 11. License

Specify your license here (e.g., MIT, GPL, etc.)

---

## Additional Notes
- Devices and Printers modules are under development (indicated by sidebar icons)
- For advanced configuration, see `printers/settings.py`
- For UI customization, edit templates in `customers/templates/customers/`

---

For any questions or issues, please contact the repository owner.
