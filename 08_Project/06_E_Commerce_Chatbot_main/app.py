# This is final application build script, here we combine all moduler code written for RAG in sequesce and create simple frontend

from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
import os
from ecommbot.retrieval_generation import generation
from ecommbot.ingest import ingestdata

app = Flask(__name__)

load_dotenv()

# Call moduler code wriiten 1st
vstore = ingestdata("done")
chain = generation(vstore)


# Home route
@app.route("/")
def index():
    # This gives home page in UI which mentioned inchat.html
    return render_template("chat.html")


# This route to get User Q from UI and POST Response to UI. So GET and POST method used
@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]  # THis bomes GET -request.form
    input = msg
    result = chain.invoke(input)
    print("Response : ", result)
    return str(result)  # THis becomes POST


if __name__ == "__main__":
    app.run(debug=True)
