import sys

sys.path.append('.')  # đoạn này để gọi import root folder của project vào module này : để gọi được đến các folder khác
from app.controllers.main import main
from app.controllers.errors import errors
