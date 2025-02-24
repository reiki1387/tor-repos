from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/page_2/<name>/<int:number>')
def second_page(name, number):
    return render_template('index_page_2.html', name=name, number=number)
    # return f"{name} is learning flask at {number} am"


if __name__ == '__main__':
    app.run(debug=True)
