from datetime import timedelta, datetime
from flask import Flask, jsonify, request, session, escape, make_response, send_file, blueprints
from app.DB.database import db_session
from app.utils.json_encoder import AlchemyEncoder
from app.users import mod as users

app = Flask(__name__)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=60)
app.json_encoder = AlchemyEncoder
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
    if exception and db_session.is_active:
        db_session.rollback()


app.register_blueprint(users, url_prefix='/users')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
