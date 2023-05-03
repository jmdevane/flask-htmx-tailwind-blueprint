from flask_app import create_app #app variable has to exist in init.py

app = create_app()

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000, debug=True)