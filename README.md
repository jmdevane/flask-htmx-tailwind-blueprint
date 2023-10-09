# Flask Blueprint Boilerplate App
### A template for Flask apps utilizing the Blueprint architecture.

The internet is littered with Flask tutorials and templates. Here is another one.

**THIS BRANCH INCLUDES TAILWIND+HTMX**
`git clone --single-branch --branch feature/tailwind-htmx git@github.com:jmdevane/flask-blueprint-boilerplate.git`
[reference tutorial](https://testdriven.io/blog/flask-htmx-tailwind/)

1. Clone the repository.

    `git clone https://github.com/jmdevane/flask-blueprint-boilerplate.git`

2. Setup virtual environment.

    [virtual envrionment basics](https://realpython.com/python-virtual-environments-a-primer/#create-it)

3. Install dependencies (with virtual environment active)

    `(venv)$ pip install -r requirements.txt`

4. Set Flask app secret key (for securing client-side sessions).

    ```
        >>> import secrets
        >>> secrets.token_hex(16)
        'da08208f2fd9b29c21e6655757ce4f9a'
    ```

    Either set key as an environment variable `FLASK_SECRET_KEY` (current state) or edit `config.py` directly:

    `   SECRET_KEY = 'da08208f2fd9b29c21e6655757ce4f9a'`

5. Configure Tailwind CSS.

    `(venv)$ tailwindcss`

6. Scan the templates and generate CSS file.

    `(venv)$ tailwindcss -i ./flask_app/static/src/main.css -o ./flask_app/static/dist/main.css --minify`

7. Launch development app server.

    `python run.py`

8. Navigate to `http://localhost:5000/` (or ip listed in console if running remotely) to view.

Steps 7-8 can also be excuted via `run.sh`.

---

Production deployment via docker:
1. Create an `env.list` file in the root directory:
```
FLASK_SECRET_KEY
DEPLOYMENT_MODE=prod
```
2. Build Docker image
    
    `docker image build -t rblncd .`
    
3. Run container
    
    `docker run --env-file env.list --name="rblncd" -p 8000:8000 rblncd`