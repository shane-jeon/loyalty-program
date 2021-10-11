"""HausStar Server"""

# from the flask library, import ...
from flask import Flask

# set up flask application
# app in an instance/object of flask
# "__name__" name of the module, lets Flask know where to look for application part
app = Flask(__name__)

#routes and view functions
# in order for "view function" to work, there needs to be a route telling it where to go (thus the /____). flask ROUTES
# to the /___

# python decorator
@app.route('/')
# view function: function that returns web response (response is string, usually HTML)
def homepage():
    """Shows example homepage."""
    # example html until I can get to jinja
    return """
    <!doctype html>
    <html>
    <head>
      <title>temp HTML in server.py</title>
    </head>
    <body>
      <h1>'Sup<h2>
      <form action="/">
        Just put anything here!
        <input type="text" name="anything, really. anything!">
        <input type="submit">
      </form>
    </body>
    </html>
    """
# if this script is being called directly, than run(method) app(instance) 
# need to let module to scan for routes when creating a Flask application
if __name__ == "__main__":
    #DebugToolbarExtension(app)

    app.run(host="0.0.0.0", debug=True)