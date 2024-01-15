from market import app
import os


if __name__ == '__main__':
    app.run(debug=True, port=os.environ.get('APP_PORT'))
