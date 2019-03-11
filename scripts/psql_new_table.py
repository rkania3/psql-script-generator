# Create PSQL script for creating new table
import pandas as pd
from utils import config

template = """CREATE TABLE IF NOT EXISTS %schema%.%table_name% ({});"""

def main(file, schema, table_name, option="default"):

    ret_str = ""

    headers = file.columns.tolist()

    # If default option is selected, make a guess of cols
    if option == "default":
        df = pd.read_csv(file, nrows = 5)

        types = df.types

        psql_types = []

        for type in types:
            col_type = config.get("types", str(type))
            psql_types.append(col_type)

    body = format_sql(headers, psql_types)

    ret_str = template.replace("%schema%", schema)
    ret_str = ret_str.replace("%table_name%", table_name)
    ret_str = ret_str.format(body)

    return ret_str

def format_sql(headers, types):

    ret_str = ""

    if len(headers) != len(types):
        return ret_str

    for i in range(0, len(headers)):

        if i == len(headers) - 1:
            ret_str += str(headers[i]) + " " + str(types[i])
        else:
            ret_str += str(headers[i]) + " " + str(types[i]) + ", "

    return ret_str