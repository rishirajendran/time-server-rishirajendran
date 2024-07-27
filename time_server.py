from datetime import datetime, timedelta

from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route("/time", methods=["GET"])
def server_time():
    x = datetime.now().time()
    return x.strftime("%H:%M:%S")


@app.route("/date", methods=["GET"])
def server_date():
    y = datetime.now().date()
    return y.strftime("%Y-%m-%d")


@app.route("/age", methods=["POST"])
def server_age():
    """
      in_json = {'date': "10/21/1999", 'units': "years"}
    """
    in_json = request.get_json()
    in_date_str = in_json['date']
    in_date_obj = datetime.strptime(in_date_str, "%m/%d/%Y")
    curr_date_obj = datetime.now().date()
    diff = curr_date_obj - in_date_obj.date()
    years = diff.days/365
    return jsonify(years)


@app.route("/until_next_meal/<meal>", methods=["GET"])
def server_until_next_meal(meal):
    date = datetime.now()

    if meal == "breakfast":
        meal_hour = 8
    elif meal == "lunch":
        meal_hour = 12
    elif meal == "dinner":
        meal_hour = 19

    meal_time = datetime(
        year=date.year,
        month=date.month,
        day=date.day,
        hour=meal_hour,
        minute=0
    )

    # If the meal time is in the past, add one day
    if meal_time < date:
        meal_time += timedelta(days=1)

    diff = (meal_time - date)
    diff_hours = (diff.total_seconds())/3600
    return jsonify(diff_hours)


if __name__ == "__main__":
    app.run()
    print("Server is off.")
