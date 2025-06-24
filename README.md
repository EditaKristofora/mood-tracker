# mood-tracker
# Mood Tracker App

Track your daily moods and thoughts with ease — a full-stack web app built with FastAPI and deployed on Render, featuring a capybara-themed frontend hosted on GitHub Pages.

---

## Live Demo

👉 **Frontend (GitHub Pages)**: [https://editakristofora.github.io/mood-tracker/](https://editakristofora.github.io/mood-tracker/)  
👉 **Backend (FastAPI on Render)**: [https://mood-tracker-backend-2s24.onrender.com](https://mood-tracker-backend-2s24.onrender.com)

---

## Tech Stack

- **Frontend**: HTML, Tailwind CSS, JavaScript (Vanilla)
- **Backend**: Python, FastAPI
- **Auth & Database**: Supabase
- **Hosting**: 
  - Frontend: GitHub Pages  
  - Backend: Render

---

## Features

- ✅ Sign up and log in securely (Supabase Auth)
- ✅ Log your mood with optional notes
- ✅ View mood history with timestamps
- ✅ Capybara images that reflect each mood 😄😢😡😐😰
- ✅ Mobile-friendly and responsive layout
- 🔜 Mood analytics & statistics (coming soon)

---

##  Folder Structure
mood-tracker/
├── backend/ # FastAPI backend
│ ├── app/
│ │ ├── routes/ # auth.py, mood.py
│ │ ├── dependencies/ # auth dependency
│ │ └── supabase_client.py
│ └── main.py # FastAPI app with CORS + router
├── docs/ # Frontend (GitHub Pages)
│ ├── index.html
│ └── mood-images/ # capybara mood illustrations
└── README.md # ← you're here

---

## Running Locally

### 1. Clone the repo
```bash
git clone https://github.com/EditaKristofora/mood-tracker.git
cd mood-tracker
cd backend #set up virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
# or venv\Scripts\activate on Windows
pip install -r requirements.txt
SUPABASE_URL=your_project_url #Add Supabase environment variables (create .env)

SUPABASE_KEY=your_service_role_or_anon_key
uvicorn main:app --reload #run the backend
#OPEN FRONTEND navigate to docs/index.html in your browser or from local server:
cd docs
python -m http.server 8000

#INGOING PROCESS MOOD ANALYTICS 
#Author
#Edita Kristofora 
#Aspiring Data Engineering and full stack Developer