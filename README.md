# # 🧠 AI-Powered Resume Analyzer

A modern web application that uses AI to analyze resumes, provide detailed feedback, and recommend job opportunities based on your profile. Built with **Django (DRF)** on the backend and **Vue/Nuxt.js** on the frontend.

##  Demo Video
Youtube https://youtu.be/xOZ5xQMLJMs



## 🚀 Features

- 🔍 Resume parsing and keyword extraction
- 📋 Feedback on formatting, missing skills, and ATS (Applicant Tracking System) optimization
- 🤖 AI-powered recommendations
- 💼 Job suggestion system with match score visualization
- 📄 Supports PDF, DOCX, and TXT files
- 🧑‍💼 Admin dashboard (coming soon)

---

## 🛠 Tech Stack

### Frontend

- [Nuxt.js](https://nuxt.com/) (Vue 3)
- Tailwind CSS
- AOS (Animate on Scroll)
- Axios

### Backend

- Django
- Django REST Framework
- PyMuPDF / python-docx / OpenAI API (for parsing & AI)
- PostgreSQL

---

## 📸 Screenshots

![image](https://github.com/user-attachments/assets/b7e3648c-7d07-485d-960c-884006d667e3)
![image](https://github.com/user-attachments/assets/505455b8-7889-4754-8923-92448687b819)
![image](https://github.com/user-attachments/assets/5e6d2726-5e68-4db4-b774-95fdf6eed1f6)




---

## 📦 Installation

### 1. Backend (Django)

```bash
git clone https://github.com/yourusername/resume-analyzer.git
cd resume-analyzer/backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
### 2. Frontend (Nuxt)
```bash
cd resume-analyzer/frontend
npm install
npm run dev
```
