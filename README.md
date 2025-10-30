# 📸 GalleryApp

A simple full-stack **photo gallery application** built with **Django (backend)** and **React (frontend)**.  
Users can upload, view, and manage their images in an interactive gallery interface.

---

## 🚀 Features

- Upload and display photos dynamically  
- Organized gallery layout  
- Django REST Framework backend API  
- React frontend with responsive design  
- Static files handled with `collectstatic`  
- SQLite database for development  

---

## 🧱 Tech Stack

**Frontend:**  
- React (Vite or Create React App)  
- HTML, CSS, JavaScript  

**Backend:**  
- Django  
- Django REST Framework  

**Database:**  
- SQLite (default)  

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/tareq2007/GalleryApp.git
cd GalleryApp
2. Backend setup
bash
Copy code
# Create virtual environment
python -m venv venv
source venv/bin/activate   # (Windows: venv\Scripts\activate)

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start Django server
python manage.py runserver
3. Frontend setup (if React is in a subfolder)
bash
Copy code
cd frontend   # or the folder where package.json is located
npm install
npm run dev   # or npm start
📂 Project Structure
csharp
Copy code
GalleryApp/
├── manage.py
├── db.sqlite3
├── requirements.txt
├── static/
├── staticfiles/
├── templates/
├── photo/              # Django app
├── node_modules/
├── package.json
└── frontend/           # (if exists - React frontend)
🧪 Development Notes
Run python manage.py collectstatic before deployment.

Make sure CORS is enabled if frontend and backend run separately.

Use .env file for secret keys and API URLs.

📜 License
This project is open source and available under the MIT License.

👨‍💻 Author
Tareq
GitHub Profile
