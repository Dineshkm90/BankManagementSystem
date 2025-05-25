# BankManagementSystem
DASSBank – Bank Management System
📌 Project Overview:
DASBank is a full-stack web application designed to simulate real-world online banking features. 
It allows users to register, log in, view account details, perform credit and debit operations, and track their transaction history. 
The system is built using:

- Frontend: HTML, CSS, Bootstrap (for user interface)
- Backend: Python with the Flask framework (for logic and processing)
- Database: SQLite (for storing user and transaction data)

This project helps users and developers understand how an actual online banking system is structured and operated using modern web technologies.

🌐 Frontend (Client-Side)
Technologies Used:
- HTML – For structure of web pages.
- CSS – For styling and layout.
- Bootstrap – For responsive design and UI components.
- JavaScript (optional) – For animations, sliders, and dark mode.

Pages Included:
- Home Page (bank_app.html) – Introduction to the bank, services, contact, and testimonials,follow.
- Register/Login Page – Allows new users to sign up and existing users to log in securely.
- Dashboard Page – Displays user details, account number, current balance.
- Transaction Page – Perform credit and debit actions.
- History Page – View list of all past transactions.
- Contact Page – Information to reach the bank.

Key Features:
- Mobile responsive UI
- Animated elements and interactive features


🧠 Backend (Server-Side)
Technology Used:
- Python (Flask framework)

Responsibilities:
- Handling URL routing (@app.route)
- Receiving and validating user input (login, register, transactions)
- Managing user sessions (login/logout)
- Communicating with the database (read/write)
- Rendering HTML templates with data (using Jinja2)

Key Backend Functionalities:
- Register users with secure credentials
- Authenticate login credentials
- Process credit and debit transactions
- Display user details from database
- Manage session login/logout state

🗄️ Database (SQLite)
Structure:
users table:
- id, username, password, email, phone, account_number, balance

in DASS BANK transactions table:
 account_number(unique), type (credit/debit), amount, timestamp

Operations:
- Store new users during registration
- Validate login credentials
- Update balance during credit/debit
- Log each transaction with timestamp
- Retrieve data for dashboard and history pages

💡 Why This Project is Helpful
1. Educational Value: Teaches full-stack web development using Flask and SQLite.
2. Real-World Simulation: Mimics real banking functionalities.
3. Modular Code Structure: Organized for easy understanding and future expansion.
4. Security Awareness: Involves password handling and session management.
5. UI/UX Practice: Enhances frontend skills with real use cases.


