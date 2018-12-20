from appdir import global_string, app, db
from appdir.models import User, Post

# print('Inside microblog loader :)')
# print(global_string)

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
