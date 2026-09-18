def equilateral(sides):
    if sides[0] <= 0 or sides[1] <= 0 or sides[2] <= 0:
        return False

    if sides[0] == sides[1] == sides[2]:
        return True

    return False

def isosceles(sides):
    if sides[0] == 1 or sides[1] == 1 or sides[2] == 1:
        return False
    if sides[0]==sides[1]:
        return True
    elif sides[0]==sides[2]:
        return True
    elif sides[1]==sides[2]:
        return True
    else:
        return False

def scalene(sides):
    if sides[0] + sides[1] <= sides[2]:
        return False
    elif sides[0] + sides[2] <= sides[1]:
        return False
    elif sides[1] + sides[2] <= sides[0]:
        return False
    elif sides[0] == sides[1]:
        return False
    elif sides[0] == sides[2]:
        return False
    elif sides[1] == sides[2]:
        return False
    else:
        return True
