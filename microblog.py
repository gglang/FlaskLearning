from app import create_app, db, cli
from app.models import User, Post

app = create_app()
cli.register(app)


# Use command "flask shell" to run a python shell with
# the below listed symbols pre-imported for easy devving
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
