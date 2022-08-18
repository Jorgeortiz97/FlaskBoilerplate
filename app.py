from flask import Flask, render_template

#######################
## App configuration ##
#######################

app = Flask(__name__)
app.config.from_object("config")

#######################
## Route controllers ##
#######################

@app.route("/")
def index():
    return render_template("pages/index.html")

@app.errorhandler(404)
def not_found_error(error):
    return render_template("pages/404.html"), 404


################
## App launch ##
################

if __name__ == "__main__":
    app.run() # Port 5000 by default (`host` and `port` can be specified)
