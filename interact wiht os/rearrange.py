#!/usr/bin/env/ python
import re

def rearrange_name(name):
    result = re.search(r"^([\w .]*)\s*,\s*([\w .]*)$", name)
    if result:
        return "{} {}".format(result[2].strip(), result[1].strip())
    return name


# print(rearrange_name("Alvien,Andrianto"))