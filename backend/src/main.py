from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.settings import Config
from src.api.auth.auth_routes import auth_bp
from src.api.quizzes.quiz_routes import quiz_bp
app.register_blueprint(quiz_bp, url_prefix='/quizzes')

from src.api.content.content_routes import content_bp
app.register_blueprint(content_bp, url_prefix='/content')

from src.api.ml-models.model_routes import model_bp
app.register_blueprint(model_bp, url_prefix='/ml-models')


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(auth_bp, url_prefix='/auth')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

