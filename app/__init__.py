from flask import Flask
import os
from .config import Config
from .extensions import db

def create_app(config_class: type = Config):
    app = Flask(__name__,instance_relative_config=True,template_folder="../templates",static_folder="../static")
    
    app.config.from_object(config_class)
    
    os.makedirs(app.instance_path, exist_ok =  True)
    
    db.init_app(app)
    @app.get("/health")
    def health():
        return "OK",200
    
    @app.route("/test")
    def home():
        return "It works",200
    
    from .route import bp
    app.register_blueprint(bp)
    
    return app 