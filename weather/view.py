from weather.app import app


@app.route('/')
def index():
    return 'For weather information follow <a href="/api">link</a>'
