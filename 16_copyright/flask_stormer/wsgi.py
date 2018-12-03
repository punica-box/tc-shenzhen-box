"""
Module to be used with WSGI containers.

Example:

using Gunicorn you can run the application indside of Gunicorn WSGI
container by issuing command:

gunicorn --bind my.foo.hostname:12345 bidding_agent.wsgi:app
"""

from project.server import app
