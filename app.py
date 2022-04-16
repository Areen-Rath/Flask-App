from flask import Flask, request, jsonify

app = Flask(__name__)

contacts = [
    {
        "id": 1,
        "name": "Akshat",
        "contact": "7981072926",
        "done": False
    },
    {
        "id": 2,
        "name": "Akshay",
        "contact": "9246555950",
        "done": False,
    },
    {
        "id": 3,
        "name": "Prakeerthi",
        "contact": "9000481605",
        "done": False,
    }
]

@app.route("/add-data", methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "Error",
            "msg": "Please provide the data"
        }, 400)

    contact = {
        "id": contacts[-1]["id"] + 1,
        "name": request.json["name"],
        "contact": request.json["contact"],
        "done": False
    }
    contacts.append(contact)

    return jsonify({
        "status": "Success",
        "msg": "Contact added successfully"
    })

@app.route("/contacts")
def get_contacts():
    return jsonify({
        "data": contacts
    })

if __name__ == "__main__":
    app.run()