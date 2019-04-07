from app import app, db
from app.models import User, Post


@app.shell_context_processor
def make_shell_context():
    # this adds these classes to the shell so you don't have to keep importing them
    return {'db': db, 'User': User, 'Post': Post}