from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/calendario')
def calendario():
    return render_template('calendario.html')

@app.route('/planejamento')
def planejamento():
    return render_template('planejamento.html')

if __name__ == '__main__':
    app.run(debug=True)
