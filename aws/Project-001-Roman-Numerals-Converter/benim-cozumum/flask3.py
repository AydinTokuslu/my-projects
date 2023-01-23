# Import Flask modules
from flask import Flask, render_template, request, redirect, url_for
# Create an object named app
app = Flask(__name__)


def roman_conv(num):
    roman_map = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII",
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

# @app.route("/")
# def index():
#     if request.method == "GET":
#         return render_template("index.html", methods=["GET"], developer_name='AYDIN TOKUSLU')
#     else:
#         return '<h1>Not Valid! Please enter a number between 1 and 3999, inclusively.</h1>'


# @app.route('/warning')
# def error():
#     return '<h1>Not Valid! Please enter a number between 1 and 3999, inclusively.</h1>'


# @app.route("/")
# def index():
#     num = request.form.get("number")
#     if str(num).isdigit():
#         if num > 1 and num < 3999:
#             return render_template("index.html", number=num, methods=["GET"])
#         else:
#             return redirect(url_for('error'))
#     else:
#         return redirect(url_for('error'))


# @app.route("/conv", methods=["GET", "POST"])
# def convert():
#     if request.method == "POST":
#         num = request.form.get("number")
#         return render_template("result.html", number_decimal=num, number_roman=roman_conv(num), developer_name='AYDIN TOKUSLU')


@app.route("/conv", methods=["GET", "POST"])
def convert():
    if request.method == "POST":
        num = request.form.get("number")
        if int(num) > 1 and int(num) < 3999:
            return render_template("result.html", number_decimal=num, number_roman=roman_conv(num), developer_name='AYDIN TOKUSLU')
        else:
            return '<h1>Not Valid! Please enter a number between 1 and 3999, inclusively.</h1>'


if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=80)
