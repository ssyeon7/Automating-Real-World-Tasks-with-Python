#!/usr/bin/env python3

import json
import locale
import sys
from reports import generate
from emails import generate as generate_email
from emails import send as send_email


def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data


def format_car(car):
  """Given a car dictionary, returns a nicely formatted name."""
  return "{} {} ({})".format(
      car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
  """Analyzes the data, looking for maximums.

  Returns a list of lines that summarize the information.
  """
  max_revenue = {"revenue": 0}
  highest_car = {}
  highest_sales = {"total_sales": 0}
  for item in data:
    # Calculate the revenue generated by this model (price * total_sales)
    # We need to convert the price from "$1234.56" to 1234.56
    item_price = locale.atof(item["price"].strip("$"))
    item_revenue = item["total_sales"] * item_price
    if item_revenue > max_revenue["revenue"]:
      item["revenue"] = item_revenue
      max_revenue = item
    # TODO: also handle max sales
    if item["total_sales"] > highest_sales["total_sales"]:
      highest_sales = item
    # TODO: also handle most popular car_year
    if not item["car"]["car_year"] in highest_car.keys():
      highest_car[item["car"]["car_year"]] = item["total_sales"]
    else:
      highest_car[item["car"]["car_year"]] += item["total_sales"]

    all_values = highest_car.values()
    max_value = max(all_values)
    max_key = max(highest_car, key=highest_car.get)

  summary = [
    "The {} generated the most revenue: ${}".format(
      format_car(max_revenue["car"]), max_revenue["revenue"]),
    "The {} had the most sales: {}".format(highest_sales["car"]["car_model"], highest_sales["total_sales"]),
    "The most popular year was {} with {} sales.".format(max_key, max_value),
  ]

  return summary


def cars_dict_to_table(car_data):
  """Turns the data in car_data into a list of lists."""
  table_data = [["ID", "Car", "Price", "Total Sales"]]
  for item in car_data:
    table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
  return table_data


def main(argv):
  """Process the JSON data and generate a full report out of it."""
  data = load_data("car_sales.json")
  summary = process_data(data)
  pdf_summary = '<br/>'.join(summary)
  email_summary = '\n'.join(summary)
  # TODO: turn this into a PDF report
  generate('/tmp/cars.pdf', 'Cars report', pdf_summary, cars_dict_to_table(data))
  # TODO: send the PDF report as an email attachment
  email = generate_email('automation@example.com', 'user@example.com', 'Sales summary for last month', email_summary, '/tmp/cars.pdf')
  send_email(email)

if __name__ == "__main__":
  main(sys.argv)

