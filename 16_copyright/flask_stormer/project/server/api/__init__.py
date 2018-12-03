from flask import Blueprint
from .views import add_urls


api = Blueprint('api', __name__)


@api.record
def mount_controllers(setup_state):
    """
    Is called whenever the `api` blueprint is registered on the application.
    """

    # Mount all controllers to blueprint
    add_urls(api)

    # Copy config and logger from app object into blueprint object
    # this way we can use config directly from blueprint object in all
    # controller classes
    api.config = setup_state.app.config
    api.logger = setup_state.app.logger


__all__ = [
    'api'
]
