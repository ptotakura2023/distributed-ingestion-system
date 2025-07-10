from flask import Flask
from flask_cors import CORS
from prometheus_flask_exporter import PrometheusMetrics
from routes import routes
from db import init_db



# Your existing imports and route definitions

app = Flask(__name__)
metrics = PrometheusMetrics(app)
CORS(app)

init_db()
app.register_blueprint(routes)

if __name__ == "__main__":
    app.run(debug=True)
