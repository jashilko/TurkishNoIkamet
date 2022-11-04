from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/')
def index():

    with open('polygons.json', 'r') as file:
        polygons = json.load(file)
    with open('points.json', 'r') as file:
        points = json.load(file)
    return render_template('index.html', polygons=polygons, points=points)

if __name__ == '__main__':
    app.run(debug=True)