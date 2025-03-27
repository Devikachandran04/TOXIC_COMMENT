from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simple database
reports = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    toxic_words = ["stupid", "idiot", "hate","shit","worthless","shiity", "kill", "ugly", "fat"]
    comment = request.form['comment']
    
    if any(word in comment.lower() for word in toxic_words):
        reports.append(comment)
        return render_template('index.html', 
                            result="TOXIC! 🚨", 
                            color="red",
                            comment=comment)
    else:
        return render_template('index.html', 
                            result="CLEAN! ✅", 
                            color="green",
                            comment=comment)

@app.route('/moderator')
def moderator():
    return render_template('moderator.html', reports=reports)

if __name__ == '__main__':
    app.run(debug=True)