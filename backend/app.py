from flask import Flask, request, jsonify
import sys
from io import StringIO

app = Flask(__name__)

@app.route('/run', methods=['POST'])
def run_code():
    data = request.get_json()
    code = data.get('code', '')

    # Redirect stdout to capture print statements
    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout

    try:
        exec(code)
        output = new_stdout.getvalue()
        return jsonify({'output': output}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    finally:
        sys.stdout = old_stdout

if __name__ == '__main__':
    app.run(debug=True)
  
