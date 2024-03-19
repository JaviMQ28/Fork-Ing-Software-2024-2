from flask import Blueprint, render_template

menu_blueprint = Blueprint('menu', __name__, url_prefix='/menu')

@menu_blueprint.route("/html")
def html_controller():
    return render_template('menu.html')
