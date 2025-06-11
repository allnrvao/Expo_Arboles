from flask import Flask, render_template, jsonify
from models.heapsort import heap_sort

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sort/<numbers>')
def sort(numbers):
    try:
        # Convert input string to list of integers
        arr = [int(x) for x in numbers.split(',')]
        # Get sorting steps
        steps = heap_sort(arr)
        return jsonify({'steps': steps})
    except:
        return jsonify({'error': 'Invalid input'}), 400

if __name__ == '__main__':
    app.run(debug=True)