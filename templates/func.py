
from flask import Flask, render_template, request
import math

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        shape = request.form['shape']
        precision = int(request.form['precision'])
        volume = 0

        if shape == 'sphere':
            radius = float(request.form['radius'])
            volume = round((4 / 3) * math.pi * radius ** 3, precision)
        elif shape == 'cone':
            radius = float(request.form['radius'])
            height = float(request.form['height'])
            volume = round((1 / 3) * math.pi * radius ** 2 * height, precision)
        elif shape == 'cylinder':
            radius = float(request.form['radius'])
            height = float(request.form['height'])
            volume = round(math.pi * radius ** 2 * height, precision)
        return render_template('result.html', shape=shape, volume=volume)
    return render_template('index.html')
