import sys
from loader import load_csv
from parser import parse_sql
from engine import execute_query

if len(sys.argv) < 2:
    print("Usage: python cli.py <csv_file>")
    sys.exit(1)

data = load_csv(sys.argv[1])

print("Mini SQL Engine (type 'exit' to quit)")

while True:
    try:
        query = input("mini-sql> ")
        if query.lower() in ("exit", "quit"):
            break

        parsed = parse_sql(query)
        result = execute_query(parsed, data)

        if isinstance(result, int):
            print(f"COUNT = {result}")
        else:
            for row in result:
                print(row)
            print(f"({len(result)} rows)")

    except Exception as e:
        print(f"Error: {e}")
