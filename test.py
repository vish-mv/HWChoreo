from flask import Flask

# Create a Flask app
app = Flask(__name__)

# Define a route to handle GET requests
@app.route('/hello')
def hello():
    return 'Hello, world!'

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
