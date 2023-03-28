"""
    1779. Find Nearest Point That Has the Same X or Y Coordinate
    You are given two integers, x and y, which represent your current location on a Cartesian grid: (x, y). 
    You are also given an array points where each points[i] = [ai, bi] represents that a point exists at (ai, bi). 
    A point is valid if it shares the same x-coordinate or the same y-coordinate as your location.

    Return the index (0-indexed) of the valid point with the smallest Manhattan distance from your current location. 
    If there are multiple, return the valid point with the smallest index. If there are no valid points, return -1.

    The Manhattan distance between two points (x1, y1) and (x2, y2) is abs(x1 - x2) + abs(y1 - y2).

    :type x: int
    :type y: int
    :type points: List[List[int]]
    :rtype: int

    This following codes are modified for use in local editor. It may be slighly different from submission code.
"""

def nearestValidPoint(self, x, y, points):
        min_dis= 10000 
        ind = -1
        for i in range (len (points)):
            if points[i][0] == x or points [i][1] == y:
                mandist = abs(points[i][0] -x) + abs(points[i][1] - y)
                if mandist < min_dis :
                    min_dis = mandist
                    ind = i
        return ind