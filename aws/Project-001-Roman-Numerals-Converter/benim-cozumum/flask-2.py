# Import Flask modules
from flask import Flask, render_template, request, redirect, url_for
# Create an object named app
app = Flask(__name__)


def roman_conv(num):
    roman_letters = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII",
                     8: "VIII", 9: "IX", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}

    result = ""
    remainder = int(num)

    for i in sorted(roman_letters.keys(), reverse=True):
        if remainder > 0:
            multiplier = i
            roman_digit = roman_letters[i]

            times = remainder // multiplier
            remainder = remainder % multiplier
            result += roman_digit * times

    return result


@app.route("/")
def index():
    return render_template("index.html", methods=["GET"], developer_name='AYDIN TOKUSLU')


@app.route("/conv", methods=["GET", "POST"])
def convert():
    if request.method == "POST":
        num = request.form.get("number")
        return render_template("result.html", number_decimal=num, number_roman=roman_conv(num), developer_name='AYDIN TOKUSLU')


if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=80)
