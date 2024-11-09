from flask import Flask, render_template, request
from kbbi import KBBI, TidakDitemukan

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        word = request.form['word']
        try:
            # Mencari kata di KBBI
            result = KBBI(word)
        except TidakDitemukan:
            result = None  # Jika kata tidak ditemukan

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)