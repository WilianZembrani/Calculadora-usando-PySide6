def isValidNumber(string:str):
    valid = False
    try:
        float(string)
        valid = True
    except ValueError:
        valid = False
    return valid