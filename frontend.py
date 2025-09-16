from flask import Flask, render_template_string, request
import requests
import os

app = Flask(__name__)

BACKEND_URL = os.environ.get("BACKEND_URL", "http://127.0.0.1:8000")

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Counter App</title>
</head>
<body>
    <h2>Counter App</h2>
    <p>Current Value: <strong>{{ counter }}</strong></p>
    <form method="get" action="/increment">
        <button type="submit">Increment</button>
    </form>
    <form method="get" action="/decrement">
        <button type="submit">Decrement</button>
    </form>
</body>
</html>
"""

def get_counter_value():
    try:
        response = requests.get(f"{BACKEND_URL}/value")
        return response.json().get("counter", 0)
    except:
        return 0

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE, counter=get_counter_value())

@app.route("/increment")
def increment():
    try:
        requests.get(f"{BACKEND_URL}/increment")
    except:
        pass
    return render_template_string(HTML_TEMPLATE, counter=get_counter_value())

@app.route("/decrement")
def decrement():
    try:
        requests.get(f"{BACKEND_URL}/decrement")
    except:
        pass
    return render_template_string(HTML_TEMPLATE, counter=get_counter_value())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
