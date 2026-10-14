from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        result = request.form.get('user_text')
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
