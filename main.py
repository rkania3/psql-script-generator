# Main py file that manages user input
from scripts import psql_new_table

file_path = input("File path: ")
table_name = input("Table name: ")
schema = input("Schema name: ")

def main():

    script = psql_new_table.main(file_path, schema, table_name)

    print(script)

    with open("create_table_{}.txt".format(table_name), "w+") as file:
        file.write(script)