from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Smart Knowledge Base for AI (Raheem)
RESPONSES = {
    "projects": (
        "Here are my key projects:\n"
        "1. Cloud Web App Deployment: Automated Flask & Gunicorn on AWS EC2.\n"
        "2. AI/ML for Electric Vehicles: Machine learning algorithms for battery & telemetry optimization.\n"
        "3. Smart Home Embedded Systems: IoT integration for home automation and sensors."
    ),
    "skills": (
        "My technical toolkit includes:\n"
        "• Cloud: AWS (EC2, Linux server configuration, systemd)\n"
        "• Programming: Python, Flask, Shell scripting\n"
        "• Development: Git, GitHub version control, Linux OS administration"
    ),
    "aws": (
        "This project runs on an Ubuntu 24.04 LTS instance (AWS EC2 Mumbai region). "
        "It uses Gunicorn WSGI, managed as a background daemon by Linux systemd, "
        "serving requests reliably on port 80."
    ),
    "contact": (
        "You can connect with me directly through GitHub at: github.com/raheem-cloud"
    )
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}
    message = data.get("message", "").lower().strip()
    
    if any(k in message for k in ["project", "work", "portfolio", "built"]):
        reply = RESPONSES["projects"]
    elif any(k in message for k in ["skill", "tech", "stack", "language", "python", "linux"]):
        reply = RESPONSES["skills"]
    elif any(k in message for k in ["aws", "cloud", "ec2", "server", "deploy", "architecture"]):
        reply = RESPONSES["aws"]
    elif any(k in message for k in ["contact", "email", "reach", "github"]):
        reply = RESPONSES["contact"]
    elif any(k in message for k in ["hi", "hello", "hey", "who are you"]):
        reply = "Hello! I am Raheem's AI assistant. Ask me about his projects, technical skills, or this AWS cloud architecture!"
    else:
        reply = (
            "I can tell you all about Raheem's background. Try asking about:\n"
            "• 'What projects have you worked on?'\n"
            "• 'What are your core technical skills?'\n"
            "• 'How is this AWS deployment built?'"
        )
    
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)