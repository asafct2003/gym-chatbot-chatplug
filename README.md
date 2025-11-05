# Chatplug.ai – Gym Membership Bot (Flask Demo)

A portfolio-ready chatbot demo for a gym built by Chatplug.ai.  
This chatbot answers FAQs and collects leads for free trial bookings.

## ✅ Features
- Chat UI with instant reply
- Sends gym plans, timings, facilities info
- Books free trial with name & phone
- Stores leads in `/data/leads.csv`
- Fully offline – no OpenAI API needed

## ▶ How to Run
```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux
pip install flask
python app.py
