from app import app, db
from app.models import User, Post

# Create a flask shell context within the app for the db
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post':Post}