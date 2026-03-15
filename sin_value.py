# sinの三角比と値の対応
SIN_VALUES = {
    "sin0°": "0",
    "sin30°": "1/2",
    "sin45°": "√2/2",
    "sin60°": "√3/2",
    "sin90°": "1"
}

# sinの三角比に対応する値を返す
def sin_value(tri_ratio):
    if tri_ratio not in SIN_VALUES:
        raise ValueError(f"sin_value: {tri_ratio} is not defined")
    return SIN_VALUES[tri_ratio]