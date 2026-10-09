from flask import Flask, jsonify

app = Flask(__name__)

professionals = [
    {
        "id": 1,
        "name": "John",
        "service": "Graphic Design",
        "price": 50000
    },
    {
        "id": 2,
        "name": "Mary",
        "service": "Photography",
        "price": 75000
    },
    {
        "id": 3,
        "name": "David",
        "service": "Web Development",
        "price": 40000
    }
]


@app.route("/")
def home():
    return jsonify({"message": "JUT Marketplace API is running"})


@app.route("/professionals")
def get_professionals():
    return jsonify(professionals)

@app.route("/professionals/<int:professional_id>")
def get_professional(professional_id):
    for person in professionals:
        if person["id"] == professional_id:
            return jsonify(person)

    return jsonify({"error": "Professional not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
