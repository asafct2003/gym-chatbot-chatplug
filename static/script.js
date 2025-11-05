const messages = document.getElementById('messages');
const input = document.getElementById('input');
const composer = document.getElementById('composer');
const quick = document.getElementById('quick');

document.getElementById('year').textContent = new Date().getFullYear();

function addMsg(text, who='bot') {
  const div = document.createElement('div');
  div.className = `msg ${who}`;
  div.innerHTML = text;
  messages.appendChild(div);
  messages.scrollTop = messages.scrollHeight;
}

function setQuick(items) {
  quick.innerHTML = '';
  (items || []).forEach(btnData => {
    const btn = document.createElement('button');
    btn.textContent = btnData.text;
    btn.onclick = ()=> send(btnData.payload);
    quick.appendChild(btn);
  });
}

function welcome() {
  addMsg("👋 Welcome! I'm the FitPulse Gym assistant powered by <b>Chatplug.ai</b>. Ask about <i>plans</i>, <i>timings</i>, or type <b>trial</b> to book a session.");
  setQuick(window.QUICK);
}

async function send(text) {
  addMsg(text, 'user');
  input.value = '';

  const res = await fetch('/chat', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({message: text})
  });

  const data = await res.json();
  addMsg(data.reply, 'bot');
  setQuick(data.quick);

  if(data.expecting_form) renderTrialForm();
}

function renderTrialForm() {
  const div = document.createElement('div');
  div.className = 'msg bot';
  div.innerHTML = `
    <div class="form">
      <input id="f_name" placeholder="Your name" />
      <input id="f_phone" placeholder="Phone (10 digits)" />
      <select id="f_plan">
        <option>Trial</option>
        <option>Monthly</option>
        <option>Quarterly</option>
        <option>Yearly</option>
      </select>
      <select id="f_time">
        <option value="morning">Morning</option>
        <option value="evening">Evening</option>
      </select>
      <button id="f_submit">Submit</button>
    </div>`;
  messages.appendChild(div);
  messages.scrollTop = messages.scrollHeight;

  div.querySelector('#f_submit').onclick = async () => {
    const name = div.querySelector('#f_name').value.trim();
    const phone = div.querySelector('#f_phone').value.trim();
    const plan = div.querySelector('#f_plan').value;
    const time_pref = div.querySelector('#f_time').value;

    const res = await fetch('/lead', {
      method:'POST',
      headers:{'Content-Type':'application/json'},
      body: JSON.stringify({name, phone, plan, time_pref})
    });

    const data = await res.json();
    if(data.ok) addMsg(data.message, 'bot');
    else addMsg('Please check your details and try again.', 'bot');
  };
}

composer.addEventListener('submit', e => {
  e.preventDefault();
  const text = input.value.trim();
  if(text) send(text);
});

welcome();
