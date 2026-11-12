# Budget Drishti | बजेट दृष्टि

**A Clear View of Public Budgets and Development.**

Budget Drishti is a Django-based academic e-governance prototype designed to make municipal budget information easier to understand, monitor development projects, and encourage citizen participation.

The platform brings together budget transparency, development project tracking, and citizen inquiries in one place.

## Important Notice

This project uses fictional **Sundarpur Municipality** demonstration data. Budget figures, expenditure values, and project information are illustrative and do not represent actual government records.

Some demonstration values may be based on general research references or estimated assumptions. Such values must be clearly distinguished from verified official statistics.

This is an academic prototype, not an official government platform.

## Key Features

- **Budget Dashboard:** View planned budget, estimated expenditure, utilization, and development projects.
- **Budget Overview:** Explore budget allocation by financial year and sector.
- **Development Projects:** Browse projects and monitor their progress.
- **Follow the Money:** Understand project allocation, expenditure, and physical progress.
- **Project Updates:** Allow assigned department officials and administrators to update project progress.
- **Citizen Participation:** Register, submit inquiries, and receive official-style responses.
- **Role-Based Access:** Separate permissions for citizens, department officials, and administrators.
- **Django Admin:** Manage users, budgets, departments, projects, and inquiries.

## Technology Stack

- Python
- Django
- HTML and CSS
- JavaScript
- Bootstrap 5
- Chart.js
- PostgreSQL

## Requirements

- Python 3.12 or newer (compatible with your installed Django version)
- pip
- PostgreSQL
- Internet connection for Bootstrap and Chart.js CDN assets

### Database Configuration

This project uses PostgreSQL.

Before running database migrations:

1. Install and start PostgreSQL.
2. Create a PostgreSQL database.
3. Create a `.env` file in the project root directory (the same folder as `manage.py`).
4. Add your database credentials:

```env
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=your_postgresql_port
```

Replace the example values with your own PostgreSQL details. Do not upload your `.env` file or share database credentials publicly.

## Windows PowerShell Setup

Clone or download the project and open its directory:

```powershell
cd path\to\NagarikBudgetWatch
```

Create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

Configure your database and environment variables in `.env` before running migrations.

Run migrations:

```powershell
python manage.py makemigrations
python manage.py migrate
```

Create an administrator account:

```powershell
python manage.py createsuperuser
```

Start the development server:

```powershell
python manage.py runserver
```

Open the website:

- Citizen website: http://127.0.0.1:8000/
- Django administration: http://127.0.0.1:8000/admin/

## First Use

1. Create a superuser.
2. Sign in through Django Admin.
3. Add or manage departments, budgets, financial years, and projects.
4. Register a normal account to explore the citizen experience.
5. To test official features, assign an appropriate role and department to a user through Django Admin.

## Demonstration Data Methodology

Budget Drishti is designed to demonstrate how public budget information can be presented in a simple and understandable way.

The demonstration dataset may include:

- General research references.
- Estimated community needs.
- Illustrative budget allocations.
- Assumed development project costs.
- Calculated expenditure and progress indicators.

Each estimated value should be accompanied by its source or calculation method, relevant date, assumptions, and limitations wherever applicable.

Estimated figures must never be presented as verified official government statistics.

## Future Improvements

- English and Nepali language options.
- Improved data-source documentation and verification.
- More detailed budget analysis and visualizations.
- Automated testing and audit logs.
- Source-document upload and verification workflow.
- Improved accessibility and responsive design.
- Security review and production deployment configuration.

---
Deployment configuration updated.

**Budget Drishti — Public Budget. Our Right.**