import sys

sys.path.append('.')  # đoạn này để gọi import root folder của project vào module này : để gọi được đến các folder khác

from flask import Blueprint, request, render_template, abort

main = Blueprint('main', __name__, template_folder='views')


@main.route('/index', methods=['GET'])
@main.route('/index.html', methods=['GET'])
@main.route('/', methods=['GET'])
def index():
    return render_template("index.html")
