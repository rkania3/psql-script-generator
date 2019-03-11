# Code from project compressed down to one file for ease of use
# Note: As the project grows, this file will become less viable
import pandas as pd

file_path = input("File path: ")
table_name = input("Table name: ")
schema = input("Schema name: ")

type_dict = {"object": "TEXT", "int64": "NUMERIC", "float64": "REAL", "bool": "BOOLEAN", "datetime64": "TEXT", "timedelta": "TEXT", "category": "ARRAY"}

template = """CREATE TABLE IF NOT EXISTS %schema%.%table_name% ({});"""

def main():
    df = pd.read_csv(file_path, nrows=5)

    headers = df.columns.tolist()
    types = df.types

    psql_types = []

    for type in types:
        col_type = type_dict[type]
        psql_types.append(col_type)

    body = ""

    if len(headers) != len(types):
        return RuntimeError("Length of headers doesn't match number of columns found.")

    for i in range(0, len(headers)):

        if i == len(headers) - 1:
            body += str(headers[i]) + " " + str(types[i])
        else:
            body += str(headers[i]) + " " + str(types[i]) + ", "

    final = template.replace("%schema%", schema)
    final = final.replace("%table_name%", table_name)
    final = final.format(body)

    print(final)

    with open("create_table_{}.txt".format(table_name), "w+") as file:
        file.write(final)