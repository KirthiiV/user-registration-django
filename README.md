Django User Registration System

This project is a simple Django-based User Registration Application that demonstrates how to create forms, validate data, and store it in a database using Django Models and Forms. It also includes backend validation, dynamic rendering, and CRUD operations.

Features: 
1. User registration using Django ModelForm
2. Form validation (ex: Age cannot be zero or negative)
3. Stores data in SQLite/MySQL (depends on your configuration)
4. Displays registered users in a table format
5. Basic boolean field usage (is_active, is_verified, etc.)
6. Django Template rendering
7. Error and success message handling

Tech Stack:
| Technology   | Usage                     |
| ------------ | ------------------------- |
| Python       | Programming Language      |
| Django       | Backend Web Framework     |
| HTML, CSS    | UI Templates              |
| SQLite/MySQL | Database                  |
| Git & GitHub | Version Control & Hosting |


Installation and set-up:
Clone the repository:
git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
cd YOUR-REPO-NAME


Create a virtual environment:
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

Install Dependencied:
pip install -r requirements.txt


Run Migrations:
python manage.py makemigrations
python manage.py migrate


Run the server:
python manage.py runserver


Author

Kirthika V
Python & Django Developer

📧 Email: kirthiii.v@gmail.com

🌍 GitHub: https://github.com/KirthiiV/

License:

This project is open-source and available under the MIT License.
