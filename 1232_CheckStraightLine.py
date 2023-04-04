"""
    1232. Check If It Is a Straight Line
    GYou are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. 
    Check if these points make a straight line in the XY plane.

    :type coordinates: List[List[int]]
    :rtype: bool

    This following codes are modified for use in local editor. It may be slighly different from submission code.
"""
def checkStraightLine(coordinates):
    (x1, y1), (x2, y2) = coordinates[0], coordinates[1]
    for x3, y3 in coordinates[2:]:
	    if (y2 - y1) * (x3 - x1) != (y3 - y1) * (x2 - x1):
		    return False
    # return True // uncomment this (it threw an error when run in local editor, so i comment it.)