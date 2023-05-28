import numpy as np


with open("list_tr","rt") as file:
    x = file.read()

with open("list_tr", "wt") as file:
    x = x.replace("\main\work.23\images", "\images")
    file.write(x)