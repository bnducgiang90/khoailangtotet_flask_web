from flask import Blueprint, request, render_template, abort

bp_user = Blueprint('bp_user', __name__, template_folder='views')


@bp_user.route('/user/index', methods=['GET'])
@bp_user.route('/user/index.html', methods=['GET'])
@bp_user.route('/user', methods=['GET'])
def index():
    return render_template("/users/index.html")


@bp_user.route('/user/create', methods=['GET', 'POST'])
@bp_user.route('/user/create.html', methods=['GET', 'POST'])
@bp_user.route('/user/create', methods=['GET', 'POST'])
def create():
    return render_template("/users/create.html")


@bp_user.route('/user/edit', methods=['GET', 'POST'])
@bp_user.route('/user/edit.html', methods=['GET', 'POST'])
@bp_user.route('/user/edit', methods=['GET', 'POST'])
def edit():
    return render_template("/users/edit.html")
