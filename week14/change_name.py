import numpy as np


with open("./list_train", "rt") as file:
    x = file.read()

with open("./list_tr", "wt") as file:
    x = x.replace("/", "\\")
    file.write(x)