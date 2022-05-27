from logging import root
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def home():
	return render_template('index.html')

@app.route('/documentos')
def documentitos():
	return render_template('documentos.html')

@app.route('/lenguajes')
def lenguajes():
	return render_template('lenguaje.html')

if __name__ == '__main__':
	app.run(debug=True, port=5612)
 
''' 
http://127.0.0.1:5612/documentos
'''