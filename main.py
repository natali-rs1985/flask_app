from flask_app import app
import os


app.run(debug=False, port=os.environ['PORT'])
