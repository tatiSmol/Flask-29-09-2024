from flask import Flask, render_template, request
from processing import process

app = Flask(__name__)


@app.route("/", methods=["get", "post"])
def index():
    message = ''
    if request.method == "POST":
        area = request.form.get("area")
        try:
            area = float(area)
            cost = process(float(area))
            message += f" Стоимость недвижимости {cost}"
        except:
            message += 'Некорректный ввод: '

    return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run()
