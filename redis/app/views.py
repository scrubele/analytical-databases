from flask import (
    Flask, request, abort, jsonify, send_from_directory, send_file, redirect, url_for,
    render_template)
import json
import logging
from app import app
from app.data_processors import DataProcessor
import os
from app.loggers import context

@app.before_request
def before_request_func():
    context.do_logging('Request is started')


@app.route('/', methods=['POST'])
def post():
    form_values = request.form.to_dict(flat=True)
    if 'url' in form_values:
        url = form_values['url']
        data_processor = DataProcessor(url, 100)
        get_data = data_processor.loop_data()
        return jsonify(get_data)
    else:
        response = {"error": "No URL specified", 'status_code': 404}
        return response


@app.after_request
def after_request_func(response):
    context.do_logging('Request is finished')
    return response


@app.teardown_request
def after_all_requests(response):
    context.do_logging('Request teardown')
