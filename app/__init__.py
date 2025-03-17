import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from dotenv import load_dotenv 

# Cargar las variables de entorno
load_dotenv()

# Crear la instancia de la aplicación Flask
app = Flask(__name__)

# Configuración de la base de datos PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos
db = SQLAlchemy(app)

# Importar modelos para SQLAlchemy los reconozca
from app.models import Post, Category

# Importar y registrar blueprints
from app.routes.post import posts_bp
from app.routes.category import categories_bp

# Registrar blueprints
app.register_blueprint(posts_bp, url_prefix='/posts')
app.register_blueprint(categories_bp, url_prefix='/categories')

# Ruta principal
@app.route('/')
def index():
    return render_template('home.html')