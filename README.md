# Employee Leave Management Backend (Django REST API)

A backend system built with **Django REST Framework** to manage employee leave requests, permissions, and role-based access control.  
The system supports employees submitting leave requests, while HR users can review, filter, and update them.

---

## Table of Contents

- [Features](#features)
- [Project Structure](#Project-Structure)
- [Prerequisites](#Prerequisites)
- [Installation](#Installation)
- [Environment Variables](#Environment-Variables)
- [Usage](#Usage)
- [API Overview](#API-Overview)
- [URLs Map](#URLs-Map)    

---

## Features

### Employee Features
- Submit leave requests
- Automatically receive a default **pending** status
- Only see their own leave requests
- Cannot modify other users' data

### HR Features
- View **all** leave requests
- Update leave status (approve/reject)
- Filter by employee_id, status, leave type
- Paginated results
- Full control panel for managing employees and companies

### System Features
- Authentication using Django sessions
- Role-based permissions (`IsHR`)
- Prevent overlapping leave
- Sync employees through API or command:
  ```
  python manage.py sync_employees
  ```

---

## Project Structure
```
api/
 ├── management/
 │    └── commands/sync_employees.py
 ├── models/
 │    ├── company.py
 │    ├── employee.py
 │    └── leave_request.py
 ├── permissions/
 │    └── hr_permissions.py
 ├── serializers/
 │    ├── employee.py
 │    └── leave_request.py
 ├── views/
 │    ├── authenticate.py
 │    ├── base.py
 │    ├── companies.py
 │    └── leaves_requests.py
 └── urls.py

```

---

## Prerequisites
- Python 3.10+
- PostgreSQL or SQLite
- Docker, Docker Compose

---

## Installation

```bash
git clone https://github.com/Ahmed-Elatar/Employee-Leave-Management-Backend.git
cd Employee-Leave-Management-Backend
```

```bash
docker compose up --build
```

---

## Environment Variables

```
DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///db.sqlite3
```

---

## Usage

Admin Panel:
```
http://localhost:8000/admin/
```

---

## Endpoints Summary

| Action | User | Endpoint |
|--------|--------|------------|
| Submit leave | Employee | POST /my-leave-requests/ |
| View own leaves | Employee | GET /my-leave-requests/ |
| View all leaves | HR | GET /leave-requests/ |
| Filter leaves | HR | GET /leave-requests/?status=pending&employee_id=3 |
| Update request | HR | PUT /leave-requests/<id>/ |
| Employee sync | Admin | POST /api/employees/sync/ |
| Management sync | Admin | python manage.py sync_employees |

---

## API Overview

### Employee – Create Leave
```json
{
  "leave_type": "sick",
  "start_date": "2025-11-25",
  "end_date": "2025-11-28"
}
```

### HR – Update Leave
```json
{
  "status": "approved"
}
```

---

## URLs Map
- /admin/
- /singin/
- /login/
- /my-leave-requests/
- /leave-requests/
- /leave-requests/<id>/

---
