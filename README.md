# Study Log App

## Description
Study Log App is a web-based application designed to help users systematically track and improve their English study activities. The main goal of this project is to provide a simple but effective platform where learners can record their daily study efforts and monitor their progress over time.

As someone who is learning English and preparing for exams such as TOEIC and IELTS, I wanted to create a tool that makes it easy to log vocabulary practice, listening sessions, speaking exercises, and other study activities. Instead of using paper notes or scattered apps, this application centralizes all study records in one place.

Users can create an account, log in securely, and record their study sessions. Each log includes a category (such as vocabulary, listening, speaking, or reading), content description, optional notes, and the number of minutes studied. The application then stores this information in a SQLite database and allows users to review their study history and total study time.

The main focus of this project is user authentication, database design, and CRUD functionality (Create, Read, Update, Delete). Each user can only access and modify their own data, ensuring privacy and data security.

## Features
- User registration and login system
- Password hashing for security
- Session-based authentication
- Add study logs (category, content, note, minutes)
- Edit existing study logs
- Delete study logs
- View complete study history
- Calculate and display total study time
- User-specific data protection

## Technologies
- Python
- Flask
- SQLite
- HTML / Jinja
- Bootstrap
- CS50 SQL library

## Database Design
The application uses SQLite as its database. There are two main tables:

### Users table
- id
- username
- hash (password hash)

### Logs table
- id
- user_id (foreign key)
- category
- content
- note
- minutes
- timestamp

The relationship between users and logs is one-to-many. One user can have multiple study logs, but each log belongs to only one user.

## Design Decisions
One important design decision was separating users and logs into different tables and linking them with a foreign key. This ensures proper data organization and allows multiple users to use the application independently.

Another decision was using session-based authentication to protect user routes. This prevents unauthorized access to other users’ data.

Bootstrap was used to improve the user interface and make the application visually clean and responsive.

## Challenges
One of the main challenges was implementing secure authentication and ensuring that users cannot access or modify other users’ data. Handling database queries correctly and managing user sessions required careful attention.

Another challenge was implementing edit and delete functionality while maintaining proper authorization checks.

## Future Improvements
In the future, I would like to add:
- Graphs to visualize study progress
- Monthly or weekly summaries
- Goal-setting functionality
- Email reminders
- Dark mode UI


## Files
- app.py: Main Flask application
- templates/: HTML templates
- project.db: SQLite database
- static/: CSS and assets (if any)

## How to Run
1. Install requirements
2. Run `flask run`
3. Open `http://127.0.0.1:5000` in a browser

## Video Demo
https://youtu.be/mHmEU13_KvM
