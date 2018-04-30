from Application.settings import Settings
from Application.flaskWrapper import FlaskWrapper
from DataBase.dbController import DbController


# Class to instantiate the application
class App:

    # Initialize the instance of App
    def __init__(self):
        # Create a Flask instance with app and API
        self.flask = FlaskWrapper(Settings.instance().FlaskBaseConfig())

    def run(self, flaskHost, flaskPort):
        if not Settings.instance().FLASK_DEBUG:
            url = "http://{0}:{1}".format(flaskHost, flaskPort)
            print("The Flask application is running on {0} (Press CTRL+C to quit)".format(url))

        # DataBase
        DbController.instance().initApp(self.flask.App)  # Initialize DB on the application

        if Settings.instance().DATABASE_REBUILT:
            DbController.instance().createTables(self.flask.App)
        if Settings.instance().DATABASE_TEST_DATA:
            DbController.instance().createTestData(self.flask.App)  # Add test data into de DataBase

        # Flask
        self.flask.App.run(flaskHost, port=flaskPort, threaded=True)
