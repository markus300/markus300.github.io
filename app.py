from flask import Flask, jsonify, request
import subprocess

app = Flask(__name__)

@app.route('/run-tkinter', methods=['GET'])
def run_tkinter():
    # Ejecuta el script de Tkinter
    subprocess.Popen(['python', 'tkinter_app.py'])
    return jsonify({'message': 'Tkinter app running'})

if __name__ == '__main__':
    app.run(debug=True)
