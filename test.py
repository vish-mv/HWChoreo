from flask import Flask
import yaml

# Create a Flask app
app = Flask(__name__)

# Load endpoints from endpoints.yaml
def load_endpoints():
    with open('.choreo/endpoints.yaml', 'r') as file:
        endpoints = yaml.safe_load(file)
    return endpoints.get('endpoints', [])

# Register endpoints dynamically
def register_endpoints():
    endpoints = load_endpoints()
    for endpoint in endpoints:
        url = endpoint['url']
        methods = endpoint['methods']
        handler_path = endpoint['handler']
        module_name, func_name = handler_path.rsplit('.', 1)
        handler = getattr(__import__(module_name, fromlist=[func_name]), func_name)
        app.add_url_rule(url, view_func=handler, methods=methods)

# Run this function to register endpoints
register_endpoints()

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
