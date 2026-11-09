# Smart Expense Tracker

A Flask-based web application designed to help users record daily expenses, monitor income, manage budget limits, and review their spending activity through a centralized dashboard.

## Overview

Smart Expense Tracker provides a simple and organized approach to personal expense management. The application allows users to create an account, access a dashboard, record expenses, manage income and budget limits, and review transaction history.

The interface is built with a dark-themed dashboard layout, providing quick access to expense management and financial summaries.

## Key Features

- **User Authentication:** Sign-up, login, and logout functionality.
- **Dashboard Overview:** Displays total income, total expenses, and remaining balance.
- **Expense Management:** Add and delete expense records.
- **Expense Categorization:** Organize expenses into Food, Travel, Bills, Shopping, and Other.
- **Income Management:** Update the total income value.
- **Budget Management:** Set and update a spending limit.
- **Budget Alerts:** Displays a warning when recorded expenses exceed the configured budget limit.
- **Expense History:** View recorded transactions in a structured table.
- **Search Functionality:** Search expense records by title or category.
- **Expense Reports:** Review recorded expenses and their overall total.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Flask | Backend web framework |
| HTML5 | Page structure |
| CSS3 | Styling and layout |
| JavaScript | Client-side interactions |
| Jinja2 | Dynamic HTML rendering |

## Project Structure

```text
Smart_Expense_Tracker/
│
├── .gitignore
│
└── frontend/
    ├── app.py
    ├── requirements.txt
    │
    ├── static/
    │   └── style.css
    │
    └── templates/
        ├── index.html
        ├── login.html
        └── signup.html
```

## Installation and Setup

Follow these steps to run the application locally.

### 1. Clone the Repository

```bash
git clone https://github.com/techsubhan/Smart_Expense_Tracker.git
```

### 2. Navigate to the Project Directory

```bash
cd Smart_Expense_Tracker/frontend
```

### 3. Create a Virtual Environment

```bash
python3 -m venv venv
```

### 4. Activate the Virtual Environment

**Linux / macOS:**

```bash
source venv/bin/activate
```

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 6. Run the Application

```bash
python app.py
```

### 7. Open in Browser

Visit:

```text
http://127.0.0.1:5000
```

Create an account and access the dashboard.

## Application Workflow

1. Register a user account.
2. Log in to access the dashboard.
3. Review the income, expense, and balance overview.
4. Add expenses with their title, amount, category, and date.
5. Update income and budget limits.
6. Review transaction history.
7. Search or delete recorded expenses.
8. Access the expense summary report.
9. Log out when finished.

## Current Implementation Notes

The current version uses in-memory Python data structures for storing users, expenses, income, and budget information.

Consequently, application data is not persistent and resets when the server restarts. The current implementation is intended as a functional project prototype rather than a production financial management system.

## Future Improvements

The following enhancements can extend the application's functionality:

- Integrate SQLite or another persistent database.
- Implement secure password hashing.
- Introduce user-specific expense records.
- Improve session and secret-key management.
- Add monthly and category-based expense analytics.
- Introduce graphical financial reports.
- Add expense editing and filtering options.
- Improve input validation and application security.

## License

This project is available for educational and learning purposes. A formal open-source license can be added when required.

---

**Smart Expense Tracker**  
Developed using Python and Flask.
