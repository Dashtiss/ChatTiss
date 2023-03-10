from flask import Flask, request, render_template
import gpt, os
app = Flask(__name__)
GPT = gpt.OpenAi()
GPT.answer = ""
GPT.api = os.getenv("api")
@app.route('/')
def index():
    return render_template("home.html", answer="")

@app.route('/', methods=['POST'])
def submit_form():
    question = request.form['name']
    GPT.sendResponse(question)
    return render_template("home.html", answer=GPT.answer)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
