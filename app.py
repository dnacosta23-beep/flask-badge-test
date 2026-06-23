from flask import Flask, request
import json 

app = Flask(__name__)

@app.route('/')
def hello_world():
    return {
        "name": "Nikki",
    }


@app.route("/notes", methods=["POST"])
def add_note():
    notes = request.get_json()

    

    with open("notes.json", "w") as file:
        json.dump(notes, file, indent=2)

    return notes, 201