def area_sum(rectangles):
    total = 0
    for rect in rectangles:
        area = rect["height"] * rect["width"]
        total += area
    return total
