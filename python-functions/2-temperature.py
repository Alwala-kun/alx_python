def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5/9)
    number = "{:.2f}".format(celsius)
    return number