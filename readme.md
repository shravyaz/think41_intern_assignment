## 🔹 Milestone 1 – Database Creation

### 🎯 Objective
- Understand provided Excel files: `users.xlsx`, `orders.xlsx`
- Create SQLite database (`ecommerce.db`)
- Import both Excel sheets as tables

  ![Screenshot 2025-08-04 111533.png](../../../../../../OneDrive/Pictures/Screenshots/Screenshot%202025-08-04%20111533.png)
- ![Screenshot 2025-08-04 111550.png](../../../../../../OneDrive/Pictures/Screenshots/Screenshot%202025-08-04%20111550.png)
- ![Screenshot 2025-08-04 111812.png](../../../../../../OneDrive/Pictures/Screenshots/Screenshot%202025-08-04%20111812.png)

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
## 🔹 Milestone 4 – Build Customer List Frontend

### 🎯 Objective

Enhance the frontend by building a full customer list interface that fetches data from the Flask backend and displays key information in a searchable, styled table.

---

### ✅ Features Implemented

| Feature                     | Description                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| 🔍 Search Functionality     | Real-time search by customer **name** or **email**                          |
| 📋 Customer List View       | Displayed in **table format** with name, email, and order count             |
| 🔗 API Integration          | Fetched data from `/customers` endpoint in Flask backend                    |
| 🎨 Basic Styling            | Applied simple CSS for professional presentation                           |
| 🔁 Dynamic Rendering        | Used JavaScript to populate table dynamically                              |
| ⚠️ Loading/Error Handling  | Showed loading message and error fallback if API call fails                |

---

### 🧪 Implementation Details

- Used **vanilla JavaScript** for frontend logic
- HTML file (`index.html`) is served using `render_template()` from Flask
- Used `fetch()` API to call backend `/customers` endpoint
- Implemented **client-side filtering** for search
- Handled network/API errors gracefully

---

### 📁 Files Involved

