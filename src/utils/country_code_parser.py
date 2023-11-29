import numpy as np
import pandas as pd
import pycountry
import country_converter as coco


def get_country_code(row):
    country_name = str(row).lower().strip()
    country_name = country_name[:country_name.find(",")]

    if country_name in ["caribbean", "western and central africa", np.nan, "western africa", "not found", "eastern africa", "southern africa", "eastern and southern africa"]:
        return country_name, country_name
    elif country_name in ["nan", "not found"]:
        return np.nan, np.nan
    elif country_name == "yugoslavia, former":
        country_name = "Yugoslavia"
        return country_name, "YUG"
    elif country_name == "china, taiwan":
        country_name = "taiwan"
        code = coco.convert(names=[country_name], to="ISO2")
        return country_name, code
    try:
        short_name = coco.convert(names=[country_name], to="short_name")
        code = coco.convert(names=[short_name], to="ISO2")
        return short_name, code
    except:
        return np.nan, np.nan