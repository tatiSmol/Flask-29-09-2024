from flask import Flask, render_template, request

from processing import process, preprocess

app = Flask(__name__)


@app.route("/", methods=["get", "post"])
def index():
    message = ''
    if request.method == "POST":
        area = request.form.get("area")
        print("done 1")
        try:
            area = float(area)
            print("done 2")
        except:
            area = 0
            message += 'Некорректный ввод. Установлено значение по умолчанию. '
        scaled_area = preprocess(area)
        print("done 3")
        cost = process(scaled_area)
        print("done 4")
        message += f"Стоимость недвижимости {cost} рублей"
    return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run()
