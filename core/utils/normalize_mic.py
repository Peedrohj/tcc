import os
import csv

def normalize_mic(value: str):
    """
    @param fname: string, value to normalize

    Normalize value following Nguyen rules
    """
    if("/" in value):
        value = value.split("/")[0]

    if ("<=" in value or ">=" in value):
        return float(value.replace("<=", "").replace(">=", ""))

    if ("<" in value):
        return float(value.replace("<", ""))/2

    if (">" in value):
        return float(value.replace(">", "")) * 2

    return float(value)
