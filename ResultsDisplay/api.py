from flask import Flask, jsonify, request
from build import marks

app = Flask(__name__)

build_class = marks("default_value1", "default_value2")

@app.route("/marks",mehtods=["GET"])
def store():
    result= build_class.store()
    return jsonify(result=result)

# Register the class-based vie

if __name__ == '__main__':
    app.run(debug=True)


## how to create webframe page in python  using flask for a module of a class with constructor variables