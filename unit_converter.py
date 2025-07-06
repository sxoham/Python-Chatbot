conversion_table = {
    ("km", "miles"): lambda x: x * 0.621371,
    ("miles", "km"): lambda x: x / 0.621371,
    ("kg", "pounds"): lambda x: x * 2.20462,
    ("pounds", "kg"): lambda x: x / 2.20462,
    ("celsius", "fahrenheit"): lambda x: (x * 9/5) + 32,
    ("fahrenheit", "celsius"): lambda x: (x - 32) * 5/9,
    ("cm", "inches"): lambda x: x * 0.393701,
    ("inches", "cm"): lambda x: x / 0.393701,
    ("liters", "gallons"): lambda x: x * 0.264172,
    ("gallons", "liters"): lambda x: x / 0.264172,
}

def convert_unit(amount, from_unit, to_unit):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    key = (from_unit, to_unit)

    if key in conversion_table:
        result = conversion_table[key](amount)
        return f"{amount} {from_unit} = {round(result, 4)} {to_unit}"
    else:
        return f" Conversion from '{from_unit}' to '{to_unit}' not supported."
