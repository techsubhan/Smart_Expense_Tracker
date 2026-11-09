from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "super_secret_key" 

# --- DATA STORAGE ---
users_db = {} 
expenses_db = []

# Added 'name' and 'budget_limit' to prevent UndefinedError in HTML
user_data = {
    "name": "Expense Tracker", 
    "income": 120000,
    "budget_limit": 50000
} 

# --- OOP CLASSES ---
class Transaction:
    def __init__(self, title, amount, date):
        self.title = title
        self.amount = amount
        self.date = date

class Expense(Transaction):
    def __init__(self, title, amount, category, date):
        super().__init__(title, amount, date)
        self.category = category

# --- ROUTES ---

@app.route("/")
def index():
    if "user" in session:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("username")
        pwd = request.form.get("password")
        if email in users_db:
            return "User already exists! <a href='/signup'>Try again</a>"
        users_db[email] = pwd
        return redirect(url_for("login"))
    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("username")
        pwd = request.form.get("password")
        if email in users_db and users_db[email] == pwd:
            session["user"] = email
            return redirect(url_for("dashboard"))
        else:
            return "Invalid Credentials! <a href='/login'>Try again</a>"
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    
    total_spent = sum(float(item.amount) for item in expenses_db)
    total_income = user_data["income"]
    
    return render_template("index.html", 
                           items=expenses_db, 
                           total_spent=total_spent, 
                           total_income=total_income,
                           user=user_data)

# --- UPDATE INCOME ROUTE ---
@app.route("/update_income", methods=["POST"])
def update_income():
    if "user" in session:
        new_income = request.form.get("income")
        if new_income:
            user_data["income"] = float(new_income)
    return redirect(url_for("dashboard"))

# --- NEW: UPDATE BUDGET LIMIT ROUTE ---
@app.route("/update_budget", methods=["POST"])
def update_budget():
    if "user" in session:
        new_limit = request.form.get("budget_limit")
        if new_limit:
            # user_data mein budget limit update kar rahe hain
            user_data["budget_limit"] = float(new_limit)
    return redirect(url_for("dashboard"))

@app.route("/add", methods=["POST"])
def add_expense():
    title = request.form.get("title")
    amount = request.form.get("amount")
    category = request.form.get("category")
    date = request.form.get("date")

    if title and amount:
        new_expense = Expense(title, float(amount), category, date)
        expenses_db.append(new_expense)
    
    return redirect(url_for("dashboard"))

@app.route("/delete/<int:index>")
def delete_expense(index):
    if "user" in session:
        if 0 <= index < len(expenses_db):
            expenses_db.pop(index)
    return redirect(url_for("dashboard"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)