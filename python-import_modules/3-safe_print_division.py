def safe_print_division(a, b):
    try:
        result = a / b
        return result
        
    except ZeroDivisionError:
        result = None
        return result

    finally:
        print("Inside result: {}".format(result))
        #print("{} / {} = {}".format(a,b,result))