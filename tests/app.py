from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

messages = []


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/hello")
def api_hello():
    return jsonify({"message": "Hello from Flask!", "timestamp": datetime.now().isoformat()})


@app.route("/api/messages", methods=["GET", "POST"])
def api_messages():
    if request.method == "POST":
        data = request.get_json()
        if data and "text" in data:
            messages.append({"text": data["text"], "timestamp": datetime.now().isoformat()})
            return jsonify({"status": "ok"}), 201
        return jsonify({"error": "text field required"}), 400
    return jsonify(messages)


if __name__ == "__main__":
    app.run(debug=True)
