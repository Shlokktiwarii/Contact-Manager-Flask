from flask import Flask
import os



def create_app():
    app = Flask(__name__,instance_relative_config=True,template_folder="../templates",static_folder="../static")