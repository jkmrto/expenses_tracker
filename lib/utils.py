def format_to_float(value):
    value_type = type(value)
    if value_type == int:
        return float(value)
    elif value_type == float:
        return value
    elif value_type == str:
        return float(value.replace(",", "."))