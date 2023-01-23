# Import Flask modules
from flask import Flask, render_template, request
# Create an object named app
app = Flask(__name__)


# create a function named "lcm" which calculates a least common multiple values of two numbers.

# @app.route("/")
def roman_conv(num):

    roman_map = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII",
                 8: "VIII", 9: "IX", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}

    result = ""
    remainder = num

    for i in sorted(roman_map.keys(), reverse=True):
        if remainder > 0:
            multiplier = i
            roman_digit = roman_map[i]

            times = remainder // multiplier
            remainder = remainder % multiplier
            result += roman_digit * times

    return result


@app.route("/")
def index():
    return render_template("index.html", methods=["GET"])


@app.route("/conv", methods=["GET", "POST"])
def convert():
    if request.method == "POST":
        num = request.form.get("number")
        #result = roman_conv(num)
        return render_template("result.html", number_decimal=num, number_roman=roman_conv(num), roman=roman_conv)
        # return render_template("result.html", number_decimal=num, number_roman=num2, roman=lcm(int(num1), int(num2)), developer_name='AYDINT')
    else:
        return render_template("result.html")


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         user_name = request.form['username']
#         password = request.form['password']
#         if password == 'clarusway':
#             return render_template('secure.html', user=user_name.title())
#         else:
#             return render_template('login.html', user=user_name.title(), control=True)
#     else:
#         return render_template('login.html', control=False)

# @app.route('/sum')
# def number():
#     var1, var2 = 15210, 38960
#     return render_template('body.html', value1=var1, value2=var2, sum=var1+var2)
# @app.route('/')
# def head():
#     return render_template('index.html', number1=117000, number2=229000)
# @app.route('/forth/<string:id>')
# def forth(id):
#     return f'Id number of this page is {id}'
# @app.route("/")
# def head():
#     first = "This is my first conditions experience"
#     return render_template("index.html", message=first)
# @app.route('/<name>')
# def greet(name):
#     return render_template('greet.html', name=name)
# @app.route('/')
# def home():
#     return render_template('main.html', name='Vincenzo')

# # Create a function named `index` which uses template file named `index.html`
# # send two numbers as template variable to the app.py and assign route of no path ('/')
# @app.route("/")
# def index():
#     return render_template("index.html", methods=["GET"])
# @app.route('/greet', methods=['GET'])
# def greet():
#     if 'user' in request.args:
#         usr = request.args['user']
#         return render_template('greet.html', user=usr)
#     else:
#         return render_template('greet.html', user='Send your user name with "user" param in query string')
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         user_name = request.form['username']
#         password = request.form['password']
#         if password == 'clarusway':
#             return render_template('secure.html', user=user_name.title())
#         else:
#             return render_template('login.html', user=user_name.title(), control=True)
#     else:
#         return render_template('login.html', control=False)


# calculate sum of them using "lcm" function, then sent the result to the
# "result.hmtl" file and assign route of path ('/calc').
# When the user comes directly "/calc" path, "Since this is a GET request, LCM has not been calculated" string returns to them with "result.html" file
# Add a statement to run the Flask application which can be debugged.
if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=80)
