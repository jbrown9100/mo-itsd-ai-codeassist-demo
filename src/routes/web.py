from flask import Blueprint, render_template, request
from ..services.search import search_people

web = Blueprint('web', __name__)


@web.get('/')
def index():
    return render_template('index.html')


@web.get('/search')
def search():
    q = request.args.get('q', '')
    results = search_people(q)
    return render_template('search.html', q=q, results=results)
