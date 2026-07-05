from datetime import datetime

from flask import Flask, redirect, render_template, request, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///converter.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Convert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    input_value = db.Column(db.String(20), nullable=False)
    output_value = db.Column(db.String(20), nullable=False)
    conversion_type = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)


def perform_conversion(value, conversion_type, from_unit):
    if conversion_type == "Length":
        if from_unit == "KM":
            result = value * 1000
            to_unit = "M"
        else:
            result = value / 1000
            to_unit = "KM"

    elif conversion_type == "Weight":
        if from_unit == "KG":
            result = value * 1000
            to_unit = "G"
        else:
            result = value / 1000
            to_unit = "KG"

    elif conversion_type == "Height":
        if from_unit == "IN":
            result = value * 2.54
            to_unit = "CM"
        else:
            result = value / 2.54
            to_unit = "IN"

    elif conversion_type == "Temperature":
        if from_unit == "C":
            result = (value * 9 / 5) + 32
            to_unit = "F"
        else:
            result = (value - 32) * 5 / 9
            to_unit = "C"

    return result, to_unit


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        try:
            user_choice = int(request.form.get("choice"))
            val = float(request.form.get("value"))

            if user_choice == 1:
                conversion_type = "Length"
                from_unit = "KM"

            elif user_choice == 2:
                conversion_type = "Length"
                from_unit = "M"

            elif user_choice == 3:
                conversion_type = "Weight"
                from_unit = "G"

            elif user_choice == 4:
                conversion_type = "Weight"
                from_unit = "KG"

            elif user_choice == 5:
                conversion_type = "Height"
                from_unit = "IN"

            elif user_choice == 6:
                conversion_type = "Height"
                from_unit = "CM"

            elif user_choice == 7:
                conversion_type = "Temperature"
                from_unit = "C"
            elif user_choice == 8:
                conversion_type = "Temperature"
                from_unit = "F"

            res, to_unit = perform_conversion(val, conversion_type, from_unit)

            input_val = f"{val} {from_unit}"
            output_val = f"{res} {to_unit}"

            data = Convert(input_value=input_val, output_value=output_val, conversion_type=conversion_type, created_at=datetime.now())
            db.session.add(data)
            db.session.commit()
            result = f"{input_val} = {output_val}"
        except (ValueError, TypeError):
            error = "Invalid numeric value entered. Please try again."

    return render_template("index.html", result=result, error=error)


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_record(id):
    record = Convert.query.get_or_404(id)
    error = None

    if request.method == "POST":
        try:
            updated_value = float(request.form.get("updated_value"))
            from_unit = record.input_value.split()[-1]
            res, to_unit = perform_conversion(updated_value, record.conversion_type, from_unit)
            record.input_value = f"{updated_value} {from_unit}"
            record.output_value = f"{res} {to_unit}"
            db.session.commit()

            return redirect(url_for("history"))
        except (ValueError, TypeError):
            error = "Invalid numeric value entered. Please try again."

    current_val = record.input_value.split()[0] if record.input_value else ""
    return render_template("edit.html", record=record, current_val=current_val, error=error)


@app.route("/history")
def history():
    records = Convert.query.all()
    return render_template("history.html", history=records)


@app.route("/delete/<int:id>", methods=["POST"])
def delete_record(id):
    record = Convert.query.get_or_404(id)
    db.session.delete(record)
    db.session.commit()
    return redirect(url_for("history"))


if __name__ == "__main__":
    app.run(debug=True)
