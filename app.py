import os

from flask import Flask, render_template, request

app = Flask(__name__)

MAX_LENGTH = 500


@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    error = None
    if request.method == 'POST':
        text = (request.form.get('user_text') or '').strip()
        if not text:
            error = 'Vul een bericht in.'
        elif len(text) > MAX_LENGTH:
            error = f'Je bericht mag maximaal {MAX_LENGTH} tekens zijn.'
        else:
            result = text

    return render_template('index.html', result=result, error=error)


if __name__ == '__main__':
    # Debug alleen aan als je dat expliciet wilt: FLASK_DEBUG=1 python app.py
    debug = os.environ.get('FLASK_DEBUG', '0') == '1'
    app.run(debug=debug)
