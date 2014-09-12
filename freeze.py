import os
from core import app
from flask_frozen import Freezer


freezer = Freezer(app)


if __name__ == '__main__':
    app.config.update(
        FREEZER_DESTINATION=os.path.join(os.getcwd(), 'build'),
        FREEZER_RELATIVE_URLS=True
    )
    freezer.freeze()
