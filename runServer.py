#!/usr/bin/python

from app import create_app

create_app().run(debug=True, port=8000)
