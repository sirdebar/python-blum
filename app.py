from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/auth', methods=['POST'])
def auth():
    user = request.json
    return jsonify(user)

if __name__ == '__main__':
    app.run(debug=True)
