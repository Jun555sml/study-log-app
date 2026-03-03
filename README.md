# Study Log App – Full-Stack Web Application
A secure full-stack web application built with Flask that enables users to track and manage their English study sessions efficiently.

## Overview
Study Log App is a secure full-stack web application that allows users to record, manage, and review their English study sessions.

The system supports user registration and authentication, and enables users to log study activities including category, content, notes, and study duration. All data is stored in a relational SQLite database and isolated per user to ensure privacy and security.

The project focuses on backend fundamentals, including authentication, relational database design, and full CRUD functionality.

## Features
- Secure user registration and login system
- Password hashing for credential protection
- Session-based authentication and route protection
- Full CRUD operations for study logs
- Per-user data isolation and authorization checks
- Automatic total study time calculation

## Tech Stack
- Backend: Python, Flask
- Database: SQLite
- Frontend: HTML, Jinja2, Bootstrap
- Security: Password hashing, session management

## Architecture & Design
- Designed relational database schema with one-to-many relationship (Users → Logs)
- Implemented foreign key constraints to maintain data integrity
- Applied separation of concerns (authentication, database logic, UI rendering)
- Enforced authorization checks to prevent unauthorized data access

## Database Design
The application uses SQLite as a relational database to store and manage user data.
The schema is designed with a clear one-to-many relationship between users and study logs to ensure data integrity and proper user isolation.

### Users
- id (primary key)
- username
- hash (Password hash)

### Logs
- id (primary key)
- user_id (foreign key)
- category
- content
- note
- minutes
- timestamp

The database schema defines a one-to-many relationship between Users and Logs, enforced through a foreign key constraint to maintain referential integrity.

## Design Decisions

- Separated Users and Logs into distinct tables to normalize data and ensure scalability.
- Enforced foreign key constraints to maintain referential integrity and prevent orphan records.
- Implemented session-based authentication with route protection to secure user-specific data.
- Applied Bootstrap to ensure responsive UI design and consistent component styling.

## Challenges
- Implementing secure authentication and preventing cross-user data access
- Managing session state and authorization checks for edit/delete operations
- Ensuring database consistency while handling user-generated data

## Future Improvements
- Study progress visualization (graphs)
- Weekly/monthly analytics
- Goal-setting functionality
- Email reminders
- UI improvements (dark mode)

## Project Structure
- app.py: Main Flask application
- templates/: HTML templates
- static/: CSS and assets
- requirements.txt: Python dependencies
  
## How to Run
1. Clone the repository
```bash
git clone https://github.com/Jun555sml/study-log-app.git
cd study-log-app
```

2. Install dependencies
```bash
pip3 install -r requirements.txt
```

3. Set environment variable (Mac / Linux)
```bash
export FLASK_APP=app.py
```

If you are using Windows:
```bash
set FLASK_APP=app.py
```

4. Run the application
```bash
flask run
```

5. Open in your browser:
```
http://127.0.0.1:5000
```

## Video Demo
https://youtu.be/mHmEU13_KvM
