import numpy as np


with open("list_ts","rt") as file:
    x = file.read()

with open("list_ts", "wt") as file:
    x = x.replace("./images\\", "./images/")
    file.write(x)