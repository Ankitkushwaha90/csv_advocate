from flask import Flask, render_template, abort
import os

app = Flask(__name__)

CSV_FOLDER = 'csv_files'

@app.route('/')
def index():
    csv_files = os.listdir(CSV_FOLDER)
    playlist_weight = 1/4
    display_weight = 1.25
    return render_template('index.html', csv_files=csv_files, playlist_weight=playlist_weight, display_weight=display_weight)

@app.route('/csv/<filename>')
def display_csv(filename):
    file_path = os.path.join(CSV_FOLDER, filename)
    if not os.path.isfile(file_path):
        abort(404)
    with open(file_path, 'r') as file:
        csv_data = [line.strip().split(',') for line in file.readlines()]
    return render_template('csv.html', filename=filename, csv_data=csv_data)

if __name__ == '__main__':
    app.run(debug=True)
