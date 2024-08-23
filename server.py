from flask import Flask, render_template, request, json
from Maths.mathematics import summation, subtraction, multiplication
from werkzeug.exceptions import HTTPException

app = Flask("Mathematics Problem Solver")


@app.route("/sum")
def sum_route():
    try:
        num1 = float(request.args.get("num1"))
        num2 = float(request.args.get("num2"))
        res = summation(num1, num2)
    except ValueError:
        return ({"message": "Check parameters value for this request"}, 400)
    return str(res)


@app.route("/sub")
def sub_route():
    try:
        num1 = float(request.args.get("num1"))
        num2 = float(request.args.get("num2"))
        res = subtraction(num1, num2)
    except ValueError:
        return ({"message": "Check parameters value for this request"}, 400)
    return str(res)


@app.route("/mul")
def mul_route():
    try:
        num1 = float(request.args.get("num1"))
        num2 = float(request.args.get("num2"))
        res = multiplication(num1, num2)
    except ValueError:
        return ({"message": "Check parameters value for this request"}, 400)
    return str(res)


@app.route("/")
def render_index_page():
    return render_template("index.html")


@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps(
        {
            "code": e.code,
            "name": e.name,
            "description": e.description,
        }
    )
    response.content_type = "application/json"
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
