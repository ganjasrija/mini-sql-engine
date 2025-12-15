def compare(a, op, b):
    if a is None or a == "":
        return False

    try:
        if isinstance(b, (int, float)):
            a = float(a)

        return {
            '=': a == b,
            '!=': a != b,
            '>': a > b,
            '<': a < b,
            '>=': a >= b,
            '<=': a <= b
        }[op]
    except:
        raise Exception("Type mismatch in WHERE clause")


def execute_query(parsed, rows):
    if parsed['where']:
        col = parsed['where']['col']
        if col not in rows[0]:
            raise Exception(f"Column '{col}' does not exist")

        rows = [
            r for r in rows
            if compare(r[col], parsed['where']['op'], parsed['where']['val'])
        ]

    if parsed['is_count']:
        if parsed['count_target'] == '*':
            return len(rows)

        col = parsed['count_target']
        if col not in rows[0]:
            raise Exception(f"Column '{col}' does not exist")

        return sum(1 for r in rows if r[col])

    if parsed['select_cols'] == '*':
        return rows

    for col in parsed['select_cols']:
        if col not in rows[0]:
            raise Exception(f"Column '{col}' does not exist")

    return [{c: r[c] for c in parsed['select_cols']} for r in rows]
