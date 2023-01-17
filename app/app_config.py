from flask import Flask
from app.v1.urls import v1


app = Flask(__name__)


VERSION_OBJECT_MAPPING = {
    '1': v1,
}


def get_url_prefix(version):
    return '/api/v{version_number}'.format(version_number=str(version))


def register_versions(allowed_versions):
    for version in allowed_versions:
        app.register_blueprint(
            VERSION_OBJECT_MAPPING[version], url_prefix=get_url_prefix(version))
