import csv
import copy
import settings
import pymysql.cursors
from lib.sheet_handler import sheetHandler
from lib import topics
from lib import mysql_handler

from lib import utils

def format_expenses_row(expenses_row, expense_value, who_label):
    replica_expenses_row = copy.deepcopy(expenses_row)
    replica_expenses_row["quien"] = who_label
    print(expense_value)
    print(type(expense_value))
    replica_expenses_row["gasto"] = utils.format_to_float(expense_value)
    return replica_expenses_row

def dump_expenses_to_file(expenses):

    gastos_temp_handler =  open(settings.gastos_temp_file, 'w', newline='') 
    fieldnames = ["quien", "tipo", "subtipo", "mes", "dia_mes", "dia_semana", "gasto", "comentario"]
    writer = csv.DictWriter(gastos_temp_handler, fieldnames=fieldnames)
    writer.writeheader()
    for row in expenses:
        writer.writerow(row)
    gastos_temp_handler.close()

def split_expenses_by_who(sheet):

    required_header = ["mes", "dia_mes", "dia_semana", "subtipo", "tipo",  "comentario"]
    expenses = []
    for both_expense in sheet:
        expenses_row = {k:v for k, v in both_expense.items() if k in required_header}
        expense_ana = both_expense.pop("gasto_ana")
        if expense_ana != "":
            ana_formatted_row = format_expenses_row(expenses_row, expense_ana, "ana")
            expenses.append(ana_formatted_row)
        expense_juan = both_expense.pop("gasto_juan")
        if expense_juan != "":
            formatted_row = format_expenses_row(expenses_row, expense_juan, "juan")
            expenses.append(formatted_row)
    return expenses


if __name__ == "__main__":
    sheet_handler = sheetHandler()
    sheet = sheet_handler.load_sheet("Julio")

    topics_available = topics.load_topics_from_csv(settings.topics_file)

    sheet = topics.check_and_fix_topic_names(sheet, topics.load_topics_from_csv(settings.topics_file))
    expenses = split_expenses_by_who(sheet)
    
   # mysql_handler.create_expenses_table()
    
    for row in expenses:
        mysql_handler.insert_expense(row)


    