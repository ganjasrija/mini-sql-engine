import re

def parse_sql(query):
    query = query.strip().rstrip(";")

    pattern = re.compile(
        r"SELECT (.+?) FROM (\w+)(?: WHERE (.+))?$",
        re.IGNORECASE
    )

    match = pattern.match(query)
    if not match:
        raise Exception("Invalid SQL syntax")

    select_part, table, where_part = match.groups()

    is_count = select_part.upper().startswith("COUNT")
    count_target = None

    if is_count:
        count_target = select_part[6:-1].strip()
        select_cols = None
    elif select_part == "*":
        select_cols = "*"
    else:
        select_cols = [c.strip() for c in select_part.split(",")]

    where = None
    if where_part:
        w = re.match(r"(\w+)\s*(=|!=|>=|<=|>|<)\s*(.+)", where_part)
        if not w:
            raise Exception("Invalid WHERE clause")

        col, op, val = w.groups()
        val = val.strip()

        if val.startswith("'") and val.endswith("'"):
            val = val[1:-1]
        else:
            try:
                val = int(val)
            except ValueError:
                try:
                    val = float(val)
                except ValueError:
                    pass

        where = {'col': col, 'op': op, 'val': val}

    return {
        'select_cols': select_cols,
        'table': table,
        'where': where,
        'is_count': is_count,
        'count_target': count_target
    }
