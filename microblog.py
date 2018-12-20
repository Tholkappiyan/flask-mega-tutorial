from appdir import global_counter, app, db
from appdir.models import User, Post

# print('Inside microblog loader :)')
# print(global_counter)

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
