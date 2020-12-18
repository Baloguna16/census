from flask import Flask, jsonify, Blueprint, request, render_template, redirect, session, make_response

bp = Blueprint('/routes', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/state/<code>')
def state(code):
    state = code.upper()
    return render_template('state.html', state=state)
