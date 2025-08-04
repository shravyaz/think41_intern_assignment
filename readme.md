## 🔹 Milestone 1 – Database Creation

### 🎯 Objective
- Understand provided Excel files: `users.xlsx`, `orders.xlsx`
- Create SQLite database (`ecommerce.db`)
- Import both Excel sheets as tables

### ⚙️ Tools Used
- Microsoft Excel
- DB Browser for SQLite

### 🧪 Steps
1. Analyzed and cleaned `users.xlsx` and `orders.xlsx`
2. Created `user` and `orders` tables in SQLite
3. Imported both sheets using DB Browser
4. Ensured relationships (e.g., `user_id` foreign key)

### 🐞 Issue Faced
- Import button disabled in DB Browser
✅ Fixed by restarting and verifying column headers

---

## 🔹 Milestone 2 – Flask Backend

### 🎯 Objective
- Create Flask app (`app.py`) to serve customer data

### 🔌 API Endpoints

| Endpoint               | Description                            |
|------------------------|----------------------------------------|
| `/customers`           | Get all customers                      |
| `/customers/<user_id>` | Get specific customer + order count    |

### ⚙️ Tools Used
- Python 3, Flask, Flask-CORS, SQLite

### 🐞 Issues & Fixes
- ❌ `SyntaxError: unterminated string` — fixed DB path
- ❌ `git push` rejected — fixed with `--force`

---

## 🔹 Milestone 3 – Frontend UI

### 🎯 Objective
- Build basic frontend using HTML + JS
- Fetch data from Flask API
- Display customer list and details on click

### 📁 Key File: `templates/index.html`

### ✨ Features
- Loads all customers from `/customers`
- On click, fetches data from `/customers/<id>`
- Displays name, email, and order count

### 🐞 Issues
- Flask not routing `/` correctly — fixed by using `render_template()`
- Used browser DevTools to debug missing data

---
