from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():  # 确保函数名称为 home
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run()
