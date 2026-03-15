SIN_VALUE = {
    "sin0°": "0",
    "sin30°": "1/2",
    "sin45°": "√2/2",
    "sin60°": "√3/2",
    "sin90°": "1"
}

def sin_value(tri_ratio):
    if tri_ratio not in SIN_VALUE:
        raise ValueError(f"sin_value: {tri_ratio} is not defined")
    return SIN_VALUE[tri_ratio]