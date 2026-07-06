# 📊 UnitConverter - Premium Web Unit Converter

UnitConverter is a clean, minimalist, and responsive web-based unit converter built using Python (Flask), SQLite, and modern CSS3. It features an interactive tabbed layout for converting length, weight, height, and temperature, alongside a persistent database-backed history log.

---

## ✨ Features

- **💡 Multi-Category Conversions**:
  - **Length**: Kilometers (KM) ➔ Meters (M) and vice versa.
  - **Weight**: Grams (G) ➔ Kilograms (KG) and vice versa.
  - **Height**: Inches (IN) ➔ Centimeters (CM) and vice versa.
  - **Temperature**: Celsius (C) ➔ Fahrenheit (F) and vice versa.
- **🕒 Conversion History**: All successful conversions are logged in an SQLite database. You can view, search (via database logs), edit numeric values to recalculate results, or delete logs.
- **📋 Copy to Clipboard**: Quickly copy results using an interactive clipboard button that provides visual checkmark feedback.
- **🔒 Input Validation**: Fully validated forms on both index and edit pages to prevent server crashes on invalid entries.
- **🎨 Premium Minimalist UI**: Styled with a clean white dashboard layout, geometric typography (`Outfit`), subtle outline cards, and warm orange (`#f97316`) primary accent buttons.

---

## 🛠️ Tech Stack

- **Backend**: Python 3.10+, Flask
- **Database & ORM**: SQLite, Flask-SQLAlchemy
- **Migrations**: Flask-Migrate (Alembic)
- **Frontend**: HTML5, Vanilla JavaScript, CSS3 (Custom Variables, Light Theme, Responsive Design)

---

## 📂 Project Structure

```
unit_converter/
│
├── app.py                 # Application configuration, DB models, and Flask routes
├── migrations/            # Database migration scripts (Flask-Migrate)
├── instance/              # SQLite database storage directory (converter.db)
│
├── static/                # Static assets served by Flask
│   └── css/
│       └── style.css      # Core minimalist light-themed design stylesheet
│
└── templates/             # Jinja2 HTML templates
    ├── base.html          # Shared layout template (DRY architecture)
    ├── index.html         # Interactive category tabs & converter form
    ├── history.html       # Clean history logs table with category badges
    └── edit.html          # Clean dashboard card for editing records
```

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have **Python 3.10+** installed.

### 2. Install Dependencies
Run the following command to install the required packages:
```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate
```

### 3. Initialize the Database
If you are running the app for the first time, initialize and apply the database migrations:
```bash
flask db upgrade
```
*(Alternatively, Flask-SQLAlchemy will automatically create the SQLite database file on first run).*

### 4. Run the Application
Start the local development server:
```bash
python app.py
```

Open your browser and navigate to `http://127.0.0.1:5000` to start converting!

---

## 🤝 License
This project is open-source and available under the MIT License.
