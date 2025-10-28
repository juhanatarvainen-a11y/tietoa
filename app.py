from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Tervetuloa Evankeliseen erakkomajaan, jossa voit hengähtää ja hiljentyä Raamatun sanan ja rukouksen äärellä."
