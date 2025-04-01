import os
from flask import Flask, render_template_string, request

app = Flask(__name__)
app.template_folder = '.'  # Look for HTML files in current directory

reports = []

@app.route('/')
def home():
    with open('index.html') as f:
        return render_template_string(f.read())

@app.route('/check', methods=['POST'])
def check():
    toxic_words = ["stupid", "idiot", "hate", "kill", "ugly", "fat"]
    comment = request.form['comment']

    if any(word in comment.lower() for word in toxic_words):
        reports.append(comment)
        result = ("TOXIC! 🚨", "red")
    else:
        result = ("CLEAN! ✅", "green")

    with open('index.html') as f:
        return render_template_string(
            f.read(),
            result=result[0],
            color=result[1],
            comment=comment
        )

@app.route('/moderator')
def moderator():
    with open('moderator.html') as f:
        return render_template_string(
            f.read(),
            reports=reports
        )

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use Render-assigned port
    app.run(host='0.0.0.0', port=port)
