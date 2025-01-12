from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('courses.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

if __name__ == '__main__':
    app.run(debug=True)
