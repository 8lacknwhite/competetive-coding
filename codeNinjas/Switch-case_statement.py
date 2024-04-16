from typing import *
import math
def areaSwitchCase(ch: int, a: List[float]):
    # Write your code here
    if ch == 1:
        x= math.pi * a[0] *a[0] 
        x = round(x,5)
        return(x)
    elif ch ==2:
        x= a[0]*a[1]
        x = "{:.05f}".format(x)
        return(x)
    else:
        return(-1)

    pass