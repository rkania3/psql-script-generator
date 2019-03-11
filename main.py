# Main py file that manages user input
import psql_new_table

file_path = input("File path: ")
table_name = input("Table name: ")
schema = input("Schema name: ")

def main():
    print(psql_new_table.main(file_path, schema, table_name))