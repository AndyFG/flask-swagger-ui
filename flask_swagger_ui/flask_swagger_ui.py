import os
import json
from flask import Blueprint, send_from_directory, render_template, request


def get_swaggerui_blueprint(base_url, api_url, oauth_config=None, blueprint_name='swagger_ui'):
    swagger_ui = Blueprint(blueprint_name, __name__, static_folder='dist', template_folder='templates')
    default_config = dict(url=api_url)

    if oauth_config:
        default_config.update({'oauth_config_json': json.dumps(oauth_config)})

    @swagger_ui.route('/')
    @swagger_ui.route('/<path:path>')
    def show(path=None):
        if not path or path == 'index.html':
            fields = dict(base_url=base_url, config=json.dumps(default_config))
            return render_template('index.template.html', **fields)
        else:
            return send_from_directory(os.path.join(swagger_ui.root_path, swagger_ui._static_folder), path)

    return swagger_ui
