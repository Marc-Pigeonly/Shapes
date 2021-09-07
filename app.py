from flask import Flask, jsonify
from circle import Circle

app = Flask(__name__)


def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


@app.route('/circle/<radius>')
def circle_route(radius):
    if not is_number(radius):
        return jsonify({"msg": "radius must be a numeric value"}), 401
    circle = Circle(radius=radius)
    return jsonify({"area": circle.area(), "perimeter": circle.perimeter()}), 200


if __name__ == '__main__':
    app.run()
