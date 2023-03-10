# Import necessary libraries and modules
from flask import Flask, request, render_template
import gpt, os

# Set a title for the app
Title = "ChaTiss"

# Initialize Flask app
app = Flask(__name__)

# Create an instance of the GPT class
GPT = gpt.OpenAi()

# Set initial values for GPT class attributes
GPT.answer = ""
GPT.api = os.getenv("api")

# Define the home route for the app
@app.route('/')
def index():
    return render_template("home.html", answer="", Title=Title)

# Define the behavior when the form is submitted
@app.route('/', methods=['POST'])
def submit_form():
    # Retrieve the user's question from the form
    question = request.form['name']
    # Send the user's question to the GPT API
    GPT.sendResponse(question)
    # Render the template with the response from GPT
    return render_template("home.html", answer=GPT.answer, Title=Title)

# Run the app
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
