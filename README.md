Chatplug.ai – Gym Membership Chatbot (Flask Project)

An interactive AI-style chatbot for gyms and fitness centers. This chatbot provides membership information, gym details, answers FAQs, and collects leads for free trial sessions.
It features a clean UI with Dark/Light mode, responsive chat interface, and CSV-based lead capture.


🧠 Features

✅ Chatbot answers FAQs:

Membership plans & pricing

Gym timings (weekday/weekend)

Amenities & trainers

Location & contact info

✅ Lead generation system:

Users can book Free Trial

Fills name, phone, plan, time slot

Saved to data/leads.csv

✅ Modern UI/UX:

Dark + Light Mode toggle 🌙☀️

Responsive chatbot layout

Smooth animations & quick replies

✅ Fully Offline / No API Required

✅ Built for portfolio use (can show to clients)




chatplug-gym-bot/
│── app.py                 # Flask backend
│── requirements.txt       # Dependencies
│── README.md              # Documentation
│
├── templates/
│   └── index.html         # Frontend UI
│
├── static/
│   ├── style.css          # Styling (Dark/Light Theme + Chat)
│   └── script.js          # Chat functionality + Form + Theme Toggle
│
├── data/
│   ├── faq.json           # Gym FAQs (Pricing, Timings, Trainers...)
│   └── leads.csv          # Auto-created when leads are submitted
│
└── screenshots/           # (You will upload screenshots here manually)
