from flask import Flask, jsonify
from circle import Circle

app = Flask(__name__)


@app.route('/circle/<radius>')
def circle_route(radius):
    circle = Circle(radius=radius)
    return jsonify({"area": circle.area(), "perimeter": circle.perimeter()}), 200


if __name__ == '__main__':
    app.run()
