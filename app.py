from flask import Flask, render_template, request, jsonify
from datetime import datetime
import json, os, csv, re

app = Flask(__name__)

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
FAQ_PATH = os.path.join(DATA_DIR, 'faq.json')
LEADS_PATH = os.path.join(DATA_DIR, 'leads.csv')
BUSINESS = {
    "brand": "Chatplug.ai",
    "client": "FitPulse Gym",
    "location": "MG Road, Kozhikode",
    "phone": "+91 98765 43210",
    "hours": {
        "weekday": "6:00 AM – 10:00 PM",
        "weekend": "7:00 AM – 9:00 PM"
    }
}

with open(FAQ_PATH, 'r', encoding='utf-8') as f:
    KB = json.load(f)

# Simple intent rules
INTENTS = {
    'greet': [r"hi", r"hello", r"hey", r"namaste"],
    'pricing': [r"price", r"fees", r"cost", r"plan"],
    'timings': [r"time", r"timing", r"hours", r"open"],
    'location': [r"where", r"location", r"address", r"map"],
    'trainer': [r"trainer", r"coach", r"personal"],
    'amenities': [r"pool", r"steam", r"sauna", r"equipment", r"amenit"],
    'trial': [r"trial", r"free", r"demo"],
    'contact': [r"phone", r"call", r"contact"],
    'membership': [r"join", r"membership", r"enroll"],
    'cancel': [r"cancel", r"stop", r"nevermind"],
}

QUICK_REPLIES = [
    {"text": "Membership plans", "payload": "plans"},
    {"text": "Timings", "payload": "timings"},
    {"text": "Book free trial", "payload": "trial"},
]

def match_intent(text):
    t = text.lower()
    for name, patterns in INTENTS.items():
        for p in patterns:
            if re.search(p, t):
                return name
    return None

def kb_answer(intent):
    if intent == 'pricing':
        return KB['plans']
    if intent == 'timings':
        return KB['timings']
    if intent == 'location':
        return KB['location']
    if intent == 'trainer':
        return KB['personal_training']
    if intent == 'amenities':
        return KB['amenities']
    if intent == 'contact':
        return f"You can call us at {BUSINESS['phone']}. Or just share your number and we'll call you back."
    if intent == 'membership':
        return "Great! To start a membership, type ‘trial’ to book a free session or say which plan you want (Monthly/Quarterly/Yearly)."
    if intent == 'trial':
        return "Awesome! I can book a free trial workout. Please share: Name, Phone, Preferred time (morning/evening)."
    if intent == 'greet':
        return f"Welcome to {BUSINESS['client']}! I’m your assistant from {BUSINESS['brand']}. Ask me about plans, timings, or type ‘trial’ to book a free session."
    return None

@app.route('/')
def index():
    return render_template('index.html', business=BUSINESS, quick_replies=QUICK_REPLIES)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    msg = (data.get('message') or '').strip()
    intent = match_intent(msg)

    # Lead form using free text
    if re.search(r"name\s*:\s*|phone\s*:\s*|time\s*:\s*", msg.lower()):
        captured = {
            'name': re.search(r"name\s*:\s*([^,|\n]+)", msg, re.I),
            'phone': re.search(r"phone\s*:\s*([0-9+\- ]{8,15})", msg, re.I),
            'time': re.search(r"time\s*:\s*([^,|\n]+)", msg, re.I)
        }
        name = captured['name'].group(1).strip() if captured['name'] else ''
        phone = captured['phone'].group(1).strip() if captured['phone'] else ''
        pref_time = captured['time'].group(1).strip() if captured['time'] else ''

        if name and phone:
            save_lead({
                'timestamp': datetime.now().isoformat(),
                'source': 'chat',
                'name': name,
                'phone': phone,
                'preference': pref_time or '—',
                'note': 'Free trial request'
            })
            return jsonify({
                'reply': f"Thanks {name}! We'll contact {phone} to confirm your {pref_time or 'preferred'} slot.",
                'quick': QUICK_REPLIES
            })
        else:
            return jsonify({'reply': 'Please share in format → Name: <name>, Phone: <number>, Time: morning/evening.', 'quick': QUICK_REPLIES})

    if intent:
        ans = kb_answer(intent)
        if intent == 'trial':
            return jsonify({'reply': ans, 'expecting_form': True})
        return jsonify({'reply': ans, 'quick': QUICK_REPLIES})

    # Fallback
    return jsonify({'reply': KB['fallback'], 'quick': QUICK_REPLIES})

@app.route('/lead', methods=['POST'])
def lead():
    payload = request.get_json() or {}
    name = (payload.get('name') or '').strip()
    phone = (payload.get('phone') or '').strip()
    plan = (payload.get('plan') or 'Trial').strip()
    time_pref = (payload.get('time_pref') or '').strip()

    if not name or not re.fullmatch(r"[+\- 0-9]{8,15}", phone):
        return jsonify({'ok': False, 'error': 'Invalid name or phone number.'}), 400

    save_lead({
        'timestamp': datetime.now().isoformat(),
        'source': 'form',
        'name': name,
        'phone': phone,
        'preference': time_pref or '—',
        'note': f'Plan: {plan}'
    })
    return jsonify({'ok': True, 'message': f'Thanks {name}! We will confirm on {phone} soon.'})

def save_lead(row):
    os.makedirs(DATA_DIR, exist_ok=True)
    new = not os.path.exists(LEADS_PATH)
    with open(LEADS_PATH, 'a', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=['timestamp','source','name','phone','preference','note'])
        if new:
            w.writeheader()
        w.writerow(row)

if __name__ == '__main__':
    app.run(debug=True)
