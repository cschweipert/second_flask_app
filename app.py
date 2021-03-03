from flask import Flask, request
import operations as op

app = Flask(__name__)


@app.route('/add')
def sum_query_string_options():
    """Handle GET: Add a and b and return result in body."""


    a = int(request.args["a"])
    b = int(request.args["b"])

    result = op.add(a, b)

    return f"<h1>The sum of a and b is {result}!</h1>"


@app.route('/sub')
def sub_query_string_options():
    """Handle GET: Subtract a and b and return result in body."""


    a = int(request.args["a"])
    b = int(request.args["b"])

    result = op.sub(a, b)

    return f"<h1>The subtraction of a and b is {result}!</h1>"


@app.route('/mult')
def mult_query_string_options():
    """Handle GET: Multiply a and b and return result in body."""


    a = int(request.args["a"])
    b = int(request.args["b"])

    result = op.mult(a, b)

    return f"<h1>The multiplication of a and b is {result}!</h1>"


@app.route('/div')
def div_query_string_options():
    """Handle GET: Divide a and b and return result in body."""


    a = int(request.args["a"])
    b = int(request.args["b"])

    result = op.div(a, b)

    return f"<h1>The division of a and b is {result}!</h1>"
    


