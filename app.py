#!/bin/env/python3
# coding: utf-8

import os
import StrintIO


from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

@app.route('/')

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(port=port)
