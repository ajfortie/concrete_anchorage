"""The functions in this script will define the geometric properties
of the anchors passed to them"""

#Calculate Center of gravity of anchors
from logging import exception


def anc_CoG(x_pts,y_pts):
    
    if len(x_pts) != len(y_pts):
        raise exception("x_pts and y_pts lists are not the same length. Verify function inputs")
    
    num = len(x_pts)
    x_sum = 0
    y_sum = 0

    for i in range(num):
        x_sum += x_pts[i]
        y_sum += y_pts[i]

    return [x_sum/num,y_sum/num]

def anc_Acno(heff):
    return 9*heff**2
