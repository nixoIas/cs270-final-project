from flask import Flask, render_template, request
from werkzeug.datastructures import ImmutableTypeConversionDict
import os
import kevinpsm

app = Flask(__name__, static_url_path = "/Users/nix/desktop")
 
if __name__ == "__main__":
    app.run()
 
@app.route("/", methods = ["GET", "POST"])
def webapp():
    if request.method == "POST":
        ambiance = request.form.get('Ambiance')
        categories = request.form.get('Type')
        day = request.form.get('Day')
        lat = request.form.get('Lat')
        lon = request.form.get('Lon')
        time = request.form.get('Time')
        minstar = request.form.get('Minstar')
        minreview = request.form.get('MinReview')

        if lat == "None":
            lat = None
        if lon == "None":
            lon = None
        if categories == 'no preference':
            categories = []
        if ambiance == 'no preference':
            ambiance = []

        params = [lat, lon, day, time, categories, ambiance, minstar, minreview]
        return_var = kevinpsm.funky(params)
        split_var = return_var.split('//')
        return return_var
    return render_template("webapp.html")


# lat = None
# lon = None
# day = 'mon'
# time = 11.45
# categories = []
# ambiences = []
# minStars = 2.0
# minReviewCount = 1

