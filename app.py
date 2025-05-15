from flask import Flask, request, render_template, redirect, session, url_for
import requests, json, os
from werkzeug.security import check_password_hash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'CHANGE_THIS_TO_SOMETHING_LONG_AND_RANDOM'

LM_ENDPOINT = 'http://192.168.40.57:1234/v1/chat/completions'
CHAT_LOG_DIR = 'user_chats'
os.makedirs(CHAT_LOG_DIR, exist_ok=True)

with open('users.json') as f:
    USERS = json.load(f)

def get_chat_log_path(username):
    return os.path.join(CHAT_LOG_DIR, f"{username}.json")

def load_chat_history(username):
    path = get_chat_log_path(username)
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return []

def save_chat_history(username, history):
    with open(get_chat_log_path(username), 'w') as f:
        json.dump(history, f, indent=2)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed = USERS.get(username)
        if hashed and check_password_hash(hashed, password):
            session['user'] = username
            return redirect(url_for('chat'))
        error = "Invalid credentials"
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/', methods=['GET', 'POST'])
def chat():
    if 'user' not in session:
        return redirect(url_for('login'))

    user = session['user']
    history = load_chat_history(user)
    response_text = None

    if request.method == 'POST':
        prompt = request.form['prompt']
        payload = {
            "model": "deepseek-r1-distill-qwen-7b:2",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7
        }

        try:
            r = requests.post(LM_ENDPOINT, json=payload)
            response_text = r.json()['choices'][0]['message']['content']
        except Exception as e:
            response_text = f"Error: {e}"

        history.append({
            "timestamp": datetime.now().isoformat(),
            "prompt": prompt,
            "response": response_text
        })
        save_chat_history(user, history)

    return render_template('index.html', response=response_text, history=history, username=user)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
