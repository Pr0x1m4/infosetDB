"""infoset-ng configuration ui."""

# Flask imports
from flask import Blueprint
from flask import render_template
import os
# Define the STATUS global variable
CONFIG_PAGE = Blueprint('CONFIG_PAGE', __name__)


@CONFIG_PAGE.route('/config/get')
def getConfig():
    """Function for displaying the current configuration status.

    Args:
        None

    Returns:
        Configuration Page

    """
    # Return
    return render_template('config.html')
