from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)


@app.route("/")
def home():
    active = [
        '"nav-link active"',
        '"nav-link"',
        '"nav-link"',
        '"nav-link"'
    ]
    return render_template("all.jinja2", active=active)


@app.route("/wild")
def wild():
    active = [
        '"nav-link"',
        '"nav-link active"',
        '"nav-link"',
        '"nav-link"'
    ]
    return render_template("wild.jinja2", active=active)


@app.route("/portrait")
def portrait():
    active = [
        '"nav-link active"',
        '"nav-link"',
        '"nav-link"',
        '"nav-link"'
    ]
    return render_template("portrait.jinja2", active=active)


@app.route("/art")
def art():
    active = [
        '"nav-link"',
        '"nav-link"',
        '"nav-link active"',
        '"nav-link"'
    ]
    return render_template("art.jinja2", active=active)


@app.route("/other")
def other():
    active = [
        '"nav-link"',
        '"nav-link"',
        '"nav-link"',
        '"nav-link active"'
    ]
    return render_template("other.jinja2", active=active)


if __name__ == '__main__':
    app.run(debug=True)
