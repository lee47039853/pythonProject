from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/sample')
def hello_sample():
    html = """
        <html>
            <h1>Welcome to our Flask!</h1>
            <ul>
                <li>Host</li>
                <li>Port</li>
                <li>Debug</li>
            </ul>
        </html>
    """
    return html


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7070, debug=True)
