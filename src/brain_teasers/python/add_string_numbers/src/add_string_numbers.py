
def add_string_numbers(num1, num2):
    try:
        result = str(float(num1) + float(num2))
    except ValueError:
        result = str(int(num1) + int(num2))

    return result
