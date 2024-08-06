from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

main = Blueprint('main', __name__)

@main.route('/')
def welcome():
    try:
        return render_template('welcome.html')
    except TemplateNotFound:
        abort(404)

@main.route('/get_started')
def get_started():
    try:
        return render_template('get_started.html')
    except TemplateNotFound:
        abort(404)

@main.route('/regions')
def regions():
    try:
        return render_template('region_links.html')
    except TemplateNotFound:
        abort(404)

@main.route('/region/<region_name>')
def region(region_name):
    try:
        return render_template(f'regions/{region_name}.html', region_name=region_name)
    except TemplateNotFound:
        abort(404)

@main.route('/region/<region_name>/district/<district_name>')
def district(region_name, district_name):
    try:
        return render_template(f'districts/{region_name}/{district_name}.html', region_name=region_name, district_name=district_name)
    except TemplateNotFound:
        abort(404)
