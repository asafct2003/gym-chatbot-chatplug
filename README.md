# 💪 Chatplug.ai – Gym Membership Chatbot (Flask + Dark/Light Mode)

An interactive AI-style chatbot built using Flask for a gym business.  
This bot answers FAQs (plans, timings, trainers), provides gym details, allows users to book free trial sessions, and stores leads in a CSV file.

It includes a modern UI with Dark/Light mode, chat interface, responsive layout, and is perfect for portfolio or client projects.

---

## 📌 Features

✅ AI-style chatbot using Flask (rule-based)  
✅ Dark Mode + Light Mode toggle (with saved preference)  
✅ Beautiful chat UI with quick replies  
✅ Lead collection form (Name, Phone, Plan, Time)  
✅ Saves leads to data/leads.csv  
✅ Fully Offline – No API required  
✅ Mobile-Responsive layout  
✅ Highly customizable for any business (gym, salon, café)

---

## 📁 Folder Structure

chatplug-gym-bot/  
│── app.py                  → Flask backend  
│── README.md               → Documentation  
│── requirements.txt        → Dependencies (optional)  
│  
├── templates/  
│   └── index.html          → Chat UI structure  
│  
├── static/  
│   ├── style.css           → Dark/Light Theme + UI styles  
│   └── script.js           → Chat logic + Theme switch + Form  
│  
├── data/  
│   ├── faq.json            → All chatbot FAQ replies  
│   └── leads.csv           → Saved customer leads (auto-generated)  
│  
└── screenshots/            → (You will upload screenshots here)

---

## 🚀 How to Run the Project

### 1️⃣ Clone Repository
git clone https://github.com/your-username/your-repo-name.git  
cd your-repo-name

### 2️⃣ Create Virtual Environment
python -m venv venv

Activate on Windows:  
venv\Scripts\activate

Activate on Mac/Linux:  
source venv/bin/activate

### 3️⃣ Install Flask
pip install flask

(Optional if using requirements.txt)  
pip install -r requirements.txt

### 4️⃣ Run the App
python app.py

Now open your browser and go to:  
http://127.0.0.1:5000

---

## 💬 Chatbot Usage

Try typing:
- hi  
- plans  
- timings  
- trainers  
- location  
- trial  

To book a free trial session:
Type "trial" → Fill Name, Phone, Plan, Time.

Lead details will be saved to:  
data/leads.csv

---

## 🛠 Customization Guide

| What to customize | File to edit           |
|-------------------|--------------------------|
| Gym name, location, phone | app.py (BUSINESS section) |
| FAQ answers (plans, timings) | data/faq.json |
| Logo in header | Replace static/logo.png |
| Colors / Dark–Light Mode | static/style.css |
| Chat logic / form functions | static/script.js |

---

## 📸 Screenshots

(Add your own screenshots after pushing to GitHub)

Example:
![Light Mode]([screenshots/light-mode.png](https://drive.google.com/file/d/1HoUoRukFkXDbVYRQyjSklp1HvGB3KOgO/view?usp=drive_link))  
![Dark Mode]([screenshots/dark-mode.png](https://drive.google.com/file/d/1R3DZZ-YCgmzjNPrImBHq8GMYttl5H-o5/view?usp=drive_link))  
![Lead Form]([screenshots/lead-form.png](https://drive.google.com/file/d/1zTE5Py3AJJnEH8KBF5JnOjwr8YQyfkk4/view?usp=drive_link))

---

## 🌟 Future Improvements (Optional)

✔ Connect with ChatGPT (OpenAI API)  
✔ Deploy on Render / Railway / Vercel  
✔ Add WhatsApp / Instagram integration  
✔ Use database (MongoDB / Firebase) instead of CSV  
✔ Create admin dashboard to view leads

---

## 👨‍💻 Developed By

Chatplug.ai – AI Chatbot & Automation Agency  
Developer: Your Name (Asaf)  
Instagram / Portfolio: Add your link here

---

## 📄 License

This project is free for personal use, learning, and portfolio presentation.  
Credit to Chatplug.ai is appreciated if used commercially.


