# app/routes/category.py
from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Category

categories_bp = Blueprint('categories', __name__)

@categories_bp.route('/')
def listar_categorias():
    categories = Category.query.all()
    return render_template('categories/listar_categorias.html', categories=categories)

@categories_bp.route('/new', methods=['GET', 'POST'])
def add_category():
    if request.method == 'POST':
        name = request.form['name']
        new_category = Category(name=name)
        db.session.add(new_category)
        db.session.commit()
        return redirect(url_for('categories.listar_categorias'))
    return render_template('categories/create_category.html')
